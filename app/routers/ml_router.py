# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 11:35 下午
# @Author  : HuangSir
# @FileName: ml_router.py
# @Software: PyCharm
# @Desc: 新老客模型路由


from fastapi import APIRouter

from app.app.new_cust_ml.core import NewCustData
from app.app.new_cust_ml import new_cust_main

from app.app.old_cust_ml.core import OldCustData
from app.app.old_cust_ml import old_cust_main

ml_router = APIRouter()

@ml_router.post('/new/score',tags=['新客信用评分'])
async def new_cust_risk_score(data:NewCustData):
    data = data.dict()
    res = new_cust_main(data)
    return res

@ml_router.post('/old/score',tags=['老客信用评分'])
async def old_cust_risk_score(data:OldCustData):
    data = data.dict()
    res = old_cust_main(data)
    return res
