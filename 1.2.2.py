'''
Discription  : 
Author       : henry loh
Email        : 993026894@qq.com
Github       : https://github.com/henry-loh
Date         : 2021-05-16 20:25:47
LastEditTime : 2021-05-16 21:36:37
FilePath     : \repo\practice\physicsical experiments\a2\1.2.2.py
'''
#%%
## import
#%%
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import random
import warnings
import plotly
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
#%%
## initialize
#%%
warnings.filterwarnings("ignore")
plt.style.use('ggplot') # 用来设置作图风格
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
%matplotlib inline
#%%
## read file
#%%
path1="C:/Users/henry_loh/Documents/GitHub/repo/practice/physicsical experiments/a2/1.2.1.txt"
path2="C:/Users/henry_loh/Documents/GitHub/repo/practice/physicsical experiments/a2/1.2.2.txt"
df1=pd.read_csv(sep='\t',filepath_or_buffer=path1,header=0)
df2=pd.read_csv(sep='\t',filepath_or_buffer=path2,header=0)
#%%
## fitting
#%%
m = np.linspace(0,3.5,3500)
parameter = np.polyfit(df2['砝码质量(g)'].values,df2['数字电压表读数(mV)'].values, 1)
uval = parameter[0] * m + parameter[1]
correlation = np.corrcoef(df2['数字电压表读数(mV)'].values, parameter[0] * df2['砝码质量(g)'].values + parameter[1])[0,1]
p = np.poly1d(parameter,variable='x')
print(correlation)
print('uval=',parameter[0],'m',parameter[1])
#%%
## plot 1.2.1
#%%
fig=go.Figure()
fig.add_trace(go.Scatter(
    x=df1['砝码质量(g)'],
    y=df1['数字电压表读数(mV)'],
    mode="lines+markers",
    name = '测量值',
    marker = dict(color='rgba(255,127,80,0.8)')
    )
)
fig.add_trace(go.Scatter(
    x=df2['砝码质量(g)'],
    y=df2['数字电压表读数(mV)'],
    mode="lines+markers",
    name = '平均值',
    marker = dict(color='rgba(0,0,139,0.8)')
    )
)
fig.add_trace(go.Scatter(
    x=m,
    y=uval,
    mode="lines",
    name = '线性拟合',
    line=dict(color='firebrick', width=2, dash='dot'),
    marker = dict(color='rgba(0,0,139,0.8)')
    )
)
fig.update_layout(title = dict(
        text = "(a) 力敏传感器的标定曲线",
        y = 0.02,
        x = 0.5,
        xanchor = 'center',
        yanchor = 'bottom'),
    legend = dict(
        
    ),
    xaxis = dict(
        title = dict(
                 text= "砝码质量(g)"
                 ),
        tickmode = 'linear',
        tick0 = 0,
        dtick = 0.5
        ),
    yaxis = dict(
        title=dict(
            text="数字电压表读数(mV)"
            ),
        tickmode = 'linear',
        tick0 = -3.6,
        dtick = 3.6
        ),
    annotations = [dict(
        text=f'拟合结果：<br>r=0.99919<br>K=5.2350',
        showarrow = False,
        x=0.2,
        y=16.5,
        bordercolor='rgba(0,0,0,0.8)',
        borderwidth=1,
        borderpad=4,
        bgcolor='rgba(255,255,255,1)'
    )]
)
#%%
fig.write_image("C:/Users/henry_loh/Documents/GitHub/repo/practice/physicsical experiments/a2/(a) 力敏传感器的标定曲线.pdf")
#%%
# end