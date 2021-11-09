# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 5:08 下午
# @Author  : HuangSir
# @FileName: ml_utils.py
# @Software: PyCharm
# @Desc:

import numpy as np
import pandas as pd
import re
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import warnings

def prob2Score(prob,basePoint=550,PDO=100,odds=30):
    # 将概率转化成分数且为正整数
    y = np.log(prob/(1-prob))
    a = basePoint - y * np.log(odds)
    y2 = a - PDO/np.log(2)*(y)
    score = y2.astype('int')
    return score


def points_ply(dtx, binx, x_i, woe_points):
    binx = pd.merge(
        binx[['bin']].assign(v1=binx['bin'].str.split('%,%')).explode('v1'),
        binx[['bin', woe_points]],
        how='left', on='bin'
    ).rename(columns={'v1': 'V1', woe_points: 'V2'})

    # dtx
    ## cut numeric variable
    if is_numeric_dtype(dtx[x_i]):
        is_sv = pd.Series(not bool(re.search(r'\[', str(i))) for i in binx.V1)
        binx_sv = binx.loc[is_sv]
        binx_other = binx.loc[~is_sv]
        # create bin column
        breaks_binx_other = np.unique(list(map(float, ['-inf'] + [re.match(r'.*\[(.*),.+\).*', str(i)).group(1) for i in
                                                                  binx_other['bin']] + ['inf'])))
        labels = ['[{},{})'.format(breaks_binx_other[i], breaks_binx_other[i + 1]) for i in
                  range(len(breaks_binx_other) - 1)]

        dtx = dtx.assign(xi_bin=lambda x: pd.cut(x[x_i], breaks_binx_other, right=False, labels=labels)) \
            .assign(xi_bin=lambda x: [i if (i != i) else str(i) for i in x['xi_bin']])
        mask = dtx[x_i].isin(binx_sv['V1'])
        dtx.loc[mask, 'xi_bin'] = dtx.loc[mask, x_i].astype(str)
        dtx = dtx[['xi_bin']].rename(columns={'xi_bin': x_i})
    ## to charcarter, na to missing
    if not is_string_dtype(dtx[x_i]):
        dtx.loc[:, x_i] = dtx.loc[:, x_i].astype(str).replace('nan', 'missing')
    dtx = dtx.replace(np.nan, 'missing').assign(rowid=dtx.index).sort_values('rowid')
    # rename binx
    binx.columns = ['bin', x_i, '_'.join([x_i, woe_points])]
    # merge
    dtx_suffix = pd.merge(dtx, binx, how='left', on=x_i).sort_values('rowid') \
        .set_index(dtx.index)[['_'.join([x_i, woe_points])]]
    return dtx_suffix


def scorecard_ply(dt, card, only_total_score=True,var_kp=None):
    dt = dt.copy(deep=True)
    card_df = card.copy(deep=True)
    xs = card_df.loc[card_df.variable != 'basepoints', 'variable'].unique()
    # length of x variables
    xs_len = len(xs)
    # initial datasets
    dat = dt.loc[:, list(set(dt.columns) - set(xs))]
    # loop on x variables
    for i in np.arange(xs_len):
        x_i = xs[i]
        cardx = card_df.loc[card_df['variable'] == x_i]
        dtx = dt[[x_i]]
        # score transformation
        dtx_points = points_ply(dtx, cardx, x_i, woe_points="points")
        dat = pd.concat([dat, dtx_points], axis=1)

    # set basepoints
    card_basepoints = list(card_df.loc[card_df['variable'] == 'basepoints', 'points'])[0] if 'basepoints' in card_df[
        'variable'].unique() else 0
    # total score
    dat_score = dat[xs + '_points']
    dat_score.loc[:, 'score'] = card_basepoints + dat_score.sum(axis=1)
    if only_total_score:
        dat_score = dat_score[['score']]
    if var_kp is not None:
        if isinstance(var_kp, str):
            var_kp = [var_kp]
        var_kp2 = list(set(var_kp) & set(list(dt)))
        len_diff_var_kp = len(var_kp) - len(var_kp2)
        if len_diff_var_kp > 0:
            warnings.warn(
                f"Incorrect inputs; there are {len_diff_var_kp} var_kp variables are not exist in input data "
                f"which are removed from var_kp. \n {list(set(var_kp) - set(var_kp2))}")
        var_kp = var_kp2 if len(var_kp2) > 0 else None
    if var_kp is not None:
        dat_score = pd.concat([dt[var_kp], dat_score], axis=1)
    return dat_score