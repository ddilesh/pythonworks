import pandas as pd 
import numpy as np 

coviddata=pd.read_csv("country_wise_latest.csv")


df=pd.DataFrame(coviddata)
print(df)

print("1.Summarize case count by Region")

print(df.groupby("WHO Region")[["Deaths","Recovered","Confirmed"]].count())

print("2.Filter Lower case Records")

print(df[df['Confirmed']>=10])

print("3.Identify Region with Highest Confirmed Cases")

print(df.groupby("WHO Region")["Confirmed"].sum().idxmax())
print(df.groupby("WHO Region")["Confirmed"].sum().max())

print("4.Sort data by confirmed cases")

print(df.sort_values(by='Confirmed'))

sortedvalues=df.sort_values(by='Confirmed')
sortedvalues.to_csv("sorted_countrywisefile.csv",index=False)

print("5.Top five countires by case count")
print(df.sort_values(by="Confirmed", ascending=False).head(5))

print("6.Region with Lowest death Count")
print(df.groupby("WHO Region")["Deaths"].sum().idxmin())
print(df.groupby("WHO Region")["Deaths"].sum().min())

print("7.India's case Summary as of April")
print(df[df["Country/Region"]=="India"])

print("8.Calculate Mortality rate by Region -Death to confirmed case Ratio")

region_summary = df.groupby("WHO Region")[["Confirmed", "Deaths"]].sum()

region_summary["Mortality Rate"] = region_summary["Deaths"] / region_summary["Confirmed"]

print(region_summary)

print("9.Compare Recovery Rates across Regions")

reg_summary = df.groupby("WHO Region")[["Confirmed", "Recovered"]].sum()
reg_summary["Recovery Rate"] = reg_summary["Recovered"] / reg_summary["Confirmed"]
print(reg_summary)


print("10.Detect Outliers in Case counts")
mean_val = df["Confirmed"].mean()
std_val  = df["Confirmed"].std()
lower_bound = mean_val - 2*std_val
upper_bound = mean_val + 2*std_val

outliers = df[(df["Confirmed"] < lower_bound) | (df["Confirmed"] > upper_bound)]
print("Outliers in Confirmed Cases:")
print(outliers)

print("11.Group data by Country & Region")
grouped_data = df.groupby(["WHO Region", "Country/Region"])[["Confirmed", "Deaths", "Recovered"]].sum()
print(grouped_data)

print("12.Regions with Zero Recovered cases")
region_recovery = df.groupby("WHO Region")["Recovered"].sum()
zero_recovery_regions = region_recovery[region_recovery == 0]
print("Regions with Zero Recovered Cases:")
print(zero_recovery_regions)


