import pandas as pd
import lxml
import openpyxl
from IPython.display import display
import matplotlib.pyplot as plt
def drowpilot(year,month,obs,T,Tmax,Tmin):

    fig,ax1=plt.subplots(figsize=(8,6))
    ax1.plot(obs,Tmax,color='#BB3D00',label="最高氣溫")
    ax1.plot(obs,T,color='#FF5809',label="氣溫")
    ax1.plot(obs,Tmin,color='#FF9D6F',label="最低氣溫")
    plt.grid(1)
    ax1.legend(bbox_to_anchor=(1, 1))
    plt.title(year+'年'+month+'月氣溫變化')
    ax1.set_xlabel('時間(日)')
    ax1.set_ylabel('氣溫(℃)')
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.show()