import pandas as pd
import lxml
import openpyxl
from IPython.display import display
import matplotlib.pyplot as plt
import drow
# 提取天氣資料
year=str(2023)
month=str(10)
table = pd.read_html("https://e-service.cwa.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=467410&stname=%25E8%2587%25BA%25E5%258D%2597&datepicker="+year+"-"+month+"&altitude=40.8m", encoding='utf-8')
new=table[1]
ObsTime_data = new['Unnamed: 0_level_0']['觀測時間 (day)']
Temperature_data=new['temperature']['氣溫 (℃)']
TMax_data=new['temperature']['最高氣溫 (℃)']
TMin_data=new['temperature']['最低氣溫 (℃)']
Sunshine_data=new['SunShine']['日照時數 (hour)']
data=ObsTime_data.join(Temperature_data).join(TMax_data).join(TMin_data).join(Sunshine_data)
data.to_excel(year+'年'+month+'月'+'溫度資訊.xlsx')
drow.drowpilot(year,month,ObsTime_data,Temperature_data,TMax_data,TMin_data)