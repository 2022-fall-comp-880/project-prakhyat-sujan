import unittest
import os
from apps.main import Main, Count_Batsmen


class TestCountBatsmen(unittest.TestCase):
    """Test Count_Batsmen's get() method."""

    def setUp(self):
        """Create Tasks objects for the three test cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = Count_Batsmen(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = Count_Batsmen(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = Count_Batsmen(ref)

    def test_multiple_entries(self):
        """Test case 1 using all.csv."""
        actual_result = self.tasks_all.get()
        expected_result = {
            "India": {"Left_Hand": 61, "Right_Hand": 203},
            "New Zealand": {"Left_Hand": 9, "Right_Hand": 13},
            "Australia": {"Left_Hand": 23, "Right_Hand": 49},
            "Pakistan": {"Left_Hand": 3, "Right_Hand": 10},
            "South Africa": {"Left_Hand": 12, "Right_Hand": 27},
            "Sri Lanka": {"Left_Hand": 8, "Right_Hand": 12},
            "West Indies": {"Left_Hand": 5, "Right_Hand": 14},
            "Zimbabwea": {"Left_Hand": 0, "Right_Hand": 2},
            "England": {"Left_Hand": 2, "Right_Hand": 12},
            "Bangladesh": {"Left_Hand": 3, "Right_Hand": 2},
            "Netherlands": {"Left_Hand": 0, "Right_Hand": 1},
        }
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get()
        expected_result = {
            "India": {"Left_Hand": 11, "Right_Hand": 18},
            "New Zealand": {"Left_Hand": 1, "Right_Hand": 1},
            "Australia": {"Left_Hand": 4, "Right_Hand": 9},
            "Pakistan": {"Left_Hand": 0, "Right_Hand": 1},
            "South Africa": {"Left_Hand": 0, "Right_Hand": 3},
            "Sri Lanka": {"Left_Hand": 2, "Right_Hand": 0},
        }
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get()
        expected_result = {
            "India": {"Left_Hand": 1, "Right_Hand": 3},
            "New Zealand": {"Left_Hand": 0, "Right_Hand": 1},
            "Australia": {"Left_Hand": 0, "Right_Hand": 3},
            "Pakistan": {"Left_Hand": 0, "Right_Hand": 1},
            "South Africa": {"Left_Hand": 0, "Right_Hand": 1},
        }
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
