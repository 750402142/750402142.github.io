

def get_brand(data,top):
    dp_brand = data.groupby('brands').size().sort_values(ascending=False).reset_index()
    dp_brand_top = dp_brand.values.tolist()[:top]
    return dp_brand_top

def get_drive_way(data):
    data1 = data.groupby(['year', '车辆级别']).size().reset_index(name='count')
    data1_unstacked = data1.set_index(['year', '车辆级别']).unstack(fill_value=0)['count'].T
    data1_filled = data1_unstacked.reset_index()
    data1_filled.columns.name = None
    year = data['year'].unique().tolist()
    year.sort()
    return data1_filled,year

def get_data3(data, data_score='label_price'):
    data1 = data.groupby(['year', data_score]).size().reset_index(name='count')
    data1_unstacked = data1.set_index(['year', data_score]).unstack(fill_value=0)['count'].T
    data1_filled = data1_unstacked.reset_index()
    data1_filled.columns.name = None
    return data1_filled
# 得到某一个属性前多少的列表
def get_one_top(data,data_score,top):
    data_pair = data.groupby([data_score]).size().reset_index(name='count').sort_values(by='count', ascending=False).head(top).values.tolist()
    return data_pair
def get_max(data_pair,year):
    max_y = 0
    for i in year:
        if max_y<data_pair[i].max():
            max_y = data_pair[i].max()
    return max_y

# 得到按某一列划分之后另一列变量数量前多少的数据统计
def get_single_by_single(data,single1,single2,top):
    dp = data.groupby(single1)[single2].count().sort_values(ascending=False).reset_index().values.tolist()[:top]
    return dp