install.packages("mosaic")
library(mosaic)

data = read.csv("data.csv")
BMI = data[7]
desc = fav_stats(as.numeric(unlist(BMI)))
