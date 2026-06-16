csv = open("data.csv")
data = []

for line in range(1,2768): # number of rows in the dataset
    row = csv.readline().split(",")
    data.append(row)

csv.close()

data.pop(0)

print(data[0])

