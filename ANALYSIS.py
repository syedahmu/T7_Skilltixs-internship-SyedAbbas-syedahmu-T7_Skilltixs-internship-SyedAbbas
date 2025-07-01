import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # for visualizing data
import seaborn as sns

# Import CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Display basic information
print("Data Shape:", df.shape)
print("First 5 Rows:")
print(df.head())
print("Dataset Information:")
print(df.info())

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
print("Null Values Count:")
print(pd.isnull(df).sum())

# Drop rows with null values
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype('int')

# Rename column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Describe dataset
print("Dataset Description:")
print(df.describe())

# Describe specific columns
print("Description of Specific Columns:")
print(df[['Age', 'Orders', 'Amount']].describe())

# Plotting a bar chart for Gender and its count
plt.figure(figsize=(6, 4))
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Gender Distribution')
plt.tight_layout()
plt.show()

# Gender vs Total Amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 4))
sns.barplot(x='Gender', y='Amount', data=sales_gen)
plt.title('Total Amount by Gender')
plt.tight_layout()
plt.show()
#  From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men


# Age Group vs Gender Count
plt.figure(figsize=(8, 6))
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Age Group vs Gender Distribution')
plt.tight_layout()
plt.show()

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(8, 6))
sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.title('Total Amount by Age Group')
plt.tight_layout()
plt.show()
# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female


# Total Number of Orders from Top 10 States
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data=sales_state, x='State', y='Orders')
plt.title('Top 10 States by Number of Orders')
plt.tight_layout()
plt.show()

# Total Amount/Sales from Top 10 States
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data=sales_state, x='State', y='Amount')
plt.title('Top 10 States by Total Amount')
plt.tight_layout()
plt.show()
# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively


# Marital Status Distribution
plt.figure(figsize=(7, 5))
ax = sns.countplot(data=df, x='Shaadi')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Marital Status Distribution')
plt.tight_layout()
plt.show()

# Marital Status vs Gender and Total Amount
sales_state = df.groupby(['Shaadi', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 5))
sns.barplot(data=sales_state, x='Shaadi', y='Amount', hue='Gender')
plt.title('Total Amount by Marital Status and Gender')
plt.tight_layout()
plt.show()
# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power


# Occupation Distribution
plt.figure(figsize=(20, 5))
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Occupation Distribution')
plt.tight_layout()
plt.show()

# Occupation vs Total Amount
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Occupation', y='Amount')
plt.title('Total Amount by Occupation')
plt.tight_layout()
plt.show()
# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# Product Category Distribution
plt.figure(figsize=(20, 5))
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Product Category Distribution')
plt.tight_layout()
plt.show()

# Product Category vs Total Amount
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Product_Category', y='Amount')
plt.title('Top 10 Product Categories by Total Amount')
plt.tight_layout()
plt.show()

# Product ID vs Total Orders
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Product_ID', y='Orders')
plt.title('Top 10 Products by Number of Orders')
plt.tight_layout()
plt.show()
# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# Top 10 Most Sold Products
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar', ax=ax1)
ax1.set_title('Top 10 Most Sold Products')
plt.tight_layout()
plt.show()



# Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
