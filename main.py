import matplotlib.pyplot as plt
import pandas
import os
import numpy as np
import matplotlib as mpl

class mains():
    # %% codecell
    set1 = os.path.join('.', 'data', 'Set1')
    colors = pandas.read_csv(os.path.join(set1,'colors.csv'))
    #colors.head()
    inventories = pandas.read_csv(os.path.join(set1,'inventories.csv'))
    #inventories.head()
    #inventory_sets=pandas.read_csv(os.path.join(set1,'inventory_sets.csv'))
    #inventory_sets.head()
    inventory_parts = pandas.read_csv(os.path.join(set1,'inventory_parts.csv'))
    #inventory_parts.head()
    sets = pandas.read_csv(os.path.join(set1,'sets.csv'))
    #sets.head()
    themes = pandas.read_csv(os.path.join(set1,'themes.csv'))
    #themes.head()
    set2 = os.path.join('.', 'data', 'Set2')
    lego_sets = pandas.read_csv(os.path.join(set2,'lego_sets.csv'))
    #lego_sets.head()

    # %% codecell
    len(inventory_parts['inventory_id'])
    len(colors['color_id'])
    len(lego_sets['set_name'])
    data = pandas.merge(sets, inventories[['inventory_id', 'set_num']], on = 'set_num', how='left')
    data = pandas.merge(data, inventory_parts[['inventory_id', 'part_num', 'color_id']], on = 'inventory_id', how='right')
    data = pandas.merge(data, colors[['color_id','color_name', 'rgb']], on = 'color_id')
    data = pandas.merge(data, themes[['theme_id', 'theme_name']], on = 'theme_id')
    len(data['set_name'])
    data = pandas.merge(lego_sets, data[['set_name', 'inventory_id', 'num_parts', 'part_num', 'theme_id', 'color_id', 'color_name', 'rgb']], on = 'set_name', how='left')
    data = data.drop(['prod_desc', 'prod_long_desc', 'country', 'num_parts'], axis=1)
    dataMini = data.drop(['inventory_id', 'part_num', 'color_id', 'color_name', 'rgb', 'theme_id', 'prod_id'], axis=1, errors='ignore')
    data = data.drop_duplicates()
    dataMini = dataMini.drop_duplicates()
    len(data['set_name'])
    len(dataMini['set_name'])
    data.head(10)

    # %% codecell
    plt.style.use('seaborn')
    #plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Ubuntu'
    plt.rcParams['font.monospace'] = 'Ubuntu Mono'
    plt.rcParams['font.size'] = 7.0
    plt.rcParams['axes.labelsize'] = 12.0
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 8.0
    plt.rcParams['ytick.labelsize'] = 8.0
    plt.rcParams['figure.titlesize'] = 20.0
    plt.rcParams['figure.titleweight'] = 'bold'
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['figure.figsize'] = 9,4.5


    # %% codecell
    #Graph 1 - Histogram of Star Ratings
    dataMini[['val_star_rating']].plot(kind='hist',bins=np.arange(0,5.1,0.2),rwidth=0.9, figsize=(8,4.5), legend=False)
    plt.xlabel('Rating')
    plt.ylabel('Number of Sets')
    plt.title('Frequency of Star Ratings')
    plt.xticks(np.arange(0,5.2,0.2))
    plt.yticks(np.arange(0,1250,100))
    plt.ylim(0,1200)
    plt.xlim(0,5)
    plt.show()

    # %% codecell
    #Graph 2 - Difficulty Vs. Average Star Ratings
    import seaborn as sns
    order = ['Very Easy', 'Easy', 'Average', 'Challenging','Very Challenging']
    plt.figure(figsize=(8,4.5))
    #dataMini.groupby(['review_difficulty'])['val_star_rating'].mean().loc[order].plot(kind='bar',figsize=(8,4.5), color=['green','limegreen','yellow','orange','red'])
    #dataMini.boxplot(by=['review_difficulty'], column=['val_star_rating'])
    sns.boxplot(x=dataMini['review_difficulty'], y=dataMini['val_star_rating'], order=['Very Easy', 'Easy', 'Average', 'Challenging','Very Challenging'], width=1, hue=dataMini['review_difficulty'], palette='RdYlGn', hue_order=['Very Challenging', 'Challenging', 'Average', 'Easy','Very Easy'])
    plt.legend([])
    plt.title('Review Difficulty Vs. Average Star Ratings')
    plt.xlabel('Review Difficulty')
    plt.yticks(np.arange(1,5.5,0.2))
    plt.ylabel('Average 5-Star Rating')
    plt.ylim(1,5)
    plt.show()

    # %% codecell
    #Graph 3 - List Price Vs. Star Rating
    dataMini.plot(kind='scatter',x='list_price',y='val_star_rating', figsize=(10,4.5), alpha=0.5)
    plt.title("List Price Vs. Star Rating", weight='bold')
    plt.xlabel('List Price ($)')
    plt.yticks(np.arange(1, 5.1, step=0.2))
    plt.xticks(np.arange(0, 1150, step=100))
    plt.xlim(0,1150)
    plt.ylim(.9,5.1)
    plt.ylabel('5-Star Rating')
    plt.show()
    # %% codecell
    #Graph 3.5 - List Price Vs. Star Rating Under $100
    dataMini.plot(kind='scatter',x='list_price',y='val_star_rating', figsize=(9,4.5), alpha=0.1)
    plt.title("List Price Vs. Star Rating Under $150")
    plt.xlabel('List Price ($)')
    plt.yticks(np.arange(1, 5.01, step=0.2))
    plt.xticks(np.arange(0, 151, step=10))
    plt.xlim(0,150)
    plt.ylabel('5-Star Rating')
    plt.show()
    # %% codecell
    #Graph 4 - Piece Count Vs. Star Rating
    dataMini.plot(kind='scatter',x='piece_count',y='val_star_rating',figsize=(9,4.5), alpha = 0.1)
    plt.title("Piece Count vs Star Rating")
    plt.xlabel('Piece Count')
    plt.xlim(0,8000)
    plt.yticks(np.arange(0, 5.1, step=0.2))
    plt.ylabel('5-Star Rating')
    plt.show()

    # %% codecell
    #Graph 4.5 - Piece Count (Under 1000) Vs. Star Rating
    dataMini.plot(kind='scatter',x='piece_count',y='val_star_rating',figsize=(9,4.5), alpha = 0.1)
    plt.title("Piece Count vs Star Rating")
    plt.xlabel('Piece Count')
    plt.xlim(0,1000)
    plt.yticks(np.arange(0, 5.1, step=0.2))
    plt.ylabel('5-Star Rating')
    plt.show()

    # %% codecell
    #Graph 5 - Color Vs. Average Star Ratings
    colors=(list(data.groupby(['color_name'])['rgb'].unique()))
    print(colors)
    colors=["#"+x[0] for x in colors]
    plt.figure(figsize=(16,12))
    data.groupby(['color_name'])['val_star_rating'].mean().plot(kind='bar', title='Color Vs. Average Star Ratings',color=colors, figsize=(15,4.5))
    plt.xlabel('Color Name')
    plt.yticks(np.arange(3,5.5,0.2))
    plt.ylabel('Average 5-Star Rating')
    plt.ylim(3,5)
    plt.show()
