library(dplyr, warn.conflicts = FALSE)
library(tidygeocoder)

# Read the data
data <- read.csv("/home/godwin/Desktop/Geopsy/Geocoding/Accidents_Database - 2017.csv")

# Convert the data to a dataframe
addr <- as.data.frame(data)

# Geocode using the osm method
geocoded_data <- addr %>%
  geocode(address = PLACE, method = 'osm', lat = "latitude", long = "longitude")

# Filter out rows with missing latitude or longitude
geocoded_data <- geocoded_data %>% filter(!is.na(latitude) & !is.na(longitude))

# Save as a CSV file
write.csv(geocoded_data, "/home/godwin/Desktop/Geopsy/Geocoding/Accidents_Database_2017_Geocoded.csv", row.names = FALSE)

