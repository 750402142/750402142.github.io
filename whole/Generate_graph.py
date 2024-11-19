from matplotlib import pyplot as plt
from pyecharts.charts import Page
import seaborn as sns
import creat
import generated_data
import itemsyle_all
import pandas as pd
from app import read_html

data = pd.read_csv('./data/二手车上牌数据处理.csv')
data_list = ['车辆级别', '车身颜色','驱动方式','label_price','label1_行驶距离']
dp6=data.groupby(['year','brands'])['price'].mean().reset_index()
dp6=dp6.sort_values(by=['year', 'price'], ascending=[True, False]).values.tolist()
year = data['year'].unique().tolist()
year = sorted(year)
# 绘制出tab展示基本变量的时间条形图
# creat.draw_tab1(data,data_list,itemsyle_all.itemstyle_line).render('./result/tab展示各年变量的变化.html')
# print(generated_data.get_max(generated_data.get_data3(data,'车辆级别'),year))
# creat.draw_tab(year,data,itemsyle_all.itemstyle_line,data_list).render('./result/tab展示各年变量的变化.html')

# # 绘制品牌数量钱top饼图
# creat.draw_pie(data,itemsyle_all.pie_style,'brands',10,'车辆品牌前十的数量').render('./result/车辆品牌的前十饼图.html')
# # 绘制驱动方式前十数量的柱形图
# creat.draw_single_bar(data,itemsyle_all.bar_style,'车辆级别',10,'驱动方式前10柱形图').render('./result/驱动方式的前十柱形图.html')
#在售车辆的颜色统计
# creat.draw_pie(data,itemsyle_all.pie_style,'车身颜色',8,'车身颜色数量的统计').render('./result/车身颜色数量的统计.html')
#在售车辆的驱动方式数量统计
# creat.draw_single_bar(data,itemsyle_all.bar_style,'驱动方式',6,'车辆驱动方式的数量统计').render('./result/车辆驱动方式的数量统计.html')
# #绘制不同车辆颜色喜爱程度柱形图.html
dp = generated_data.get_single_by_single(data,'brands','车身颜色',10)
creat.draw_bar(dp,itemsyle_all.bar_style,'不同车辆颜色喜爱程度柱形图','brands','车身颜色').render('./result/不通车辆颜色喜爱程度柱形图.html')
# plot绘制

#x='行驶距离(万公里)',y='price',hue='车辆级别'
# creat.plot_vehicle_data(data).savefig('./result/x=行驶距离(万公里),y=price,hue=车辆级别.png')
# # x=year,y=行驶距离(万公里),hue=车辆级别
# creat.plot_vehicle_data(data, x='year',y='行驶距离(万公里)',hue='车辆级别').savefig('./result/x=year,y=行驶距离(万公里),hue=车辆级别.png')
# creat.plot_vehicle_data(data, x='驱动方式', y='price',hue='车辆级别').savefig('./result/x=x=驱动方式, y=price,hue=车辆级别.png')

# 生成车辆的基本信息情况
# page1 = Page(layout=Page.SimplePageLayout)
# page1.add(
# creat.draw_pie(data,itemsyle_all.pie_style,'brands',10,'车辆品牌前10的分布'),
#     creat.draw_single_bar(data,itemsyle_all.bar_style,'车辆级别',10,'车辆级别前10的分布'),
#
# )
# page1.render("combined_charts1.html")
# page2 = Page(layout=Page.SimplePageLayout)
# page2.add(
#
# creat.draw_pie(data,itemsyle_all.pie_style,'车身颜色',8,'车身颜色的数量统计'),
# creat.draw_single_bar(data,itemsyle_all.bar_style,'驱动方式',6,'车辆驱动方式的数量统计')
# )
# page2.render("combined_charts2.html")

# creat.draw_line(dp6,year,itemsyle_all.itemstyle_line).render('./result/每一年各品牌的平均价格.html')
# data_pair_color = data.groupby('brands')['车身颜色'].count().sort_values(ascending=False).reset_index().values.tolist()[:10]
# page1 = Page()
# page1.add(
#     creat.draw_bar(data_pair_color,itemsyle_all.bar_style),
#     creat.draw_bar1(data,itemsyle_all.itemstyle_bar,itemsyle_all.itemstyle1_bar1)
# )
# page1.render('./result/page1.html')


# creat.draw_pie(data,itemsyle_all.pie_style,'label_price',10,'各价格区间的车辆').render('./result/各价格区间的车辆.html')
# creat.get_data6(data,year).render('./result/上牌时间间隔.html')

