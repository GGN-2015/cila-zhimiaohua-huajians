#!/bin/bash

# 先获取脚本的相对路径（$0 是脚本名）
script_path="$0"

# 解析符号链接，得到绝对路径
abs_script_path=$(readlink -f "$script_path" 2>/dev/null)

# 提取脚本所在的目录路径
script_dir=$(dirname "$abs_script_path")

# 执行构建脚本
python3 $script_dir/src/exp/show_and_replace.py

# 检查 neko 命令是否存在
if command -v neko &> /dev/null; then
    echo "neko found，execute neko sync_remote..."
    neko quick_push
    neko sync_remote
else
    echo "neko not found!，sync remote yourself!"
    exit 1
fi
