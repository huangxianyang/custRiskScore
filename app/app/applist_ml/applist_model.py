# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 10:26 下午
# @Author  : HuangSir
# @FileName: applist_model.py
# @Software: PyCharm
# @Desc: appList模型主程序

import sys

sys.path.append('..')
import logging
import pandas as pd
import numpy as np
from datetime import datetime
import time
import joblib

from app.app.applist_ml.utils import load_txt_feat


class AppListML:
    """appList模型主程序"""

    def __init__(self):
        self.file = 'app/app/applist_ml/static/'
        self.model = joblib.load(self.file + 'app_add_1104.pkl')
        self.feat = load_txt_feat(self.file + 'in_ml_col.txt')
        self.comp = pd.read_excel(self.file + 'comp.xlsx', names=['package', 'name'])

    def __get_feat(self, data: dict):
        """获取特征"""
        df = pd.DataFrame(data['app_list'])
        df['apply_time'] = data['apply_time']
        try:
            df['apply_time'] = pd.to_datetime(df['apply_time'])
        except:
            logging.error(f"申请时间戳转换错误:{data['apply_time']}")
            df['apply_time'] = datetime.now()

        df['lastTime'] = pd.to_datetime(df['lastTime'])
        self_df = df[df.lastTime > datetime(2010, 1, 1)]
        day_tag = pd.DataFrame(pd.cut((self_df['apply_time'] - self_df['lastTime']).dt.days,
                                      bins=[0, 1, 3, 7, 15, 30, 60, np.inf], include_lowest=True,
                                      labels=['self_1', 'self_3', 'self_7', 'self_15', 'self_30', 'self_60',
                                              'self_90']).value_counts()).T
        day_tag.columns = day_tag.columns.tolist()
        self_comp = df[df.packageName.isin(self.comp.package)]
        comp_day_tag = pd.DataFrame(pd.cut((self_comp['apply_time'] - self_comp['lastTime']).dt.days,
                                           bins=[0, 1, 3, 7, 15, 30, 60, np.inf], include_lowest=True,
                                           labels=['comp_1', 'comp_3', 'comp_7', 'comp_15', 'comp_30', 'comp_60',
                                                   'comp_90']).value_counts()).T
        comp_day_tag.columns = comp_day_tag.columns.tolist()
        day_tag['all_self_cnt'] = self_df.shape[0]
        day_tag['all_self_comp_cnt'] = self_comp.shape[0]
        day_tag['all_cnt'] = df.shape[0]

        # 获取add联系人数目
        add_df = pd.DataFrame(data['add_list'])
        lxr_num = add_df.shape[0]
        day_tag['lxr_num'] = lxr_num

        all_tag = pd.concat([day_tag, comp_day_tag], axis=1)

        all_tag['self_1_pct'] = all_tag['self_1'] / all_tag['all_self_cnt']
        all_tag['self_1_all_pct'] = all_tag['self_1'] / all_tag['all_cnt']
        all_tag['comp_1_pct'] = all_tag['comp_1'] / all_tag['all_self_comp_cnt']
        all_tag['self_3_all'] = all_tag['self_1'] + all_tag['self_3']
        all_tag['self_7_all'] = all_tag['self_1'] + all_tag['self_3'] + all_tag['self_7']
        all_tag['self_15_all'] = all_tag['self_1'] + all_tag['self_3'] + all_tag['self_7'] + all_tag['self_15']
        all_tag['self_30_all'] = all_tag['self_1'] + all_tag['self_3'] + all_tag['self_7'] + all_tag['self_15'] + \
                                 all_tag[
                                     'self_30']
        all_tag['self_60_all'] = all_tag['self_1'] + all_tag['self_3'] + all_tag['self_7'] + all_tag['self_15'] + \
                                 all_tag[
                                     'self_30'] + all_tag['self_60']
        all_tag['self_90_all'] = all_tag['self_1'] + all_tag['self_3'] + all_tag['self_7'] + all_tag['self_15'] + \
                                 all_tag[
                                     'self_30'] + all_tag['self_60'] + all_tag['self_90']
        all_tag['self_3_1'] = all_tag['self_3'] - all_tag['self_1']
        all_tag['self_7_3'] = all_tag['self_7'] - all_tag['self_3']
        all_tag['self_15_7'] = all_tag['self_15'] - all_tag['self_7']
        all_tag['self_30_15'] = all_tag['self_30'] - all_tag['self_15']
        all_tag['self_60_30'] = all_tag['self_60'] - all_tag['self_30']
        all_tag['comp_3_all'] = all_tag['comp_1'] + all_tag['comp_3']
        all_tag['comp_7_all'] = all_tag['comp_1'] + all_tag['comp_3'] + all_tag['comp_7']
        all_tag['comp_15_all'] = all_tag['comp_1'] + all_tag['comp_3'] + all_tag['comp_7'] + all_tag['comp_15']
        all_tag['comp_30_all'] = all_tag['comp_1'] + all_tag['comp_3'] + all_tag['comp_7'] + all_tag['comp_15'] + \
                                 all_tag[
                                     'comp_30']
        all_tag['comp_60_all'] = all_tag['comp_1'] + all_tag['comp_3'] + all_tag['comp_7'] + all_tag['comp_15'] + \
                                 all_tag[
                                     'comp_30'] + all_tag['comp_60']
        all_tag['comp_90_all'] = all_tag['comp_1'] + all_tag['comp_3'] + all_tag['comp_7'] + all_tag['comp_15'] + \
                                 all_tag[
                                     'comp_30'] + all_tag['comp_60'] + all_tag['comp_90']
        all_tag['comp_3_all_pct'] = all_tag['comp_3_all'] / all_tag['self_3_all']
        all_tag['comp_7_all_pct'] = all_tag['comp_7_all'] / all_tag['self_7_all']
        all_tag['comp_15_all_pct'] = all_tag['comp_15_all'] / all_tag['self_15_all']
        all_tag['comp_30_all_pct'] = all_tag['comp_30_all'] / all_tag['self_30_all']
        all_tag['comp_60_all_pct'] = all_tag['comp_60_all'] / all_tag['self_60_all']
        all_tag['comp_90_all_pct'] = all_tag['comp_90_all'] / all_tag['self_90_all']
        all_tag['all_self_pct'] = all_tag['all_self_cnt'] / all_tag['all_cnt']
        all_tag['all_self_comp_pct'] = all_tag['all_self_comp_cnt'] / all_tag['all_cnt']

        return all_tag[self.feat]

    def predict(self, data: dict):
        """
        输出逾期概率
        """
        if len(data['app_list']) == 0 or len(data['add_list']) == 0:
            return {'prob': -999,'msg': 'input empty','status_code':101}
        else:
            res_data = pd.DataFrame(self.__get_feat(data))
            res_data.fillna(0, inplace=True)
            prob = np.mean([i.predict(res_data) for i in self.model], axis=0)[0]
            return {'prob': prob,'msg': 'success', 'status_code': 100}
