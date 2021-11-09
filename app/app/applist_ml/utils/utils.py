# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 7:05 下午
# @Author  : HuangSir
# @FileName: utils.py
# @Software: PyCharm
# @Desc:

import sys
sys.path.append('..')

def load_txt_feat(file:str):
    with open(file,'r') as f:
        feature = f.read().split('\n')
        feature = [i for i in feature if i]
        return feature