import pandas as pd
from dtw import *
import tushare as ts
from sklearn import preprocessing
import numpy as np
from matplotlib import pyplot as plt
import datetime


class StockCount():

    mean_start_time = "20140101"  # 求均值时间
    mean_end_time = "20140331"

    def __init__(self, code):
        """
        :var stock_code: 股票代码
        :var stock_data: 计算后的股票数据，包括["trade_date", "close","log_close","yield_rate"]
        """
        self.stock_code = code
        self.stock_data = StockCount.get_stock_data(code)
        self.mens_lnS = None  # 计算均值
        self.data = None
        self.preprocessing_data()  # 数据预处理

    def preprocessing_data(self):
        data = self.stock_data[["trade_date", "close"]].iloc[::-1]  # 倒序
        data["log_close"] = np.log(data['close'])
        self.mens_lnS = StockCount.cout_mean(data)  # 计算均值
        data["yield_rate"] = np.exp(data["log_close"] - self.mens_lnS)  # 计算收益率
        self.data = data

    @staticmethod
    def cout_mean(data):
        """
        计算2014年1月1日到2014年3月31日时间段内所有收盘对数价格平均数 mean_lnS
        :param data:
        :return:
        """
        sum = 0
        counter = 0
        for i in range(0, data.shape[0]):  # 遍历整个 pandas
            now_date = data["trade_date"].iloc[i]
            if (StockCount.compare_time(now_date, StockCount.mean_start_time) >= 0 and
                    StockCount.compare_time(StockCount.mean_end_time, now_date) >= 0):
                sum += data["log_close"].iloc[i]
                counter += 1
            if (StockCount.compare_time(now_date, StockCount.mean_start_time) < 0):
                break
        return sum / counter

    @staticmethod
    def get_stock_data(code="", start="20140101", end="20191209"):
        """
            获取股票交易数据，按日期顺序增排列
            :return: pandas
            """
        token = "264f9e8a490cc3f2fa69cd654442ba812b45dd5680e706ce6988d818"
        ts.set_token(token)
        data = ts.pro_bar(ts_code=code, adj='qfq', start_date=start, end_date=end)
        return data

    @staticmethod
    def compare_time(time1, time2):
        d1 = datetime.datetime.strptime(time1, '%Y%m%d')
        d2 = datetime.datetime.strptime(time2, '%Y%m%d')
        delta = d1 - d2
        return delta.days

if __name__ == '__main__':
    stock_of_template = StockCount(code="600519.SH")

    print(stock_of_template.data)


    # stock_1 = get_stock_data("601168.SH")
    # data_stock_1 = preprocessing_data(stock_1)
    # query = data_stock_1["log_close"]
    #
    # stock_2 = get_stock_data("601991.SH")
    # data_stock_2 = preprocessing_data(stock_2)
    # template = data_stock_2["log_close"]
    #
    # print(data_stock_1.head(), data_stock_2.head())
    # plt.plot(data_stock_1["trade_date"], data_stock_1["log_close"])
    # plt.show()
    #
    # alignment = dtw(query, template, keep_internals=True,step_pattern=asymmetric)
    # # print( countPaths(alignment) )
    # print(alignment.distance)
    #
    # ## Display the warping curve, i.e. the alignment curve
    # alignment.plot(type="threeway")
    #
    # ## Align and plot with the Rabiner-Juang type VI-c unsmoothed recursion
    # dtw(query, template, keep_internals=True,
    #     step_pattern=rabinerJuangStepPattern(6, "c")) \
    #     .plot(type="twoway", offset=-2)
    #
    # ## See the recursion relation, as formula and diagram
    # print(rabinerJuangStepPattern(6, "c"))
    # rabinerJuangStepPattern(6, "c").plot()