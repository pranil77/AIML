import pandas as pd

mydataset={'cars':['BMW','VOLVO','LAMBO'],
           'Passings':[1,2,3] }
        
df=pd.DataFrame(mydataset)
print(df)

a=[1,2,3,4]
ser=pd.Series(a)
print(ser)

ser2=pd.Series(a,index=["x","y","z","w"])
print(ser2)

calories={'paratha':650,'beer':1000,'banana':350}
ser3=pd.Series(calories)
print(ser3)

print("\n\n")
data={'calories':[350,450,550],
      'Duration':[50,60,70]}
df1=pd.DataFrame(data)
print("\n")
print(df1)
print(df1.loc[0])
print(df1.loc[0:1])
print("\n\n")

df3=pd.read_csv("C:\\Users\\pranil\\Desktop\\people.csv")
print(df3)
print(df3.head(5))
print(df3.tail(5))

new_df=df3.dropna()
print(new_df)

df3.fillna(130, inplace = True)

print(df3.duplicated())

df3.drop_duplicates(inplace = True)