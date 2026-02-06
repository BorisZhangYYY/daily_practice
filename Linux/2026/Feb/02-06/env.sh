#!/bin/bash
# 环境构建脚本 - 执行此脚本创建测试环境
mkdir -p $(pwd)/tmp/test_logs $(pwd)/tmp/archive_logs
# 创建测试日志文件（包含不同时间戳）
for i in {1..20}; do
    echo "This is test log file $i" > $(pwd)/tmp/test_logs/test_$i.log
    # MacOS 兼容写法：使用 date -v 计算日期，touch -t 设置时间
    timestamp=$(date -v -${i}d +%Y%m%d%H%M)
    touch -t "$timestamp" $(pwd)/tmp/test_logs/test_$i.log
done
echo "测试环境已创建："
echo "日志目录：$(pwd)/tmp/test_logs（包含20个不同日期的.log文件）"
echo "归档目录：$(pwd)/tmp/archive_logs"
echo "请编写脚本实现上述功能，完成后可执行："
echo "bash your_script.sh $(pwd)/tmp/test_logs $(pwd)/tmp/archive_logs 7"
