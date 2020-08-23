#OLYMPICS
import pandas as pd 
import numpy as np 

#Reading in the data
data = pd.read_csv("data/athlete_events.csv")
obs_per_sport = data['Sport'].value_counts()

#Mapping the medal column to numeric codes for classifying
medal_mapping = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 0: 0}
data['Medal'] = data['Medal'].fillna(0)
data['Medal'] = data['Medal'].map(medal_mapping)

#Extracting MMA sports dataset
mma = ["Wrestling", "Boxing", "Judo", "Taekwondo", "Weightlifting"]
mma_data = data[data.Sport.isin(mma)]

#Grouping Countries Medal Counts
mma_data.groupby('Team')['Medal'].unique()

#Bargraph
#bar = data.plot.bar(x='Team', y='Medal', rot=0)

