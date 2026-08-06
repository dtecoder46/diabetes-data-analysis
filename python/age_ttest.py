import scipy
from scipy import stats

import numpy as np

data_class1 = open("diabetes_class1.csv", "r")

diabetes_class1 = data_class1.read()

# CSV string -> 2D array

list_of_lines = diabetes_class1.split("\n")

array_2d = []

for line in list_of_lines:
	line_split = line.split(",")
	
	array_2d.append(line_split)

# Extract the age column into an array

age_list = []

for line in array_2d:

	if len(line) > 1:
		age_int = int(line[2]) # ttest_1samp only accepts int arrays
		age_list.append(age_int)

# TODO: ttest

x = np.array(age_list)

# H0: average age for diabetes outcome class 1 = 50
# Ha: average age > 50

t_stat, p_value = stats.ttest_1samp(a=x, popmean=50, alternative='greater')

print(f"T-stat: {t_stat}")

print(f"P-value: {p_value}")

data_class1.close()
