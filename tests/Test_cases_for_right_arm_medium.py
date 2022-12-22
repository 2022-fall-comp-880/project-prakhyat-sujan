README-prakhyat
"""Import all the required modules."""
"""Test methods."""
main
import unittest
import os
from src.main import Main, RightArmMedium


class TestRightArmMedium(unittest.TestCase):
    """Test Right_Arm_Medium get() method."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = RightArmMedium(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = RightArmMedium(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = RightArmMedium(ref)

    def test_multiple_entries(self):
        """Test case 1 using all.csv."""
        actual_result = self.tasks_all.get(100)
        expected_result = [
            "SC Ganguly",
            "BB McCullum",
            "RT Ponting",
            "V Kohli",
            "MV Boucher",
            "P Kumar",
            "ML Hayden",
            "MEK Hussey",
            "MS Dhoni",
            "JR Hopes",
            "T Kohli",
            "SK Trivedi",
            "DJ Thornely",
            "RV Uthappa",
            "AM Nayar",
            "SB Styris",
            "LR Shukla",
            "DPMD Jayawardene",
            "WA Mota",
            "MA Khote",
            "DS Kulkarni",
            "R Vinay Kumar",
            "AM Rahane",
            "TM Srivastava",
            "B Chipli",
            "MK Pandey",
        ]
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get(100)
        expected_result = [
            "SC Ganguly",
            "BB McCullum",
            "RT Ponting",
            "V Kohli",
            "MV Boucher",
            "P Kumar",
            "ML Hayden",
            "MEK Hussey",
            "MS Dhoni",
            "JR Hopes",
            "T Kohli",
            "SK Trivedi",
            "DJ Thornely",
            "RV Uthappa",
            "AM Nayar",
        ]
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get(100)
        expected_result = ['SC Ganguly', 'BB McCullum', 'RT Ponting',
                           'V Kohli']
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
