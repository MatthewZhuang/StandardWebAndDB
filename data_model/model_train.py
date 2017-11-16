#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @description:
        
 @Time       : 17/11/16 下午11:52
 @Author     : guomianzhuang
"""
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


def single_factor(x, y):
    """
        For single factor model, do a data transformation or not.
        Transformed data can not give a intuitive understanding.


    :return:    confidence interval for prediction.
    """
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    print results.summary()
    print dir(results)
    conf = 0.2
    prstd, iv_l, iv_u = wls_prediction_std(exog=[1, 3.1], res=results, alpha=conf)
    # v = model.predict(9.8)
    # prstd, iv_l, iv_u = wls_prediction_std(v)
    print "predict std %.3f, value_lower %3.f, " \
          "value_upper %.3f, confidence %.3f" % (prstd, iv_l, iv_u, conf)


def regression(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    print results.summary()
    # print dir(results)
    print "params ", results.params
    print "pvalues ", results.pvalues
    conf = 0.2
    prstd, iv_l, iv_u = wls_prediction_std(exog=[1, 3.1, 3.2, 3.3], res=results, alpha=conf)
    # v = model.predict(9.8)
    # prstd, iv_l, iv_u = wls_prediction_std(v)
    print "predict std %.3f, value_lower %3.f, " \
          "value_upper %.3f, confidence %.3f" % (prstd, iv_l, iv_u, conf)


def random_forest():
    pass


if __name__ == '__main__':
    # singlefactor
    # x = [1.2, 2, 3]
    # y = [3, 4, 5]
    # single_factor(x, y)

    # regression
    # x = [[1, 2, 3, 4],
    #      [1, 3.5, 4.6, 6.7],
    #      [1, 2.7, 3, 4],
    #      [1, 3.0, 4.6, 6.7],
    #      [1, 2.9, 3, 4],
    #      [1, 3.3, 4.6, 6.7],
    #      [1, 2.2, 3, 4],
    #      [1, 3.9, 4.6, 6.7],
    #      [1, 2.1, 3, 4],
    #      [1, 3.3, 4.6, 6.7],
    #      [1, 2.3, 3.5, 4.6]]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # regression(x, y)

    # random forest
    random_forest()
