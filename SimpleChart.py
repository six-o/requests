import matplotlib.pyplot as plt

# x	必填，數據位置 ( x 軸 )。
# height	必填，長條圖高度 ( y 軸 )。
# width	寬度，預設 0.8，支援陣列資料。
# bottom	底部位置，預設 0，支援陣列資料。
# align	對齊方式，預設 center，可設定 edge。
# color	顏色，支援陣列資料 ( 除了十六進位色碼，也可填入顏色代碼，例如 r、g、b、m、c、y...等，參考：color 列表 )。
# edgecolor	邊框顏色，支援陣列資料 ( 除了十六進位色碼，也可填入顏色代碼，例如 r、g、b、m、c、y...等，參考：color 列表 )。
# linewidth	邊框寬度，預設 2，支援陣列資料。
# tick_label	座標軸文字，預設無文字，支援陣列資料。
# xerr, yerr	x、y 軸的誤差範圍，預設 0，支援陣列資料。
# ecolor	誤差線段顏色，預設黑色，支援陣列資料。
# capsize	誤差範圍的上下線條尺寸，預設 0。
# fill	是否填滿，預設 True。

# Plots 1
x = [1, 2, 3, 4, 5]  # 水平資料點
h = [10, 20, 30, 40, 50]  # 高度
plt.bar(x, h)
plt.show()

# Plots 2
x = [1, 2, 3, 4, 5]
h = [10, 20, 30, 40, 50]
color = ['r', 'b', 'g', 'y', 'm']  # 顏色數據
label = ['a', 'b', 'c', 'd', 'e']  # 標籤數據
plt.bar(x, h, color=color, tick_label=label, width=0.5)  # 加入顏色、標籤和寬度參數
plt.show()

# Plots 3
x = [1, 2, 3, 4, 5]
h = [10, 20, 30, 40, 50]
color = ['r', 'b', 'g', 'y', 'm']
label = ['a', 'b', 'c', 'd', 'e']
plt.barh(x, h, color=color, tick_label=label, height=0.5)  # 改成 barh
plt.show()

# Plots 4
x = [1, 2, 3, 4, 5]
x2 = [0.8, 1.8, 2.8, 3.8, 4.8]  # 因為長條圖寬度 0.4，所以位移距離為除以 2 為 0.2
h = [10, 20, 30, 40, 50]  # 第一組數據高度
h2 = [20, 10, 40, 50, 30]  # 第二組數據高度
plt.bar(x, h, color='b', width=0.4, align='edge')  # 第一組數據靠左邊緣對齊
plt.bar(x2, h2, color='r', width=0.4)  # 第二組數據置中對齊
plt.show()

# Plots 5
x = [1, 2, 3, 4, 5]
x2 = [0.8, 1.8, 2.8, 3.8, 4.8]
h = [10, 20, 30, 40, 50]
h2 = [20, 10, 40, 50, 30]
plt.barh(x, h, color='b', height=0.4, align='edge')  # 改成 barh
plt.barh(x2, h2, color='r', height=0.4)  # 改成 barh
plt.show()
