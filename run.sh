#!/bin/bash

# 🚀 Space Shooter - 快速启动脚本

echo "🚀 正在启动 Space Shooter 游戏..."
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "请先安装 Python 3.7 或更高版本"
    exit 1
fi

# 检查 Pygame 是否安装
if ! python3 -c "import pygame" &> /dev/null; then
    echo "⚠️  Pygame 未安装，正在安装..."
    pip3 install pygame
    if [ $? -ne 0 ]; then
        echo "❌ Pygame 安装失败"
        echo "请手动运行: pip3 install pygame"
        exit 1
    fi
fi

echo "✅ 环境检查完成"
echo "🎮 启动游戏..."
echo ""

# 运行游戏
python3 main.py
