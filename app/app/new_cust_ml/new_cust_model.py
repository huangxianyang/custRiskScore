# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 5:35 下午
# @Author  : HuangSir
# @FileName: new_cust_model.py
# @Software: PyCharm
# @Desc: 新客模型

import sys
sys.path.append('..')
import joblib
import pandas as pd
import numpy as np
from utils import load_txt_feature,prob2Score
from app.app.new_cust_ml.core import FeatMap

class NewCustModel:
    """新客模型"""
    def __init__(self):
        self.model_cv = joblib.load('app/app/new_cust_ml/static/newModel.pkl')
        self.feat = load_txt_feature('app/app/new_cust_ml/static/newFeat.txt')
        self.cat_feat = load_txt_feature('app/app/new_cust_ml/static/newCatFeat.txt')
        self.num_feat = list(set(self.feat) - set(self.cat_feat))

    def predict(self, data: dict):
        # 变量置换
        ml_data = {v:data[k] for k,v in FeatMap.items()}
        # 变量排序
        ml_data = {k: [ml_data[k]] for k in self.feat}
        # 入模参数构造
        ml_df = pd.DataFrame(ml_data)
        # 预测
        prob = np.nanmean([self.model_cv[i].predict(ml_df) for i in range(len(self.model_cv))])
        score = prob2Score(prob=prob, basePoint=600, PDO=50, odds=10)
        score = int(score)
        return score