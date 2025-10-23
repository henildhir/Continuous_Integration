import pandas as pd
import matplotlib.pyplot as plt

US_Election_df = pd.read_csv("US_Election/US-2016-primary.csv",sep=';')
candidate_name='Donald Trump'
state=input("Enter a state you want to look at: ")
candidate_df= US_Election_df[US_Election_df['candidate']==candidate_name]
state_df=candidate_df[candidate_df['state'].str.lower()==state.lower()]

state_df['fraction_votes']=pd.to_numeric(state_df['fraction_votes'],errors='coerce')


plt.figure(figsize=(8,5))

plt.hist(state_df['fraction_votes'].dropna(),bins=30)

plt.xlabel('Fraction of Votes')
plt.ylabel('Number of Counties')
plt.title(f'Distribution of fraction of votes for {candidate_name}')
plt.tight_layout()
plt.show()