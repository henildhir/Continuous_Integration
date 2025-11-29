import unittest
import pandas as pd
from US_Election_graph import US_Election_Graph

class TestUSElectionGraph(unittest.TestCase):

    def test_candidate_votes_sum(self):

        candidate_name="bernie sanders"
        state_votes = US_Election_Graph(candidate_name)

        self.assertIsInstance(state_votes,pd.Series)
        self.assertFalse(state_votes.empty)
        self.assertIn('California', state_votes.index)
        self.assertGreater(state_votes.sum(),0)

if __name__ == "__main__":
    unittest.main()