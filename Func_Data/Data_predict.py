#中国科学院院士袁亚湘：一里路一里路把地面划分成几十亿个格子，每个点处的上方将大气划分成10-20层；最终有几百亿个点，每个点有不同的数据特征等；
import os
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


import datetime
from Dao import oper_database
import pandas as pd
import numpy as np
from Func_Data import Data_quary
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras

class Data_Predict():
    #获取数据：最高温、最低温、湿度
    #-1：数据库连接错误
    #list：数据列表
    def __init__(self,city):
        self.epochs = 1000
        self.N = 7
        self.list=[]
        self.city = city
    def GetData(self):
        print("开始获取数据集")
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            self.list = []
            # datelist = dc.getDatesByTimes('2019-01-01', today)
            data = dc.QuaryWeaDataSE(self.city,'2019-01-01', today)
            if data != -1:
                for index,value in data.items():
                    list_one = []

                    list_one.append(value[0])
                    list_one.append(value[1])
                    list_one.append(value[2])
                    # print(list_one)
                    self.list.append(list_one)

            dc.closeDB()
        else:
            return -1

    #预测最高温
    #数据库错误：return 100
    def Predict_max(self):
        print('开始预测最高温度')
        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][0])
                X.append(s)
                Y.append(list[i][0])
            X_a = np.array(X)
            Y_a = np.array(Y)
            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][0])
            X_ = [X_]
            # 数据均值化； Python中归一化特征到一定区间的函数；
            # 函数原型：sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)
            # .fit(self, X[, y])：计算给定数据集X的最大/小值用于之后的放缩（这一步没有进行放缩）
            # .transform(self, X)：将数据集X放缩至给定区间
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X_a)
            x = min_max_scaler.transform(X_a)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y_a
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性

            # 整流线性单元（ReLU）激活函数也被内置在 TensorFlow 库中。
            # 这个激活函数类似于线性激活函数，但有一个大的改变：对于负的输入值，神经元不会激活（输出为零），对于正的输入值，神经元的输出与输入值相同
            # 使用 ReLU 的主要优点之一是导致稀疏激活。在任何时刻，所有神经元的负的输入值都不会激活神经元。就计算量来说，这使得网络在计算方面更轻便。
            # 一般来说，隐藏层最好使用 ReLU 神经元。

            # ReLu激活函数的优点是：
            #  使用梯度下降（GD）法时，收敛速度更快
            # 相比Relu只需要一个门限值，即可以得到激活值，计算速度更快
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            # Adam优化器
            # Adam优化器，结合AdaGrad和RMSProp两种优化算法的优点。
            # 对梯度的一阶矩估计（First Moment Estimation，即梯度的均值）和二阶矩估计（SecondMoment Estimation，即梯度的未中心化的方差）进行综合考虑，计算出更新步长。
            # 主要包含以下几个显著的优点：
            # 实现简单，计算高效，对内存需求少
            # 参数的更新不受梯度的伸缩变换影响
            # 超参数具有很好的解释性，且通常无需调整或仅需很少的微调
            # 更新的步长能够被限制在大致的范围内（初始学习率）
            # 能自然地实现步长退火过程（自动调整学习率）
            # 很适合应用于大规模的数据及参数的场景
            # 适用于不稳定目标函数
            # 适用于梯度稀疏或梯度存在很大噪声的问题
            # 综合Adam在很多情况下算作默认工作性能比较优秀的优化器。
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs) # 开始训练模型 # 训练1000批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测:对今天的预测
            y_ = model.predict(x_)
            return y_

    #预测最低温
    #数据库错误：return 100
    def Predict_min(self):
        print('开始预测最低温度')
        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][1])
                X.append(s)
                Y.append(list[i][1])
            X = np.array(X)
            Y = np.array(Y)

            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][1])
            X_ = [X_]
            # print(X_)

            # 数据均值化
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X)
            x = min_max_scaler.transform(X)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            # 开始训练模型
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs)  # 训练1000个批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测
            y_ = model.predict(x_)
            return y_

    #预测最湿度
    #数据库错误：return 100
    def Predict_hum(self):
        print('开始预测平均湿度')
        list=self.list
        if list == -1:
            return 100
        else:
            N = self.N
            X = []
            Y = []
            X_= []
            for i in range(N, len(list)-1):
                s = []
                for j in range(i - N, i):
                    s.append(list[j][2])
                X.append(s)
                Y.append(list[i][2])
            X = np.array(X)
            Y = np.array(Y)

            for j in range(len(list)-N-1,len(list)-1):
                X_.append(list[j][2])
            X_ = [X_]
            # print(X_)

            # 数据均值化
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(X)
            x = min_max_scaler.transform(X)  # 均值化处理
            #预测所需最近七天数值
            x_ = min_max_scaler.transform(X_)  # 这里随便取一组数据，作为后面预测用，注意数据维度
            y = Y
            # 划分数据集,按训练集:测试集=8:2比例划分
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
            # 模型结构，采用relu函数为激活函数，输入层为N个属性
            # 下面为4层隐含层，每层的神经元个数依次为500，500，250，250
            # 输入层对应N个属性
            model = keras.Sequential([
                keras.layers.Dense(500, activation='relu', input_shape=[N]),
                keras.layers.Dense(500, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(250, activation='relu'),
                keras.layers.Dense(1)])  # 最后输出为一个结果，也就是预测的值
            # 定义损失函数loss，采用的优化器optimizer为Adam
            model.compile(loss='mean_absolute_error', optimizer='Adam')
            # 开始训练模型
            model.fit(x_train, y_train, batch_size=128, epochs=self.epochs)  # 训练1000个批次，每个批次数据量为126   梯度下降 126个样本作为一批次
            # 输出结果预测
            y_ = model.predict(x_)
            return y_

    def Predict_tommorw(self):
        today_max=self.Predict_max()
        today_min=self.Predict_min()
        today_hum=self.Predict_hum()
        s=[today_max,today_min,today_hum]
        self.list.append(s)
        tom_max = self.Predict_max()
        tom_min = self.Predict_min()
        tom_hum = self.Predict_hum()
        tma = round(np.double(tom_max), 2)
        tmi = round(np.double(tom_min), 2)
        thu = round(np.double(tom_hum), 2)

        return [tma,tmi,thu]
