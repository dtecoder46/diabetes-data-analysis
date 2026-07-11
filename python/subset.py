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

# cursor.execute(command)
# conn.commit()

# cursor.execute(select_command)
# result = cursor.fetch()
