from datetime import datetime

import matplotlib
import requests
import matplotlib.pyplot as plt
import pandas as pd  # Add this line

matplotlib.rc('font', family='Microsoft JhengHei')


url = 'https://data.epa.gov.tw/api/v2'
dataset = "AQX_P_434"  # 請替換欲下載資料集代碼,如何查詢資料集代碼詳簡報第8頁
Format = "json"  # 平臺提供格式包含JSON、 XML、 CSV，請依欲下載資料格式自行更換。
offset = 0  # 為遞移起始下載筆數使用，請輸入欲跳過的筆數，若欲擷取第1001筆後之資料，數字請輸入 1000
# 將項目數量放入變數 limit
limit = 2000  # 請輸入欲取得資料的筆數，考量系統效能，資料擷取上限為 1000 筆,若未設定，預設值為 1000
api_key = "b03125d5-9a0d-4d4a-a88d-44085566fb4a"  # 加入會員後可取得 api_key，請自行更換。
API_URL = f'{url}/{dataset}?format={Format}&offset={offset}&limit={limit}&api_key={api_key}'

data = requests.get(API_URL)  # 使用 get 方法透過空氣品質指標 API 取得內容
data_json = data.json()  # 將取得的檔案轉換為 JSON 格式

data_list = ['siteid', 'sitename', 'monitordate', 'aqi']
now = datetime.now().strftime("%Y-%m-%d")
for day in range(31, 0, -1):
    if day < 10:
        day = f"0{day}"
    time = f"2024-05-{day}"
    for i in data_json['records']:
        if i['monitordate'] == time:
            for j in data_list:
                print(f'{i[j]:>3}', end='\t')
            print('\n')

# data_list = ['siteid', 'sitename', 'monitordate', 'aqi', 'so2subindex', 'cosubindex', 'o3subindex',
#              'pm10subindex', 'no2subindex', 'o38subindex', 'pm25subindex']
#
# for i in data_json['records']:
#     for j in i:
#         print(f"{i[j]:>3}", end='\t')
#     print('\n')

# Create a DataFrame from the JSON data
# df = pd.DataFrame(data_json['records'])  # Add this line

# 將 'monitordate' 列轉換為 datetime 對象，並設置為索引
# df['monitordate'] = pd.to_datetime(df['monitordate'])
# df = df.set_index('monitordate')

# 指標列表
indicators = ['aqi', 'so2subindex', 'cosubindex', 'o3subindex', 'pm10subindex', 'no2subindex', 'o38subindex', 'pm25subindex']

# Convert all indicator columns to numeric
# for indicator in indicators:
#     df[indicator] = pd.to_numeric(df[indicator], errors='coerce')


# 选择要绘制的站点
# site = '左營'  # 请将 'YourSiteName' 替换为您要绘制的站点的名称

# 筛选出该站点的数据
# df_site = df[df['sitename'] == site]
#
# # 绘制AQI随时间变化的图表
# df_site['aqi'].plot(kind='line')
# plt.title(f'AQI over time at {site}')
# plt.xlabel('Date')
# plt.ylabel('AQI')
# plt.show()

# # Now you can plot
# for indicator in indicators:
#     df[indicator].plot(kind='line')
#     plt.title(f'{indicator} over time')
#     plt.xlabel('Date')
#     plt.ylabel(indicator)
#     plt.show()
#
# # 繪製盒鬚圖
# for indicator in indicators:
#     df.boxplot(column=indicator)
#     plt.title(f'Boxplot of {indicator}')
#     plt.ylabel(indicator)
#     plt.show()

# # 繪製直方圖
# for indicator in indicators:
#     df[indicator].hist(bins=30)
#     plt.title(f'Histogram of {indicator}')
#     plt.xlabel(indicator)
#     plt.ylabel('Frequency')
#     plt.show()
