import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 假設我們有一個CSV文件包含空氣質量數據
data = pd.read_csv('air_quality_data.csv')

# 描述性統計分析
desc_stats = data.describe()
print(desc_stats)

# 保存描述性統計分析結果到CSV文件
desc_stats.to_csv('descriptive_statistics.csv', index=True)

# 處理缺失值
data = data.dropna()

# 繪製時間序列圖並保存為圖像文件
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['PM2.5'], label='PM2.5')
plt.xlabel('Date')
plt.ylabel('PM2.5 Concentration')
plt.title('PM2.5 Concentration Over Time')
plt.legend()
plt.savefig('pm25_time_series.png')
plt.show()

# 相關分析
correlation_matrix = data[['PM2.5', 'temperature', 'humidity']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()
