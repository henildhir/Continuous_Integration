#imported all functions needed for this function
import pandas as pd
import matplotlib.pyplot as plt
import os


def US_Election_Graph(candidate_name):
    #assigned a dataframe variable to read csv file with seperators as ;
    US_Election_df = pd.read_csv("US_Election/US-2016-Primary.csv",sep=';')

    #asks for a candidate name and filtered the dataframe to show only the candidate chosen
    #candidate_name=input("Enter a candidate: ")

    candidate_df= US_Election_df[US_Election_df['candidate'].str.lower()==candidate_name.lower()]

    while candidate_df.empty:
        candidate_name = input(f"No data found for candidate '{candidate_name}'. Please enter a valid candidate name: ")
        candidate_df = US_Election_df[US_Election_df['candidate'].str.lower() == candidate_name.lower()]
    #groups the candidate dataframe by state first then adds all the fraction votes together
    state_votes = candidate_df.groupby('state')['fraction_votes'].sum()

    #this plots a bar graph of state on the x axis and fraction of votes on the y axis with the candidate name being at the title
    plt.figure(figsize=(8,5))
    state_votes.plot(kind='bar')

    #this creates the x and y axis and gives them each a name
    plt.xlabel('State')
    plt.ylabel('fraction of votes')
    plt.title(f'Distribution of fraction of votes for {candidate_name.title()}')
    plt.tight_layout()
    plt.show()

    #Returns the function
    return state_votes


print("Current working directory:", os.getcwd())
candidate_name=input("Enter a candidate: ")
US_Election_Graph(candidate_name)