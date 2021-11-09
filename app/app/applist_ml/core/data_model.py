# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:55 下午
# @Author  : HuangSir
# @FileName: data_model.py
# @Software: PyCharm
# @Desc: applist + adbook

from pydantic import BaseModel,Field

class AppList(BaseModel):
    """appList数据模型"""
    firstTime:str = Field(default=None, title='首次安装时间', example='2020-06-25 09:39:24',
                          description='yyyy-mm-dd HH:MM:SS')
    lastTime:str = Field(default=None, title='最近更新时间', example='2020-06-25 09:39:24',
                         description='yyyy-mm-dd HH:MM:SS')

    name:str = Field(default=None, title='名称', example='โคลนโทรศัพท์',description='app名称')
    packageName:str = Field(default=None, title='包名', example='com.coloros.backuprestore',description='包名')
    systemApp:str = Field(default=None, title='系统版本', example='1',description='')
    versionCode:str =  Field(default=None, title='5.0.50', example='1',description='')

class AdList(BaseModel):
    """通讯录"""
    last_time:str = Field(default=None, title='更新时间', example='2020-06-25 09:39:24',
                          description='yyyy-mm-dd HH:MM:SS')
    other_mobile:str = Field(default=None, title='对方号码', example='4250719194',
                          description='对方号码')
    other_name:str = Field(default=None, title='对方姓名', example='กรุง',
                          description='对方姓名')


