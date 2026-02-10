#!/bin/bash

# 创建日志目录
mkdir -p logs

# 生成模拟 Nginx 访问日志
cat > logs/access.log << 'EOF'
192.168.1.1 - - [08/Feb/2026:08:00:01 +0800] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
192.168.1.2 - - [08/Feb/2026:08:00:02 +0800] "GET /api/data HTTP/1.1" 404 512 "-" "curl/7.64.1"
192.168.1.1 - - [08/Feb/2026:08:00:03 +0800] "POST /login HTTP/1.1" 200 2048 "-" "Mozilla/5.0"
192.168.1.3 - - [08/Feb/2026:08:00:04 +0800] "GET /admin HTTP/1.1" 403 256 "-" "Mozilla/5.0"
192.168.1.1 - - [08/Feb/2026:08:00:05 +0800] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
EOF

echo "测试环境构建完成！"