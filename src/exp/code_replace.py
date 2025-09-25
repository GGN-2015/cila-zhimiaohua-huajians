import re

def replace_generated_code(original_string, new_content):
    """
    替换字符串中位于// >>> PYTHON_GENERATED_CODE >>>和// <<< PYTHON_GENERATED_CODE <<<之间的内容
    支持处理多行内容

    参数:
        original_string: 包含需要处理的代码块的原始字符串
        new_content: 要替换进去的新内容（可以包含多行）

    返回:
        替换后的字符串
    """
    # 正则表达式模式，用于匹配两个标记之间的内容
    # 使用非贪婪匹配，确保只匹配到第一个结束标记
    pattern = r'(// >>> PYTHON_GENERATED_CODE >>>\n)(.*?)(// <<< PYTHON_GENERATED_CODE <<<)'

    # 使用re.DOTALL让.匹配包括换行符在内的所有字符
    # 保留前后标记，只替换中间内容
    def replace_match(match):
        return f"{match.group(1)}{new_content}\n{match.group(3)}"

    # 执行替换操作
    modified_string = re.sub(
        pattern,
        replace_match,
        original_string,
        flags=re.DOTALL  # 关键标志，确保.匹配换行符
    )

    return modified_string

# 示例用法 - 特别展示多行内容的处理
if __name__ == "__main__":
    # 原始字符串，包含多行生成代码
    original = """def main():
    print("开始执行")

    // >>> PYTHON_GENERATED_CODE >>>
    # 这是生成的代码块
    # 包含多行内容
    a = 10
    b = 20
    result = a + b
    print(f"结果: {result}")
    // <<< PYTHON_GENERATED_CODE <<<

    print("执行结束")
    return"""

    # 新的多行内容
    new_code = """# 新的生成代码
# 也包含多行
x = 5
y = 3
product = x * y
print(f"乘积: {product}")
print("计算完成")"""

    # 执行替换
    result = replace_generated_code(original, new_code)

    # 输出结果
    print("替换后的结果:")
    print("-" * 50)
    print(result)
    print("-" * 50)
