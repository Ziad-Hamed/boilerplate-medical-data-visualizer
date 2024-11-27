import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv(r"C:\Users\Ziad\boilerplate-medical-data-visualizer\medical_examination.csv")

# 2
df['overweight'] = np.where(df["weight"]/ ((df['height']/100) ** 2)>25, 1, 0)
# df.insert(12, 'overweight',np.where(df['weight']/ ((df['height']/100) ** 2)>25, 1, 0))

# 3
df['cholesterol'] = np.where(df['cholesterol'] >1, 1, 0)
df['gluc'] = np.where(df['gluc'] >1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio',value_vars=['cholesterol', 'gluc','smoke','alco', 'active',  'overweight']  )


    # 6
    # Group and reformat the data in df_cat to split it by cardio. 
    # Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly
    # df_cat = None
    

    # 7
    # Convert the data into long format and 
    # create a chart that shows the value counts of the categorical features
    # sns.catplot( data=df_cat, x='variable', hue='value', col='cardio', kind='count',
    # height=4, aspect=1.3,order=order_list )
    # df_cat.set_ylabels('total')

    # 8
    order_list = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'] 

    fig = sns.catplot( data=df_cat, x='variable', hue='value', col='cardio', kind='count',
    height=4, aspect=1.3,order=order_list ).set_ylabels('total').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
    & (df['height'] >= df['height'].quantile(0.025)) 
    & (df['height'] <= df['height'].quantile(0.975))
    & (df['weight'] >= df['weight'].quantile(0.025)) 
    & (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15

    sns.heatmap( corr ,center=0.08,annot=True ,fmt='.1f', square=True,mask=mask, annot_kws={'size': 6},linewidths=.01, linecolor='white', cbar_kws={'shrink':0.5 })

    # 16
    fig.savefig('heatmap.png')
    return fig
