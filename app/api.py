# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 8:49 下午
# @Author  : HuangSir
# @FileName: api.py
# @Software: PyCharm
# @Desc:

import logging
from datetime import datetime
logging.basicConfig(filename=f"log/{str(datetime.now().date())}.log",
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

from .routers import risk_router_init

from fastapi import FastAPI

def create_app():
    app = FastAPI(title= '风险评分模型',description='新老客风险评分模型,仅供平台内调用',version='1.0')
    risk_router_init(app)
    return app