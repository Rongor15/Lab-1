import pandas as pd

df = pd.read_csv('results.csv',
                sep=',')
all_cont = df['region_eng'].unique()
