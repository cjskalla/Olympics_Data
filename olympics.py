#OLYMPICS
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#Reading in the data
data = pd.read_csv("data/athlete_events.csv")
obs_per_sport = data['Sport'].value_counts()

#Mapping the medal column to numeric codes for classifying
medal_mapping = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 0: 0}
data['Medal'] = data['Medal'].fillna(0)
data['Medal'] = data['Medal'].map(medal_mapping)

#Extracting martial_art sports dataset
martial_art = ["Wrestling", "Boxing", "Judo", "Taekwondo"]
martial_art_data = data[data.Sport.isin(martial_art)]

#Creating Gold, Silver, Bronze, and no medal dataframes
gold_data = martial_art_data[martial_art_data.Medal == 1]
silver_data = martial_art_data[martial_art_data.Medal == 2]
bronze_data = martial_art_data[martial_art_data.Medal == 3]
no_medal_data = martial_art_data[martial_art_data.Medal == 0]

#Calculating totals for each country
martial_art_gold = pd.DataFrame(gold_data.groupby('Team')['Medal'].count())
martial_art_gold = martial_art_gold.rename(columns={'Medal': 'Gold'})

martial_art_silver = pd.DataFrame(silver_data.groupby('Team')['Medal'].count())
martial_art_silver = martial_art_silver.rename(columns={'Medal': 'Silver'})

martial_art_bronze = pd.DataFrame(bronze_data.groupby('Team')['Medal'].count())
martial_art_bronze = martial_art_bronze.rename(columns={'Medal': 'Bronze'})

martial_art_no_medal = pd.DataFrame(no_medal_data.groupby('Team')['Medal'].count())
martial_art_no_medal = martial_art_no_medal.rename(columns={'Medal': 'NoMedal'})

#Joining martial_art Medal Counts
martial_art_medal_count = pd.merge(martial_art_gold, martial_art_silver, on='Team')
martial_art_medal_count = pd.merge(martial_art_medal_count, martial_art_bronze, on='Team')
martial_art_medal_count = pd.merge(martial_art_medal_count, martial_art_no_medal, on='Team')
#martial_art_medal_count = martial_art_medal_count.assign(Participants=
                    #martial_art_medal_count['Gold']+
                    #martial_art_medal_count['Silver']+
                    #martial_art_medal_count['Bronze']+
                    #martial_art_medal_count['NoMedal'])

#Graphs
colors = ["gold", "silver", "chocolate", "lightblue"]
martial_art_sort_data = martial_art_medal_count.nlargest(15, ['Gold', 'Silver', 'Bronze'])
martial_art_sort_data.plot(color=colors, kind='barh', stacked=True)
plt.ylabel('Team')
plt.xlabel("Participants")
plt.title("Olympic Martial Arts History")
plt.show()
