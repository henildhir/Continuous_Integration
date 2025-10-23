#imported all functions needed for this function
import pandas as pd
import matplotlib.pyplot as plt

#assigned a dataframe variable to read csv file with seperators as ;
US_Election_df = pd.read_csv("US_Election/US-2016-primary.csv",sep=';')

#asks for a candidate name and filtered the dataframe to show only the candidate chosen
candidate_name=input("Enter a candidate: ")
candidate_df= US_Election_df[US_Election_df['candidate'].str.lower()==candidate_name.lower()]

#groups the candidate dataframe by state first then adds all the fraction votes together
state_votes = candidate_df.groupby('state')['fraction_votes'].sum()

#this plots a bar graph of state on the x axis and fraction of votes on the y axis with the candidate name being at the title
plt.figure(figsize=(8,5))
state_votes.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('fraction of votes')
plt.title(f'Distribution of fraction of votes for {candidate_name}')
plt.tight_layout()
plt.show()