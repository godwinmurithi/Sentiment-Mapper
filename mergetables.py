import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("raw_data*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

# View columns
df.columns

# Drop/Delete unnecessary columns
df.drop(["author_id", "author_followers", "author_tweets", "author_description", 
        "retweets", "replies", "likes", "quote_count", "place_id", "licence", 
        "osm_type", "display_name", "class", "type", "importance", "icon"], 
        axis=1, inplace=True)

# View Columns
df.columns

# Save the cleaned data frame as csv
pd.read_csv("tweetsdata0.csv")
