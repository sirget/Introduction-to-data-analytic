import pandas as pd
import numpy as np

path = "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRIFbIywXecgxN5c1sMn_KYWsARoXgp4paFxu4qndPaX_47vRaOdrqmiHjtNZ9ZYQcv3ubMSv8DA9ta/pub?gid=1546938151&single=true&output=csv"

df = pd.read_csv(path)

print(df)

#df['extra_salary'] = df['salary'] * df['department'].apply(lambda x : 0.2 if x == 'developer' else 0.5)

#print(len(df))

#df['name_with_age'] = df['name'] + ('(') + df['age'].astype(str) + (')')

print(df.groupby(['gender','department']).agg({'salary':'mean'}).loc['female'].idxmax().values[0])

print(df['department'].unique())

print(df)