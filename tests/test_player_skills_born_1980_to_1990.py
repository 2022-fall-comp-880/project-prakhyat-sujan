"""Test method."""
import unittest
import os
from src.main import Main, Players


class TestPlayers(unittest.TestCase):
    """Test Players's get() method."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = Players(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = Players(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = Players(ref)

    def test_multiple_entries(self):
        """Test case 1 using all.csv."""
        actual_result = self.tasks_all.get()
        expected_result = {
            ("Parvez Rasool", "India"),
            ("AT Rayudu", "India"),
            ("MN Samuels", "West Indies"),
            ("TL Suman", "India"),
            ("Shoaib Malik", "Pakistan"),
            ("M Vijay", "India"),
            ("Sunny Gupta", "India"),
            ("SMSM Senanayake", "Sri Lanka"),
            ("LRPL Taylor", "New Zealand"),
            ("YK Pathan", "India"),
            ("MJ Guptill", "New Zealand"),
            ("R Ninan", "India"),
            ("GJ Maxwell", "Australia"),
            ("SD Chitnis", "India"),
            ("J Botha", "South Africa"),
            ("HM Amla", "South Africa"),
            ("A Chandila", "India"),
            ("Y Venugopal Rao", "India"),
            ("KM Jadhav", "India"),
            ("MB Parmar", "India"),
            ("X Thalaivan Sargunam", "India"),
            ("R Ashwin", "India"),
            ("AA Jhunjhunwala", "India"),
            ("R Sharma", "India"),
            ("Mohammad Ashraful", "Bangladesh"),
            ("SA Asnodkar", "India"),
            ("VS Yeligati", "India"),
            ("RG Sharma", "India"),
            ("BAW Mendis", "Sri Lanka"),
            ("S Randiv", "Sri Lanka"),
            ("MD Mishra", "India"),
        }
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get()
        expected_result = {("YK Pathan", "India")}
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get()
        expected_result = set()
        self.assertEqual(actual_result, expected_result)


if __name__ == "_main_":
    unittest.main()
