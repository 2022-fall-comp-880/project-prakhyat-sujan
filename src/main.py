"""
main.py file to answer the queries for the Unicorn dataset
"""

import csv


class Players:
    """Players and their country with batting skill (right hand)
    and bowling skill as (right arm off break) born between 1980-1990"""

    def __init__(self, ref) -> None:
        """Method for initializing the dataset."""
        self.ref = ref

    def get(self):
        """
        Checking the Dataset and giving conditions for Batting_skill,
        Bowling_skill and DOB for required test cases.
        :return: set[tuple[Player_name, Country]]
        :rtype: string
        """


class Indian_No_Bowling:
    """Indian players who have no bowling skills."""

    def __init__(self, ref) -> None:
        """Method for initializing dataset."""
        self.ref = ref

    def get(self):
        """
        Checking the dataset and giving conditions for the test case.
        If condition satisfies appending it to the result
        :return: list[tuple[int, Any]]
        :rtype: int and string
        """


class Main:
    """Main class read the CSV and do feature engineering."""

    def __init__(self, file_path) -> None:
        """Giving the path of the dataset."""
        self.file_path = file_path
        self.ref = self.read()

    def get_data(self):
        return self.ref

    def read(self):
        """Reading the dataset."""
        ref = []
        with open(self.file_path, encoding="utf-8", newline="") as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)
            for row in reader:
                ref.append(row)
        return ref


if __name__ == "__main__":
    main = Main("../data/all.csv")
    ref = main.get_data()
    inb = Indian_No_Bowling(ref)
    print("Indian players who have no bowling skills: ", inb.get())
    players = Players(ref)
    print("\nList of Players:")
    print(players.get())
