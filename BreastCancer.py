import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the dataset into a Pandas DataFrame!
df = pd.read_csv('breast_cancer_data.csv')
# delete messing value entries
print(df.info())
print(df.isna().sum())

# there is an extra comma after the last column name
# remove unnamed column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df.info())
print(df.isna().sum())
# no missing value

# Dropping Unnecessary Columns
df = df.drop(columns=['id'])

#print(df.head())
# encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['diagnosis'] = label_encoder.fit_transform(df['diagnosis'])

# normalize features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
feature_cols = df.columns.drop('diagnosis')
df[feature_cols] = scaler.fit_transform(df[feature_cols])
# save
df.to_csv("cancer_data_refined.csv", index=False)

#visualization

# Pair Plot
#sns.pairplot(df, hue='diagnosis', diag_kind='kde')
#plt.show()
sns.pairplot(df, vars=["radius_mean", "texture_mean", "perimeter_mean"], hue="diagnosis")
plt.show()

# Compute correlation matrix
corr_matrix = df.corr()
# Create heatmap
plt.figure(figsize=(12, 8))  # Adjust figure size
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()

# Create a box plot for one feature
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["radius_mean"])  # Change feature name as needed

plt.title("Box Plot of Radius Mean")
plt.show()


#Challenge Yourself
#Visualize your data in violin plots.
#Describe what a violin plot is.
#Determine whether or not some of the features have outliers based on your violin plots.