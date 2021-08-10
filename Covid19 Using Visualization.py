from time import sleep
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pycountry
import plotly.express as px
import pandas as pd
DATASET = pd.read_excel(r'Covid_Input_File.xlsx')
df1 = pd.read_excel(r'Covid_Input_File.xlsx')
print(df1.head(3))  # Get first 3 entries in the dataframe
print(df1.tail(3))  # Get last 3 entries in the dataframe
df_india = df1[df1['Country'] == 'India']
print(df_india.head(3))


# ----- Step 1 (Download data)----
DATASET = pd.read_excel(r'Covid_Input_File.xlsx')
df1 = pd.read_excel(r'Covid_Input_File.xlsx')
print(df1.head(3))

# ----- Step 2 (Select data for India)----
df_india = df1[df1['Country'] == 'India']
print(df_india.head(3))

# ----- Step 3 (Plot data)----

# Plot column 'Confirmed'
df_india.plot(kind='bar', x='Date', y='Confirmed', color='blue')

ax1 = plt.gca()
df_india.plot(kind='bar', x='Date', y='Deaths', color='red', ax=ax1)
plt.show()

my_anim = animation.FuncAnimation(fig=fig, func=plot_bar,
                                  frames=list_dates, blit=True,
                                  interval=20)


# ---- Step 1:- Download data
DATASET = pd.read_excel(r'Covid_Input_File.xlsx')
df = pd.read_csv(DATASET, usecols=['Date', 'Country', 'Confirmed'])
print(df.head(3))

# ---- Step 2:- Create list of all dates
list_dates = df['Date'].unique()
print(list_dates)

# --- Step 3:- Pick 5 countries. Also create ax object
fig, ax = plt.subplots(figsize=(15, 8))
# We will animate for these 5 countries only
list_countries = ['India', 'China', 'US', 'Italy', 'Spain']
# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']

# --- Step 4:- Write the call back function


def plot_bar(some_date):
    df2 = df[df['Date'].eq(some_date)]
    ax.clear()
    # Only take Confirmed column in descending order
    df3 = df2.sort_values(by='Confirmed', ascending=False)
    # Select the top 5 Confirmed countries
    df4 = df3[df3['Country'].isin(list_countries)]
    print(df4)
    sleep(0.2)
    ax.barh()
    return ax.barh(df4['Country'], df4['Confirmed'], color=list_colors)


# ----Step 5:- Create FuncAnimation object---------
my_anim = animation.FuncAnimation(fig=fig, func=plot_bar,
                                  frames=list_dates, blit=True,
                                  interval=20)

plt.show()
