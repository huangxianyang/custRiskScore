# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 12:16 下午
# @Author  : HuangSir
# @FileName: __init__.py
# @Software: PyCharm
# @Desc: api蓝图

from .ml_router import ml_router

def risk_router_init(app):
    app.include_router(
        ml_router
    )
