import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file = "C:/PRODIGY_DS_01-main/titanic.csv"
# Load the Titanic dataset
train_data = pd.read_csv(file)

# Display the first few rows of the dataset
print(train_data.head())

# Create a bar chart for the distribution of genders
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', data=train_data, palette='viridis')
plt.title('Distribution of Genders on the Titanic')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Create a histogram for the distribution of ages
plt.figure(figsize=(10, 6))
sns.histplot(train_data['Age'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of Ages on the Titanic')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()