import pandas as pd
from matplotlib import pyplot as plt
from pyecharts.charts import Pie, Timeline, Line, Bar,Tab

import pyecharts.options as opts
from pyecharts.globals import ThemeType
import seaborn as sns
import generated_data

#绘制某一个属性前多少的饼图
def draw_pie(data,itemstyle_pie,data_score,top,title,radius=['30%', '80%'],rosetype='area',):
    data_pair  = generated_data.get_one_top(data,data_score,top)
    pie = (Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
           .add(series_name=title, data_pair=data_pair,
                radius=radius,  # 饼图内半径和外半径
                rosetype=rosetype,  # 否展示成南丁格尔图
                label_opts=opts.LabelOpts(formatter='{b}:{c}\n百分占比{d}%'),  # 标签配置
                itemstyle_opts=itemstyle_pie,  # 图元样式配置
                emphasis_opts=opts.EmphasisOpts(is_show_label_line=True, focus='series',
                                                label_opts=opts.LabelOpts(font_size=20, font_weight='bold')
                                                ),  # 高亮多边形配置
                )
           #     .set_colors()
           .set_global_opts(tooltip_opts=opts.TooltipOpts(trigger='item'),
                            title_opts=opts.TitleOpts(title = title,pos_left='center'),
                            legend_opts=opts.LegendOpts(pos_top='5%',
                                                        textstyle_opts=opts.TextStyleOpts(color='auto'),  # 文字样式
                                                        ),
                            )
           )
    return pie

# 绘制某一个属性前多少的柱形图
def draw_single_bar(data,itemstyle_bar,data_score,top,title):
    data_pair = generated_data.get_one_top(data,data_score,top)
    bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([i[0] for i in data_pair])
    .add_yaxis(series_name=f'TOP{top}{data_score}', y_axis=[i[1] for i in data_pair],
               label_opts=opts.LabelOpts(position='top', formatter='{c}所',
                                         color='white', font_weight='bold'),
               itemstyle_opts=itemstyle_bar,
               category_gap='30',  ## 同一序列柱间的距离
               )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=title, pos_left='center'),
        legend_opts=opts.LegendOpts(pos_top='5%',
                                    textstyle_opts=opts.TextStyleOpts(color='auto'),  # 文字样式
                                    ),
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='shadow',
                                      ),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(font_weight='bold', color='white',  ##粗体白色
                                          ),
        )
    )
    )
    return bar

# 绘制用tab来展示多个属性随年份变化的折线图
def draw_tab(year,data,line_itemstyle1,data_list):
    tab = Tab()
    for i in data_list:
        data_filled = generated_data.get_data3(data,i)
        level_list = data[i].unique().tolist()
        t1 = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK, bg_color='#000000'))
        for index, j in enumerate(year):
            line = (Line()
            .add_xaxis(level_list)
            .add_yaxis(f'{j}车辆{i}近年来变化', data_filled[j].tolist(), is_symbol_show=False, is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       markline_opts=opts.MarkLineOpts(data=[
                           opts.MarkLineItem(type_='average', name='均值线', ),
                           opts.MarkLineItem(type_='max', name='最大值线', ),
                           opts.MarkLineItem(type_='min', name='最小值线', ),
                       ],),
                       markpoint_opts=opts.MarkPointOpts(data=[
                           opts.MarkPointItem(type_='average', name='均值点', ),
                           opts.MarkPointItem(type_='max', name='最大值点', ),
                           opts.MarkPointItem(type_='min', name='最小值点', ),
                       ]), itemstyle_opts=line_itemstyle1)
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False), ),
                yaxis_opts=opts.AxisOpts(
                    max_ = 100,  # 设置y轴最大值
                    splitline_opts=opts.SplitLineOpts(is_show=False)  # 去掉y轴网格线
                )
            )
            )
            t1.add(line, i)
        t1.add_schema(play_interval=400)
        tab.add(t1,i)
    return tab

