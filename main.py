import matplotlib.pyplot as plt
import pandas
import os

class mains():
    # %% <codecell> Import All CSVs
    set1 = os.path.join('.', 'data', 'Set1')
    colors=pandas.read_csv(os.path.join(set1,'colors.csv'))
    inventories=pandas.read_csv(os.path.join(set1,'inventories.csv'))
    inventory_sets=pandas.read_csv(os.path.join(set1,'inventory_sets.csv'))
    inventory_parts=pandas.read_csv(os.path.join(set1,'inventory_parts.csv'))
    sets=pandas.read_csv(os.path.join(set1,'sets.csv'))
    themes=pandas.read_csv(os.path.join(set1,'themes.csv'))
    set2 = os.path.join('.', 'data', 'Set2')
    lego_sets=pandas.read_csv(os.path.join(set2,'lego_sets.csv'))
    
