import pandas as pd

data = pd.read_csv("data.csv")
age = data["Age"]
descriptive_stats = age.describe()
print(descriptive_stats)

