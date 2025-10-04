import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Module': ['AI', 'ML', 'Python', 'DataStructures'],
    'Teamsize': [135, 125, 125, 115]
}

df = pd.DataFrame(data)
print(df)


df.plot(
    y='Teamsize',        # Values for slices
    labels=df['Module'], # Labels for each slice
    kind='pie',          # Pie chart
    autopct='%1.1f%%',   # Show percentage
    legend=False,        # Hide legend
    title='Team Size Distribution by Module',
    ylabel=''            # Remove default y-label
)

plt.show()

