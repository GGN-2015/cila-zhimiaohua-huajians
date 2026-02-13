# 用于生成 zhimiaohua 后台词典 PDF
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
WORDS_FOLDER = os.path.join(DIRNOW, "exp")
IMG_FOLDER = os.path.join(DIRNOW, "img")
SUFFIX = ".txt"

WORD_INDEX_PLACEHOLDER = "[[[WORD_INDEX]]]"
MD_PATH = os.path.join(DIRNOW, "zhimiaohua-huajians-backend.md")

# 获取 zhimiaohua 全部词汇
def get_all_words() -> list[str]:
    words = []
    for filename in os.listdir(WORDS_FOLDER):
        if filename.lower().endswith(SUFFIX):
            words.append(filename[:-len(SUFFIX)])
    return sorted(words)

# 检查一个词语是否有手写方法
def has_handwrite(word:str) -> bool:
    imgpath = os.path.join(IMG_FOLDER, word + ".png")
    return os.path.isfile(imgpath)

# 获取指定词汇的含义
def get_explain(word:str) -> str:
    filepath = os.path.join(WORDS_FOLDER, word + ".txt")

    # 检查对应的词汇文件是否存在
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as fp:
            raw_content = fp.read().rstrip() + "\n\n"

        # 添加释义编号
        in_term_index = 0
        while raw_content.find(">>>") != -1:
            pos = raw_content.find(">>>")
            in_term_index += 1
            raw_content = raw_content[:pos] + f"### ({WORD_INDEX_PLACEHOLDER}.{in_term_index})" + raw_content[pos+3:]

        imgpath = os.path.join(IMG_FOLDER, word + ".png")
        if os.path.isfile(imgpath):
            img_content = "### 写法\n\n" + f"<img src=\"{os.path.relpath(imgpath, DIRNOW)}\" style=\"width: 150px\">\n\n"
        else:
            img_content = ""
        
        content = (f"## ({WORD_INDEX_PLACEHOLDER}) {word}\n\n" + img_content +
                   raw_content)
    else:
        content = "未找到该词汇的含义"

    return content

# 获取年月日
def get_date_str() -> str:
    from datetime import datetime
    current_time = datetime.now()
    date_str = current_time.strftime("%Y-%m-%d")
    return date_str

# 生成全文的 markdown
def generate_markdown_content() -> str:
    content = f"# zhimiaohua 输入法后台词典 \n\n导出日期： {get_date_str()}\n\n"
    
    # 生成目录
    content += "## 目录\n\n"
    content += "注：加粗词条表示该词汇已有手写文字\n\n"
    for idx, word in enumerate(get_all_words()):
        index = idx + 1

        if not has_handwrite(word):
            content += f"- ({index}) {word}\n\n"
        else:
            content += f"- ({index}) **{word}**\n\n"

    # 生成内容
    for idx, word in enumerate(get_all_words()):
        index = idx + 1
        content += f"<!-- BEGIN: {word} -->\n\n"
        content += get_explain(word).replace(WORD_INDEX_PLACEHOLDER, f"{index}")
        content += f"<!-- END: {word} -->\n\n"

    return content

def create_md_file():
    with open(MD_PATH, "w", encoding="utf-8") as fp:
        fp.write(generate_markdown_content())

if __name__ == "__main__":
    create_md_file()
