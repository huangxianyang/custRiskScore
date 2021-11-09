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
    """新客数据模型"""
    work_type: int = Field(default=None, title='职位', example=1,
                           description='1:正式员工(2年以下); 2:正式员工(2年以上); 3:经理; 4:高管; 5:外包; 6:临时合同工')

    education: int = Field(default=None, title='教育程度', example=1,
                           description='1:小学、2:初中、3:高中 4:大专、 5:本科、6:其他')

    cust_type: int = Field(default=None, title='用户类型', example=1,
                           description='1:私营业主、2:上班族、3:自由职业(摩的司机/农民/渔夫等) 4:退休/待业/无业/家庭主妇')

    corp_no: int = Field(default=None, title='CORP_NO', example=1, description='客户端版本,1,4,12')

    id_cor_device_num: int = Field(default=0, title='身份证关联设备数量', example=1, description='')

    screen_l: int = Field(default=None, title='屏幕分辨率_L', example=720, description='720×1600 -320, 截取第一个')
    screen_w: int = Field(default=None, title='屏幕分辨率_W', example=1600, description='720×1600 -320, 截取第二个')
    screen_h: int = Field(default=None, title='屏幕分辨率_H', example=320, description='720×1600 -320, 截取第三个')

    id_reg_prod_num: int = Field(default=0, title='身份证注册过的产品数量', example=1, description='0,1,2,3 ...')

    re_30d_apply_num: int = Field(default=0, title='近30天申请次数', example=1, description='0,1,2,3 ...')

    complete_apply_power: int = Field(default=None, title='COMPLETE_APPLY_POWER', example=1, description='申请完成电量')
    open_complete_diff_power:int = Field(default=None, title='OPEN_COMPLETE_DIFF_POWER', example=1,
                                         description='电量消耗, OPEN_POWER - COMPLETE_APPLY_POWER')
    open_power:int = Field(default=None,title='OPEN_POWER',example=1, description='开始电量')

    re_7d_apply_num: int = Field(default=0, title='近7天申请次数', example=1, description='0,1,2,3 ...')

    total_apply_num: int = Field(default=0, title='历史累计申请次数', example=1, description='0,1,2,3 ...')

    ram_x:float = Field(default=None, title='RAM_X', example=3.25, description='RAM: 3.25 GB/8.01 GB, 截取第一个')
    ram_y:float = Field(default=None, title='RAM_Y', example=8.01, description='RAM: 3.25 GB/8.01 GB, 截取第二个')

    id_cor_mobile_num: int = Field(default=0, title='身份证关联手机号数量', example=1, description='0,1,2,3 ...')

    id_cor_name_num: int = Field(default=0, title='身份证关联姓名数量', example=1, description='0,1,2,3 ...')

    re_90d_apply_num: int = Field(default=0, title='近90天申请次数', example=1, description='0,1,2,3 ...')

    age: int = Field(default=None, title='年龄', example=30, description="下单时间减去 - 出生日期")

    re_24h_apply_num: int = Field(default=0, title='近24小时申请次数', example=1, description='0,1,2,3 ...')

    mobile_cor_id_num: int = Field(default=0, title='手机号关联身份证数量', example=1, description='0,1,2,3 ...')

    apply_time: str = Field(default=None, title='申请时间', example='2021-06-25 09:39:24',
                            description='yyyy-mm-dd HH:MM:SS')

    app_list: List[AppList] = Field(default=..., title='appList', description='applist详情')

    add_list: List[AdList] = Field(default=..., title='通讯录',description='通讯录详情')


class NewCustData(BaseModel):
    user_id: str = Field(default='83595', title='用户id,可用手机号')
    busi_id: str = Field(default='1020210717125639000083595', title='交易订单号')
    data: DataMl = Field(default=..., title='模型数据')
