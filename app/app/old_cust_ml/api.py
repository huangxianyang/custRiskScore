# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:43 下午
# @Author  : HuangSir
# @FileName: api.py
# @Software: PyCharm
# @Desc:老客信用分模型主程序

import logging

from app.app.applist_ml.applist_model import AppListML
from app.app.old_cust_ml.old_cust_model import OldCustModel

apl = AppListML()
ocl = OldCustModel()

def old_cust_main(data):

    user_id = data['user_id']
    busi_id = data['busi_id']
    ml_data = data['data']

    appList_data = {'apply_time':ml_data['apply_time'],
                     'app_list':ml_data['app_list'],
                     'add_list':ml_data['add_list']}

    res = apl.predict(appList_data)
    logging.warning(res)
    ml_data['FRAUD_PROB'] = res['prob']

    score = ocl.predict(data=ml_data)

    return {'user_id':user_id,
            'busi_id':busi_id,
            'new_cust_score':score,
            'code':1000,
            'msg':'处理成功',
            'detail':''}
