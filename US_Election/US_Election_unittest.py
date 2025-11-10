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

    #     # Check a reasonable range for sum of votes, or exact value if known
    #     total_votes = state_votes.sum()
    #     self.assertGreater(total_votes, 0)
    #     self.assertLessEqual(total_votes, 1)  # Since fraction votes are fractions
        
    # def test_empty_candidate(self):
    #     # Test with a candidate name not in data, expecting empty series

    #     candidate_name = "nonexistent candidate"
    #     state_votes = US_Election_Graph(candidate_name)

    #     self.assertIsInstance(state_votes, pd.Series)
    #     self.assertTrue(state_votes.empty)

if __name__ == "__main__":
    unittest.main()