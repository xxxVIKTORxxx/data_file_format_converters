import pandas as pd

excel_data_df = pd.read_excel('data mess.xlsx', sheet_name='Sheet1')

json_file = excel_data_df.to_json()

print('.xlsx to .json', json_file)

file = 'json_converted.json'
with open(file, 'w') as to_convert:
    to_convert.write(json_file)

df = pd.read_json('json_converted.json')

print(df)

