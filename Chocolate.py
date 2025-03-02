import pandas as pd

######## Step 2 Reading the Dataset
# Read the dataset into a Pandas DataFrame
# delete messing value entries

# Read the dataset into a Pandas DataFrame!
df = pd.read_csv('flavors_of_cacao.csv')
# remove \xa0 (non-breaking space)
df.columns = df.columns.str.replace('\xa0', '', regex=False)
# replace \n (new line) with a space
df.columns = df.columns.str.replace('\n', ' ', regex=False)

# fixed folumn names
print(df.columns)
# data types of columns
print(df.dtypes)

# delete messing value entries
df = df.dropna()

######## Step 3 Exploring the Dataset
# How many tuples are there in the dataset?
print("Number of tuples:", len(df))

# How many unique company names are there in the dataset?
print("Number of unique companies:", df['Company (Maker-if known)'].nunique())

# How many reviews are made in 2013 in the dataset?
reviews_2013 = df[df['Review Date'] == 2013]
print("Number of reviews in 2013:", len(reviews_2013))

# In the BeanType Column, how many missing values are there?
print("Missing values in BeanType column:", df['Bean Type'].isnull().sum())

######## Step 4 Visualization
import matplotlib.pyplot as plt

# Visualize the rating column with a histogram!
plt.hist(df['Rating'], bins=20, edgecolor='black')
plt.title('Distribution of Chocolate Bar Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Convert and Visualize.
# Convert the Column Percent.
# Change the type of values in the column percent from string values to numerical values.
df['Cocoa Percent'] = df['Cocoa Percent'].str.replace('%', '').astype(float)

######## Step 5 Visualize
plt.hist(df['Cocoa Percent'], bins=20, edgecolor='black')
plt.title('Distribution of Cocoa Percent')
plt.xlabel('Cocoa Percent')
plt.ylabel('Frequency')
plt.show()

######## Step 6 Normalization
# Normalize the Rating Column and print the results.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_rating = scaler.fit_transform(df[['Rating']])
df['Normalized Rating'] = scaled_rating
print(scaled_rating)

####### Step 8 Encoding
# Suppose we are interested in the company’s names and locations for some collective analysis. Encode the two categorical columns with the encoder you think is best for the job!
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder = LabelEncoder()
one_hot_encoder = OneHotEncoder(sparse_output=False)
companynames = df.iloc[:,0].values
locations = df[['Company Location']].values
encoded_companynames = label_encoder.fit_transform(companynames)
encoded_locations = one_hot_encoder.fit_transform(locations)

print(encoded_companynames)    
print(encoded_locations)    