# 绘制单变量柱形图
def draw_bar(data_pair,bar_style,title,single1,single2):
    bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([i[0] for i in data_pair])
    .add_yaxis(single2, [i[1] for i in data_pair],
               itemstyle_opts=bar_style,
               label_opts=opts.LabelOpts(position='top', font_weight='bold', color='aotu',
                                         formatter="{c}辆",
                                         )
               )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=title, pos_left='center'),
        legend_opts=opts.LegendOpts(pos_top='5%'),
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='shadow'),
        xaxis_opts=opts.AxisOpts(name=single1, name_location='center', name_gap=40,
                                 name_textstyle_opts=opts.TextStyleOpts(font_weight='bold', color='orange'),
                                 axisline_opts={'show': True, "lineStyle": {'color': 'orange', "width": 2}},
                                 axistick_opts={'show': False},
                                 axislabel_opts={'color': 'orange'},
                                 splitline_opts={'show': False}
                                 ),
        yaxis_opts=opts.AxisOpts(name=single2, name_location='center', name_gap=50,
                                 name_textstyle_opts=opts.TextStyleOpts(font_weight='bold', color='orange'),
                                 axisline_opts={'show': True, "lineStyle": {'color': 'cyan', "width": 2}},
                                 axistick_opts={'show': False},
                                 axislabel_opts={'color': 'orange'},
                                 splitline_opts={'show': False}
                                 )

    )
    )
    return bar

#用plot绘制
def plot_vehicle_data(data, x='行驶距离(万公里)',
        y='price',hue='车辆级别'):
    # 设置字体为微软雅黑，确保中文显示正常
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 设置正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    fig, axs = plt.subplots(1, 2, figsize=(15, 5), dpi=100, gridspec_kw=dict(width_ratios=[4, 2]))
    sns.scatterplot(
        data=data,
        x=x,
        y=y,
        hue=hue,
        ax=axs[0]
    )
    axs[0].set_title(f'{x}与{y}的关系')
    sns.histplot(
        data=data,
        x=x,
        hue=hue,
        shrink=0.5,
        ax=axs[1]
    )
    axs[1].set_title(f'不同{hue}的行驶距离分布')
    plt.tight_layout()  # 调整子图之间的间距
    return plt


def get_data4(data, itemstyle_line,max_y,data_score='label_price'):
    data_pair = generated_data.get_data3(data, data_score)
    level_list = [str(i) for i in data[data_score].unique()]
    level_list = sorted(level_list)
    year = data['year'].unique().tolist()
    year = sorted(year)
    t1 = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK, bg_color='#000000'))
    for index, i in enumerate(year):
        line = (Line()
        .add_xaxis(level_list)
        .add_yaxis(f"{i}年{data_score}数量变化", data_pair[i].tolist(), is_symbol_show=False, is_smooth=True,
                   label_opts=opts.LabelOpts(is_show=False),
                   markline_opts=opts.MarkLineOpts(data=[
                       opts.MarkLineItem(type_='average', name='均值线', ),
                       opts.MarkLineItem(type_='max', name='最大值线', ),
                       opts.MarkLineItem(type_='min', name='最小值线', ),
                   ], ),
                   markpoint_opts=opts.MarkPointOpts(data=[
                       opts.MarkPointItem(type_='average', name='均值点', ),
                       opts.MarkPointItem(type_='max', name='最大值点', ),
                       opts.MarkPointItem(type_='min', name='最小值点', ),
                   ]), itemstyle_opts=itemstyle_line)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False), ),
            yaxis_opts=opts.AxisOpts(
                max_=max_y,  # 设置y轴最大值
                splitline_opts=opts.SplitLineOpts(is_show=False)  # 去掉y轴网格线
            )
        )
        )

        t1.add(line, i)
    t1.add_schema(play_interval=400)
    return t1
