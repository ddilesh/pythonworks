import pandas as pd 
df=pd.read_csv("data.csv")
print(df)

print("Univariate Analysis")

print(df['Duration'].describe())

mean_duration = df['Duration'].mean()
print(mean_duration)
median_duration = df['Duration'].median()
print(median_duration)
std_duration = df['Duration'].std()
print(std_duration)


print("Bivariate Analysis")

print(df.groupby("Status")["Duration"].mean())


print("Multivariate Analysis")
print(df.groupby(["Module","Status"])["Defects"].sum())