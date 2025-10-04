import pandas as pd
import matplotlib.pyplot as plt

data = {
"Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
"Week1": [1000, 2000, 3000, 5000, 7000, 8000, 6700],
"Week2": [4000, 5000, 2500, 4500, 3500, 5000, 5600],
"Week3": [5000, 6000, 4500, 3500, 2000, 6000, 4800],
"Week4": [6000, 5000, 2900, 4500, 3500, 4500, 4500]
}
df = pd.DataFrame(data)
print(df)

#Line plot 

df.plot(
    x='Day',
    y= ['Week1','Week2','Week3','Week4'],
    kind='line',
    marker='o',
    title='Weekly Data Trend'

)

df.plot(
    x='Day',             # X-axis
    y=['Week1', 'Week2','Week3','Week4'],# Columns to plot
    kind='bar',          # Bar plot
    title='Weekly Comparison'
)

df[['Week1','Week2','Week3','Week4']].plot(
    kind='hist',      # Histogram
    bins=6,           # Number of bins
    alpha=0.7,        # Transparency for overlapping
    title='Distribution of Weekly Values'
)

plt.show()