#绘制tab图形
def draw_tab1(data,data_list,itemstyle_line):
    tab = Tab()
    for i in data_list:
        max_y = generated_data.get_max(generated_data.get_data3(data, i), data['year'].unique().tolist())
        item = get_data4(data,itemstyle_line,max_y,i,)
        tab.add(item, i)
    return tab
def draw_line(data_pair,year,line_itemstyle1):
    tab = Tab()
    for index, i in enumerate(year):
        line = (Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis([j[1] for j in data_pair if j[0] == i])
        .add_yaxis(f"{i}年近年喜爱数量变化", [j[2] for j in data_pair if j[0] == i],
                   is_symbol_show=False, is_smooth=True,
                   label_opts=opts.LabelOpts(is_show=False),
                   markline_opts=opts.MarkLineOpts(data=[
                       opts.MarkLineItem(type_='average', name='均值线', ),
                       opts.MarkLineItem(type_='max', name='最大值线', ),
                       opts.MarkLineItem(type_='min', name='最小值线', ),
                   ], ),
                   markpoint_opts=opts.MarkPointOpts(data=[
                       opts.MarkPointItem(type_='average', name='均值点', ),
                       opts.MarkPointItem(type_='max', name='最大值点', ),
                       opts.MarkPointItem(type_='min', name='最小值点', ),
                   ]),
                   itemstyle_opts=line_itemstyle1)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False), ),
            yaxis_opts=opts.AxisOpts(
                max_=max([j[2] for j in data_pair if j[0] == i]),  # 设置y轴最大值
                splitline_opts=opts.SplitLineOpts(is_show=False),  # 去掉y轴网格线

            ),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        )

        tab.add(line, i)
    return tab

#绘制用tab展示每一年上牌时间间隔
def get_data6(data, year,data_score='上牌时间间隔',):
    data['上牌时间'] = pd.to_datetime(data['上牌时间'])
    tab = Tab()
    for i in year:
        def calculate_time_interval(row):
            if row['上牌时间'].year > i:
                return '未上牌'
            else:
                return str(i - row['上牌时间'].year)

        data['上牌时间间隔'] = data.apply(calculate_time_interval, axis=1)
        df = data.groupby('上牌时间间隔').size().reset_index(name='count').values.tolist()
        pie = (Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add(series_name='上牌时间间隔', data_pair=df,
             radius=['20%', '40%'], center=['50%', '50%'], rosetype='area',
             label_opts=opts.LabelOpts(formatter='{b},{c}\n百分占比{d}%'), )  # 标签配置)
        .set_global_opts(title_opts=[
            dict(text='上牌时间间隔', top=0, left='center'),

        ], legend_opts=opts.LegendOpts(pos_top='7%'))

        )

        tab.add(pie, str(i))
    return tab

def draw_bar1(data,itemstyle,itemstyle1):
    dp3 = data.groupby('车辆级别')['行驶距离(万公里)'].sum().reset_index()
    dp4 = data.groupby('车辆级别')['price'].mean().reset_index()
    dp4['price'] = dp4['price'].round(2)
    dp5 = pd.merge(dp3, dp4, on='车辆级别').values.tolist()

    bar = (Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, bg_color='#080b30'))
           .add_xaxis([i[0] for i in dp5])
           .add_yaxis('行驶距离（万公里）', [i[1] for i in dp5], yaxis_index=0,
                      itemstyle_opts=itemstyle, )
           .add_yaxis('平均价格', [i[2] for i in dp5], yaxis_index=1,
                      itemstyle_opts=itemstyle1)
           .extend_axis(
        yaxis=opts.AxisOpts(
            name='平均价格', interval=10, ))
           .set_global_opts(
        title_opts=opts.TitleOpts(title='不同车辆级别基本情况对比', pos_left='center'),
        xaxis_opts=opts.AxisOpts(splitline_opts={'show': False}),
        yaxis_opts=opts.AxisOpts(name='行驶距离（万公里）', splitline_opts={'show': False}),
        legend_opts=opts.LegendOpts(pos_top='7%'),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="shadow"),
    )
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           )
    return bar