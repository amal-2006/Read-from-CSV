import pandas as pd
df = pd.read_csv("C:\Users\admin\Downloads\nba.csv")
print(df.head(10))
print(df.tail())
print("Number of rows:",len(df.axes[0]))
print("Number of columns:",len(df.axes[1]))