csv = open("data.csv")
data = []

for line in range(1,2768): # number of rows in the dataset
    row = csv.readline().split(",")
    data.append(row)

csv.close()

data.pop(0) # needed to remove the header, as it is useless at this point

for row in range(0,2766): # range of indices in the 2D array
    array_row = data[row]
    row_length = len(array_row)
    diabetes_status = array_row[row_length - 1]
    
    status_array = diabetes_status.split("\n")
    diabetes_status = status_array[0]

    array_row[row_length - 1] = diabetes_status

    

