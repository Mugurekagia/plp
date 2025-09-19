import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print("First 5 rows of dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nMissing Values per Column:")
print(df.isnull().sum())

df = df.dropna()

print("\nBasic Statistics:")
print(df.describe())

grouped = df.groupby("species")["petal_length"].mean()
print(grouped)

for species in df['species'].unique():
    species_data = df[df['species'] ==species].reset_index()
    plt.plot(species_data.index, species_data['petal_length'], label=species)
plt.title("Petal Length Trend by Species")
plt.xlabel("Index")
plt.ylabel("Petal Length")
plt.legend()
plt.show()

grouped.plot(kind="bar", color=["skyblue", "lightgreen", "salmon"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

plt.hist(df['sepal_length'], bins=15, color="purple", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], label=species)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

