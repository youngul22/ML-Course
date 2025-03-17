import pandas as pd
import matplotlib.pyplot as plt

######## Step 2 Reading the Dataset
# Read the dataset into a Pandas DataFrame
# delete messing value entries

# Read the dataset into a Pandas DataFrame!
df = pd.read_csv('results.csv')
# delete messing value entries
df = df.dropna()

######## Step 3 Exploring the Dataset
# How many tuples are there in the dataset?
print("Number of tuples:", len(df))
print("Column Names: ", df.columns)

# How many tournaments are there is the dataset?
print("Number of tournaments:", df['tournament'].nunique())

# Convert the column date to timestamps!
df['timestamp'] = pd.to_datetime(df['date'])
count_2018 = (df['timestamp'].dt.year == 2018).sum()

# Find out how many matches in the dataset were played in 2018.
print('Number of matches played in 2018: ', count_2018)

# Calculate how many times the home team won, lost, or had a draw.
home_won = (df['home_score'] > df['away_score']).sum()
home_lost = (df['home_score'] < df['away_score']).sum()
home_draw =  (df['home_score'] == df['away_score']).sum()
print('Home team win: ', home_won)
print('Home team lost: ', home_lost)
print('Home team draw: ', home_draw)

# Step 6 Visualization
# Labels and values for pie chart
labels = ['Home Wins', 'Home Draws', 'Home Losses']
values = [home_won, home_lost, home_draw]
colors = ['#4CAF50', '#FFC107', '#F44336']  # Green, Yellow, Red

# Create Pie Chart
plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})

# Title
plt.title("Home Team Performance (Wins, Draws, Losses)")

# Show chart
plt.show()