import pandas as pd
import numpy as np
import math

df = pd.read_csv("imdb_top_1000.csv")
print(df.head())
print(df.tail())
result = df.columns
print(result)
result = df.info
print(result)

# ilk 5 kaydı gösteriniz.
print(df.head(5))
print(df.head(10))
print(df.tail(5))
print(df.tail(10))
result = df["Series_Title"]
print(result)
result = df["Series_Title"].head()
print(result)
result = df[["Series_Title","IMDB_Rating"]].head()
print(result)
result = df[5:][["Series_Title","IMDB_Rating"]].head()
print(result)
result = df[df["IMDB_Rating"] >= 8][["Series_Title","IMDB_Rating"]].head(50)
print(result)
result = df[(df[("Released_Year")].astype(int) >= 2014) & (df[("Released_Year")].astype(int) <= 2015)][[("Released_Year"),"Series_Title"]]
print(result)
result = df["Released_Year"].head()
print(result)