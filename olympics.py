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

#Extracting MMA sports dataset
mma = ["Wrestling", "Boxing", "Judo", "Taekwondo"]
mma_data = data[data.Sport.isin(mma)]

#Creating Gold, Silver, Bronze, and no medal dataframes
gold_data = mma_data[mma_data.Medal == 1]
silver_data = mma_data[mma_data.Medal == 2]
bronze_data = mma_data[mma_data.Medal == 3]
no_medal_data = mma_data[mma_data.Medal == 0]

#Calculating totals for each country
mma_gold = pd.DataFrame(gold_data.groupby('Team')['Medal'].count())
mma_gold = mma_gold.rename(columns={'Medal': 'Gold'})

mma_silver = pd.DataFrame(silver_data.groupby('Team')['Medal'].count())
mma_silver = mma_silver.rename(columns={'Medal': 'Silver'})

mma_bronze = pd.DataFrame(bronze_data.groupby('Team')['Medal'].count())
mma_bronze = mma_bronze.rename(columns={'Medal': 'Bronze'})

mma_no_medal = pd.DataFrame(no_medal_data.groupby('Team')['Medal'].count())
mma_no_medal = mma_no_medal.rename(columns={'Medal': 'NoMedal'})

#Joining MMA Medal Counts
mma_medal_count = pd.merge(mma_gold, mma_silver, on='Team')
mma_medal_count = pd.merge(mma_medal_count, mma_bronze, on='Team')
mma_medal_count = pd.merge(mma_medal_count, mma_no_medal, on='Team')
#mma_medal_count = mma_medal_count.assign(Participants=
                    #mma_medal_count['Gold']+
                    #mma_medal_count['Silver']+
                    #mma_medal_count['Bronze']+
                    #mma_medal_count['NoMedal'])

#Graph
colors = ["gold", "silver", "chocolate", "lightblue"]
mma_sort_data = mma_medal_count.nlargest(15, ['Gold', 'Silver', 'Bronze'])
mma_sort_data.plot(color=colors, kind='barh', stacked=True)
plt.ylabel('Team')
plt.xlabel("Participants")
plt.title("Mixed Martial Arts Olympic History")
plt.show()
