"""Import all the required modules."""
import unittest
import os
from src.main import Main, IndianNoBowling


class TestIndianNoBowling(unittest.TestCase):
    """Test Indian_No_Bowling's get() method."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = IndianNoBowling(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = IndianNoBowling(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = IndianNoBowling(ref)

    def test_multiple_entries(self):
        """Test case 1 using all.csv."""
        actual_result = self.tasks_all.get()
        expected_result = [
            (17, "PA Patel"),
            (36, "M Rawat"),
            (47, "PR Shah"),
            (62, "WP Saha"),
            (79, "SS Tiwary"),
            (88, "KD Karthik"),
            (114, "YV Takawale"),
            (123, "DT Patil"),
            (125, "S Anirudha"),
            (132, "SP Goswami"),
            (134, "U Kaul"),
            (138, "NK Patel"),
            (146, "H Das"),
            (183, "NV Ojha"),
            (207, "AP Tare"),
            (214, "MS Bisla"),
            (251, "C Madan"),
            (252, "AG Paunikar"),
            (260, "MA Agarwal"),
            (277, "DH Yagnik"),
            (319, "N Saini"),
            (327, "BB Samantray"),
            (351, "SV Samson"),
            (354, "KL Rahul"),
            (360, "CM Gautam"),
            (410, "Ishan Kishan"),
            (419, "NS Naik"),
            (420, "RR Pant"),
            (433, "ER Dwivedi"),
            (466, "P Dharmani"),
            (468, "KH Devdhar"),
            (479, "AV Jayaprakash"),
            (483, "S Asnani"),
            (485, "SS Hazare"),
            (486, "K Hariharan"),
            (487, "SL Shastri"),
            (488, "SK Tarapore"),
            (489, "S Ravi"),
            (491, "S Das"),
            (492, "AM Saheba"),
            (495, "AK Chaudhary"),
            (496, "VA Kulkarni"),
            (498, "CK Nandan"),
            (499, "C Shamshuddin"),
            (502, "RM Deshpande"),
            (503, "K Srinath"),
            (506, "PG Pathak"),
            (507, "Nitin Menon"),
            (508, "K Bharatan"),
            (509, "AY Dandekar"),
            (510, "KN Ananthapadmanabhan"),
            (511, "A Nand Kishore"),
            (512, "GA Pratapkumar"),
            (514, "I Shivram"),
            (515, "SD Ranade"),
            (519, "Subroto Das"),
            (520, "K Srinivasan"),
            (521, "VK Sharma"),
            (523, "AV Wankhade"),
        ]
        self.assertEqual(sorted(actual_result), sorted(expected_result))

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get()
        expected_result = [(17, "PA Patel"), (36, "M Rawat"), (47, "PR Shah")]
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get()
        expected_result = []
        self.assertEqual(actual_result, expected_result)


if __name__ == "_main_":
    unittest.main()
