#!/bin/bash
conda create -n mlvenv python=3.8
source activate mlvenv
echo "完成虚拟环境mlvenv创建"
target=$(dirname "$PWD")
echo "$target"
cd $target
pip install -r requirements.txt
echo "完成依赖安装"
