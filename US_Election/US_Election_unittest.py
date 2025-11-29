import unittest
import pandas as pd
from US_Election_graph import US_Election_Graph

#This class will test for the US election graph
class TestUSElectionGraph(unittest.TestCase):

    #This function will test for all candidate votes in the csv file
    def test_candidate_votes_sum(self):

        #This is the candidate name which will be given as a test name
        candidate_name="bernie sanders"
        state_votes = US_Election_Graph(candidate_name)

        #These tests will run to see whether the name is in the panda series, if the csv file does not contain the name
        self.assertIsInstance(state_votes,pd.Series)
        self.assertFalse(state_votes.empty)
        self.assertIn('California', state_votes.index)
        self.assertGreater(state_votes.sum(),0)

if __name__ == "__main__":
    unittest.main()