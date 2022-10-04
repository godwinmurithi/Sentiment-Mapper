import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import 

#Set PANDAS to show all columns in DataFrame
pd.set_option('display.max_columns', None)

import calendar
import matplotlib.pyplot as plt
#NECESSARY FOR XTICKS OPTION, ETC.
from pylab import*
%matplotlib inline  

import seaborn as sns
print sns.__version__

#The following line will set the default plots to be bigger.
plt.rcParams['figure.figsize'] = (15, 5)


#Version 1.4 of matplotlib enables specific plotting styles
import matplotlib as mpl

#check styles available
mpl.style.available

#We can use the len function again here to see how many columns there are in the dataframe: 54.
len(df.columns)


#And we can see what types of variable each column is -- an integer (int64), a numerical float variable (float), or a text variable (object).
df.dtypes

#To work with time, we first have to have a variable in our dataframe that indicates time
df['created_at'] = pd.to_datetime(df['created_at'])

#One thing you'll have to frequently do in PANDAS is set an index to your dataframe.
df['created_at']=pd.to_datetime(df['created_at'], unit='s')
df.head(2)

#Generate and Plot Number of Tweets over Different Time Periods
def f(x):
     return Series(dict(Number_of_tweets = x['text'].count(), 
                        ))
#Generate and Plot Daily Counts
daily_count = dg.groupby(dg.index.date).apply(f)
print(daily_count)
daily_count.head(5)

#Let's give a name to this index and then inspect the first five rows in the dataframe.
daily_count.index.name = 'date'
daily_count.head(5)

#Let's now look at the last five rows of the dataframe.
daily_count.tail(5)

#Let's run two more lines of code to see what the minimum and maximum daily values are in the dataset.
daily_count.index.min()
daily_count.index.max()


#Perfect. We're all set. Now let's plot it.
daily_plot = daily_count['Number_of_tweets'].plot(kind='line', lw=1, alpha=0.75, legend=True, x_compat=True)

daily_plot.set_xlabel('Month', weight='bold', labelpad=15)    #SET X-AXIS LABEL; ADD PADDING TO TOP OF LABEL
daily_plot.set_ylabel('# Tweets (Messages)', weight='bold', labelpad=15) #SET Y-AXIS LABEL; ADD PADDING TO RIGHT OF LABEL

xticks(fontsize = 9, rotation = -30, ha ="left")  #SET FONT PROPERTIES OF X-AXIS TICK LABELS
yticks(fontsize = 9)                              #SET FONT PROPERTIES OF Y-AXIS TICK LABELS

#http://matplotlib.org/users/legend_guide.html
#http://nbviewer.ipython.org/gist/olgabot/5357268  ### LIST OF OPTIONS
#legend(fontsize='x-small',loc=2,labelspacing=0.1, frameon=False)#.draggable()
daily_plot.legend_ = None
daily_plot.tick_params(axis='x', pad=5) #SET PADDING ABOVE X-AXIS LABELS
#Set x axis label on top of plot, set label text --> https://datasciencelab.wordpress.com/2013/12/21/beautiful-plots-with-pandas-and-matplotlib/
#daily_plot.xaxis.set_label_position('top')

savefig('daily counts.png', bbox_inches='tight', dpi=300, format='png')   #SAVE PLOT IN PNG FORMAT
