# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 3:58 下午
# @Author  : HuangSir
# @FileName: data_model.py
# @Software: PyCharm
# @Desc:

from pydantic import BaseModel, Field
from typing import List
from app.app.applist_ml.core import AppList, AdList


class DataMl(BaseModel):
    """老客数据模型"""
    # 2
    corp_no: int = Field(default=None, title='CORP_NO', example=1, description='客户端版本,1,4,12')
    # 3,4
    ram_x:float = Field(default=None, title='RAM_X', example=3.25, description='RAM: 3.25 GB/8.01 GB, 截取第一个')
    ram_y:float = Field(default=None, title='RAM_Y', example=8.01, description='RAM: 3.25 GB/8.01 GB, 截取第二个')
    # 5,6,7
    open_power: int = Field(default=None, title='OPEN_POWER', example=1, description='开始电量')
    complete_apply_power: int = Field(default=None, title='COMPLETE_APPLY_POWER', example=1, description='申请完成电量')
    open_complete_diff_power:int = Field(default=None, title='OPEN_COMPLETE_DIFF_POWER', example=1,
                                         description='电量消耗, OPEN_POWER - COMPLETE_APPLY_POWER')
    # 8
    education: int = Field(default=None, title='教育程度', example=1,
                           description='1:小学、2:初中、3:高中 4:大专、 5:本科、6:其他')
    # 9
    age: int = Field(default=None, title='年龄', example=30, description="下单时间减去 - 出生日期")
    # 10
    id_reg_prod_num: int = Field(default=0, title='身份证注册过的产品数量', example=1, description='0,1,2,3 ...')
    # 11
    id_cor_device_num: int = Field(default=0, title='身份证关联设备数量', example=1, description='')
    # 12
    id_cor_mobile_num: int = Field(default=0, title='身份证关联手机号数量', example=1, description='0,1,2,3 ...')
    # 13
    id_cor_name_num: int = Field(default=0, title='身份证关联姓名数量', example=1, description='0,1,2,3 ...')
    # 14
    mobile_reg_prod_num: int = Field(default=0, title='手机号注册过的产品数量', example=1, description='0,1,2,3 ...')
    # 15
    mobile_cor_id_num: int = Field(default=0, title='手机号关联身份证数量', example=1, description='0,1,2,3 ...')
    # 16
    mobile_cor_device_num: int = Field(default=0, title='手机号关联设备数量', example=1, description='0,1,2,3 ...')
    # 17
    contact_cor_cust_num: int = Field(default=0, title='紧急联系人关联用户数量', example=1, description='0,1,2,3 ...')
    # 18
    contact_cor_repay_cust_num: int = Field(default=0, title='紧急联系人关联还款用户数量', example=1, description='0,1,2,3 ...')
    # 19
    re_30d_apply_num: int = Field(default=0, title='近30天申请次数', example=1, description='0,1,2,3 ...')
    # 20
    re_7d_apply_num: int = Field(default=0, title='近7天申请次数', example=1, description='0,1,2,3 ...')
    # 21
    total_apply_num: int = Field(default=0, title='历史累计申请次数', example=1, description='0,1,2,3 ...')
    # 22
    re_90d_apply_num: int = Field(default=0, title='近90天申请次数', example=1, description='0,1,2,3 ...')
    # 23
    re_24h_apply_num: int = Field(default=0, title='近24小时申请次数', example=1, description='0,1,2,3 ...')
    # 24
    repay_total_num: int = Field(default=0, title='历史累计还款次数', example=1, description='0,1,2,3 ...')
    # 25
    loaning_busi_num: int = Field(default=0, title='当前在途订单数量', example=1, description='0,1,2,3 ...')
    # 26
    reject_total_num: int = Field(default=0, title='历史累计拒绝次数', example=1, description='0,1,2,3 ...')
    # 27
    loan_again_num: int = Field(default=0, title='FUDAI_NUM', example=1, description='0,1,2,3 ...')
    # 28
    loaning_busi_amt: int = Field(default=0, title='当前共债金额', example=1, description='0,1,2,3 ...')
    # 29
    apply_time: str = Field(default=None, title='申请时间', example='2021-06-25 09:39:24',
                            description='yyyy-mm-dd HH:MM:SS')

    app_list: List[AppList] = Field(default=..., title='appList', description='applist详情')

    add_list: List[AdList] = Field(default=..., title='通讯录',description='通讯录详情')


class OldCustData(BaseModel):
    user_id: str = Field(default='83595', title='用户id,可用手机号')
    busi_id: str = Field(default='1020210717125639000083595', title='交易订单号')
    data: DataMl = Field(default=..., title='模型数据')
