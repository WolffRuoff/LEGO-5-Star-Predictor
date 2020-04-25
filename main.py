import matplotlib.pyplot as plt
import pandas
import os

class mains():
    # %% codecell
    set1 = os.path.join('.', 'data', 'Set1')
    colors=pandas.read_csv(os.path.join(set1,'colors.csv'))
    #colors.head()
    inventories=pandas.read_csv(os.path.join(set1,'inventories.csv'))
    #inventories.head()
    #inventory_sets=pandas.read_csv(os.path.join(set1,'inventory_sets.csv'))
    #inventory_sets.head()
    inventory_parts=pandas.read_csv(os.path.join(set1,'inventory_parts.csv'))
    #inventory_parts.head()
    sets=pandas.read_csv(os.path.join(set1,'sets.csv'))
    sets.head()
    themes=pandas.read_csv(os.path.join(set1,'themes.csv'))
    #themes.head()
    set2 = os.path.join('.', 'data', 'Set2')
    lego_sets=pandas.read_csv(os.path.join(set2,'lego_sets.csv'))
    #lego_sets.head()

    # %% codecell
    data = pandas.merge(sets, inventories[['inventory_id','set_num']], on = 'set_num', how='left')
    data = pandas.merge(data, inventory_parts[['inventory_id', 'color_id']], on = 'inventory_id', how='right')
    data = pandas.merge(data, colors[['color_id','color_name', 'rgb']], on = 'color_id')
    data = pandas.merge(data, themes[['theme_id', 'theme_name']], on = 'theme_id')
    len(data['set_name'])
    data = pandas.merge(lego_sets, data[['set_name', 'inventory_id', 'num_parts','theme_id', 'color_id', 'color_name', 'rgb']], on = 'set_name', how='left')
    data.drop(['prod_desc', 'prod_long_desc', 'country'], axis=1)
    len(data['set_name'])
    data.head()
