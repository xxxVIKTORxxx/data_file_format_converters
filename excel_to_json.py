import pandas as pd

excel_data_df = pd.read_excel('data mess 2.xlsx', sheet_name='Sheet2')

df = excel_data_df.fillna('')

print(df)

json_file = df.to_json()

print('Excel Sheet to JSON:\n', json_file)

file = 'json_converted.json'
with open(file, 'w') as to_convert:
    to_convert.write(json_file)

df = pd.read_json('json_converted.json')

print(df)

