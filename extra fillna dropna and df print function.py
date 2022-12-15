import pandas as pd

df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())

#This operation inserts 130 in empty cells in the "Calories" column (row 18


import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
#As you can see in row 18, the empty values from "Calories" was replaced with the mean: 304.68


import pandas as pd

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())



import pandas as pd

df = pd.read_csv('data.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())


import pandas as pd
df = pd.read_csv('data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
	df.loc[x, "Duration"] = 120
print(df.to_string())



import pandas as pd

df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())

#Notice that row 12 has been removed from the result


