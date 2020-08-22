#OLYMPICS
import pandas as pd 
import numpy as np 

#Reading in the data
data = pd.read_csv("data/athlete_events.csv")
obs_per_sport = data['Sport'].value_counts()

#Medal mapping for classifications
pd.get_dummies(data, columns=['Sex', 'Medal'])