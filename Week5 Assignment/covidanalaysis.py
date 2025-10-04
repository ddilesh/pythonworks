import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CovidAnalysis:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!")
        print(f"Shape of Data: {self.data.shape}")
        print("Columns:", list(self.data.columns))
    
    def show_summary(self):
        print("\nData Summary:")
        print(self.data.describe())

    def top_countries_by_confirmed(self, n=10):
        return self.data.nlargest(n, 'Confirmed')[['Country/Region', 'Confirmed']]

    def top_countries_by_deaths(self, n=10):
        return self.data.nlargest(n, 'Deaths')[['Country/Region', 'Deaths']]

    def get_country_data(self, country_name):
        return self.data[self.data['Country/Region'] == country_name]

# --------------------------------------------------
# Derived Class: CovidVisualization
# --------------------------------------------------
class CovidVisualization(CovidAnalysis):

    # 1️⃣ Bar Chart of Top 10 Countries by Confirmed Cases
    def bar_chart_top10_confirmed(self):
        top10 = self.top_countries_by_confirmed()
        plt.figure(figsize=(10,6))
        plt.bar(top10['Country/Region'], top10['Confirmed'], color='skyblue')
        plt.title('Top 10 Countries by Confirmed Cases')
        plt.xlabel('Country')
        plt.ylabel('Confirmed Cases')
        plt.xticks(rotation=45)
        plt.show()

    # 2️⃣ Pie Chart of Global Death Distribution by Region
    def pie_chart_death_distribution(self):
        deaths = self.data.groupby('Country/Region')['Deaths'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(8,8))
        plt.pie(deaths, labels=deaths.index, autopct='%1.1f%%', startangle=140)
        plt.title('Global Death Distribution (Top 10 Countries)')
        plt.show()

    # 3️⃣ Line Chart comparing Confirmed and Deaths for Top 5 Countries
    def line_chart_confirmed_vs_deaths(self):
        top5 = self.top_countries_by_confirmed(5)
        plt.figure(figsize=(10,6))
        plt.plot(top5['Country/Region'], top5['Confirmed'], marker='o', label='Confirmed')
        plt.plot(top5['Country/Region'], self.data.nlargest(5, 'Deaths')['Deaths'], marker='o', label='Deaths')
        plt.title('Confirmed vs Deaths (Top 5 Countries)')
        plt.xlabel('Country')
        plt.ylabel('Count')
        plt.legend()
        plt.show()

    # 4️⃣ Scatter Plot of Confirmed Cases vs Recovered Cases
    def scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(8,6))
        plt.scatter(self.data['Confirmed'], self.data['Recovered'], color='purple')
        plt.title('Confirmed vs Recovered Cases')
        plt.xlabel('Confirmed Cases')
        plt.ylabel('Recovered Cases')
        plt.show()

    # 5️⃣ Histogram of Death Counts across all Regions
    def histogram_deaths(self):
        plt.figure(figsize=(10,6))
        plt.hist(self.data['Deaths'], bins=20, color='orange', edgecolor='black')
        plt.title('Distribution of Death Counts Across Regions')
        plt.xlabel('Deaths')
        plt.ylabel('Number of Countries')
        plt.show()

    # 6️⃣ Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
    def stacked_bar_chart(self, countries):
        subset = self.data[self.data['Country/Region'].isin(countries)]
        subset = subset[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']].set_index('Country/Region')
        subset.plot(kind='bar', stacked=True, figsize=(10,6))
        plt.title('Stacked Bar Chart - Confirmed, Deaths & Recovered')
        plt.ylabel('Cases')
        plt.show()

    # 7️⃣ Box Plot of Confirmed Cases across Regions
    def boxplot_confirmed(self):
        plt.figure(figsize=(8,6))
        plt.boxplot(self.data['Confirmed'], vert=True)
        plt.title('Box Plot of Confirmed Cases Across Regions')
        plt.ylabel('Confirmed Cases')
        plt.show()

    # 8️⃣ Trend Line: India vs Another Country
    def trendline_india_vs_country(self, other_country):
        india = self.get_country_data('India')
        other = self.get_country_data(other_country)

        plt.figure(figsize=(10,6))
        plt.plot(india['Confirmed'], label='India', marker='o')
        plt.plot(other['Confirmed'], label=other_country, marker='o')
        plt.title(f'Trend Comparison: India vs {other_country}')
        plt.xlabel('Index')
        plt.ylabel('Confirmed Cases')
        plt.legend()
        plt.show()



