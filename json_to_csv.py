import pandas as pd

df = pd.read_json('json_converted.json')
df.to_csv('csv_converted.csv')

df_csv = pd.read_csv('csv_converted.csv', index_col=0)
df_csv = df_csv.fillna('')
print(df_csv.iloc[:, 0:])
