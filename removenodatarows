#read the data
data <- read.csv("raw_data130.csv")

#select the location column and remove null rows
new_DF<-subset(data, data$author_location!="")
geocode

#save as a csv file
write.csv(new_DF, file = "raw_data131.csv")
