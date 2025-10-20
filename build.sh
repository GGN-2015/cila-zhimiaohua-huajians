#!/bin/bash

# 先获取脚本的相对路径（$0 是脚本名）
script_path="$0"

# 解析符号链接，得到绝对路径
abs_script_path=$(readlink -f "$script_path" 2>/dev/null)

# 提取脚本所在的目录路径
script_dir=$(dirname "$abs_script_path")

# 执行构建脚本
python3 $script_dir/src/exp/show_and_replace.py
