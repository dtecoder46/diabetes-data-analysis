import sqlite3


csv = open("data.csv")
data = []

for line in range(1,2768): # number of rows in the dataset
	row = csv.readline().split(",") # turns each row of the dataset into a list
	data.append(row) # appends each row to a list to build out a 2D array

csv.close()

data.pop(0) # needed to remove the header, as it is useless at this point

for row in range(0,2766): # range of indices in the 2D array
	array_row = data[row]
	row_length = len(array_row)
	diabetes_status = array_row[row_length - 1] # diabetes_status variable is found in the second to last column
    
	# ensures newline character isn't included

	status_array = diabetes_status.split("\n")
	diabetes_status = status_array[0]

   	# reassign cleaned value to the diabetes_status variable slot in the 2D array
		
	array_row[row_length - 1] = diabetes_status

# SQLite3 setup

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Table creation

<<<<<<< HEAD
cursor.execute('CREATE TABLE diabetes (outcome INTEGER, bmi FLOAT, blood_pressure INTEGER, age INTEGER, bmi_class TEXT);')
=======
cursor.execute('CREATE TABLE diabetes (outcome INTEGER, bmi FLOAT, blood_pressure INTEGER, age INTEGER, bmi_class TEXT(15);')
>>>>>>> 3e622d9ae84bdd92c6f847c8d523d500cb5b0a6d
conn.commit()

# Loop over 2D array, insert values from each row

for line in range(0,2766):

    # diabetes outcome: column index 9
    # bmi: column index 6
    # blood pressure: column index 3
    # age: column index 8
    # bmi_class: see conditionals below

    bmi_class = ""

    # data[line][6]: bmi

<<<<<<< HEAD
    bmi = float(data[line][6])
=======
    bmi = data[line][6]
>>>>>>> 3e622d9ae84bdd92c6f847c8d523d500cb5b0a6d

    if bmi >= 19 and bmi <= 24:
        bmi_class = "normal weight"
    elif bmi >= 25 and bmi <= 29:
        bmi_class = "overweight"
    elif bmi >= 30 and bmi <= 39:
        bmi_class = "obese"
    else:
        bmi_class = "extreme obesity"

    insert = f'INSERT INTO diabetes (outcome, bmi, blood_pressure, age, bmi_class) VALUES ({data[line][9]}, {data[line][6]}, {data[line][3]}, {data[line][8]}, \"{bmi_class}\");'

    cursor.execute(insert)

# Subset by diabetes outcome

# Subset patients with diabetes

class1_subset = cursor.execute('SELECT * FROM diabetes WHERE outcome = 1;')
diabetes_class1 = class1_subset.fetchall() # list

print(diabetes_class1)

# Subset patients without diabetes

class0_subset = cursor.execute('SELECT * FROM diabetes WHERE outcome = 0;')
diabetes_class0 = class0_subset.fetchall()
