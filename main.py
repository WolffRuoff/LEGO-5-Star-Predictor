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
    #len(inventory_parts['inventory_id'])
    #len(colors['color_id'])
    #len(lego_sets['set_name'])
    data = pandas.merge(sets, inventories[['inventory_id', 'set_num']], on = 'set_num', how='left')
    data = pandas.merge(data, inventory_parts[['inventory_id', 'part_num', 'color_id']], on = 'inventory_id', how='right')
    data = pandas.merge(data, colors[['color_id','color_name', 'rgb']], on = 'color_id')
    data = pandas.merge(data, themes[['theme_id', 'theme_name']], on = 'theme_id')
    len(data['set_name'])
    data = pandas.merge(lego_sets, data[['set_name', 'inventory_id', 'num_parts', 'part_num', 'theme_id', 'color_id', 'color_name', 'rgb']], on = 'set_name', how='left')
    data = data.drop(['prod_desc', 'prod_long_desc', 'country', 'num_parts'], axis=1)
    data = data.drop(['inventory_id', 'part_num', 'color_id', 'color_name', 'rgb', 'theme_id', 'prod_id'], axis=1, errors='ignore')
    data = data.drop_duplicates()
    len(data['set_name'])
    data.head(20)

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
    data[['val_star_rating']].plot(kind='hist',bins=np.arange(0,5.1,0.2),rwidth=0.9, figsize=(8,4.5), legend=False)
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
    plt.figure(figsize=(7,4.5))
    #dataMini.groupby(['review_difficulty'])['val_star_rating'].mean().loc[order].plot(kind='bar',figsize=(8,4.5), color=['green','limegreen','yellow','orange','red'])
    #dataMini.boxplot(by=['review_difficulty'], column=['val_star_rating'])
    sns.boxplot(x=data['review_difficulty'], y=data['val_star_rating'], order=['Very Easy', 'Easy', 'Average', 'Challenging','Very Challenging'], width=0.5, fliersize=3, hue=data['review_difficulty'], palette='RdYlGn', hue_order=['Very Challenging', 'Challenging', 'Average', 'Easy','Very Easy'])
    plt.legend([])
    plt.title('Review Difficulty Vs. Average Star Ratings')
    plt.xlabel('Review Difficulty')
    plt.yticks(np.arange(1,5.5,0.2))
    plt.ylabel('Average 5-Star Rating')
    plt.ylim(1,5)
    plt.show()

    # %% codecell
    #Graph 3 - List Price Vs. Star Rating
    data.plot(kind='scatter',x='list_price',y='val_star_rating', figsize=(10,4.5), alpha=0.5)
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
    data.plot(kind='scatter',x='list_price',y='val_star_rating', figsize=(9,4.5), alpha=0.1)
    plt.title("List Price Vs. Star Rating Under $150")
    plt.xlabel('List Price ($)')
    plt.yticks(np.arange(1, 5.01, step=0.2))
    plt.xticks(np.arange(0, 151, step=10))
    plt.xlim(0,150)
    plt.ylabel('5-Star Rating')
    plt.show()

    # %% codecell
    #Graph 4 - Piece Count Vs. Star Rating
    data.plot(kind='scatter',x='piece_count',y='val_star_rating',figsize=(9,4.5), alpha = 0.1)
    plt.title("Piece Count vs Star Rating")
    plt.xlabel('Piece Count')
    plt.xlim(0,8000)
    plt.yticks(np.arange(0, 5.1, step=0.2))
    plt.ylabel('5-Star Rating')
    plt.show()

    # %% codecell
    #Graph 4.5 - Piece Count (Under 1000) Vs. Star Rating
    data.plot(kind='scatter',x='piece_count',y='val_star_rating',figsize=(9,4.5), alpha = 0.1)
    plt.title("Piece Count vs Star Rating")
    plt.xlabel('Piece Count')
    plt.xlim(0,1000)
    plt.yticks(np.arange(0, 5.1, step=0.2))
    plt.ylabel('5-Star Rating')
    plt.show()

    # %% codecell
    # Cleanup Data
    cleanup_difficulty = {"review_difficulty":     {"Very Easy": 1, "Easy": 2, "Average": 3, "Challenging": 4, "Very Challenging": 5}}
    data.replace(cleanup_difficulty, inplace=True)
    data.head()

    #Official Age ratings used on the LEGO store website
    # 0 = 1-2
    # 1 = 3-5
    # 2 = 6-8
    # 3 = 9-11
    # 4 = 12+
    #Category chosen by average of age rage rounded down with + values using the minimum age
    cleanup_age = {"ages":     {"6-12": 3, "7-14": 3, "8-14": 3, "5-12": 2, "2-5": 1, "7-12": 2, "4-7": 1, "10+": 3, "9-14": 3, "16+": 4, "8-12": 3,
                                "12+": 4, "4-99": 4, "8+": 2, "14+": 4, "1½-3": 0, "6-14": 3, "10-21": 4, "10-16": 4, "6+": 2, "1½-5": 1, "9-16": 4,
                                "11-16": 4, "5+": 1, "12-16": 4, "9-12": 3, "9+": 3, "5-8": 2, "10-14": 4, "4+": 1, "7+": 2}}
    data.replace(cleanup_age, inplace=True)
    data.head()
