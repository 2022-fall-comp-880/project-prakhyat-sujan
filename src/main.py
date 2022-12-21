"""Import all the required packages."""

import os
import csv


class CountBatsmen:
    """Count of right hand and left hand batsmen from each country."""

    def __init__(self, ref) -> None:
        self.ref = ref

    def get(self):
        """Return the count of left-hand and right hand batsmen of each
        country."""
        output = {}
        for row in self.ref:
            country = row[-3]
            if country not in output:
                output[country] = {"Left_Hand": 0, "Right_Hand": 0}
            if row[3] != "NULL":
                output[country][row[3]] += 1
        return output


class RightArmMedium:
    """Players with right arm medium as bowling skills."""

    def __init__(self, ref) -> None:
        self.ref = ref

    def get(self, limit: int):
        """Return the player name with right arm medium as bowling skill."""
        output = []
        for row in self.ref[:limit]:
            if row[4] == "Right-arm medium":
                output.append(row[1])
        return output


class Players:
    """Players and their country with batting skill (right hand)
    and bowling skill as (right arm off-break) born between 1980-1990."""

    def __init__(self, ref) -> None:
        """Method for initializing the dataset."""
        self.ref = ref

    def get(self):
        """
        Checking the Dataset and giving conditions for Batting_skill.
        Bowling_skill and DOB for required test cases.
        :return: set[tuple[Player_name, Country]]
        :rtype: string
        """
        result = set()
        for row in self.ref:
            if row[2] != 'NULL':
                dob = int(row[2].split("-")[-1])
                if (row[4] == "Right-arm offbreak") and (row[3] == "Right_Hand") and (80 < dob < 90):
                    result.add((row[1], row[-3]))
        return result


class IndianNoBowling:
    """Indian players who have no bowling skills."""

    def __init__(self, ref) -> None:
        """Method for initializing dataset."""
        self.ref = ref

    def get(self):
        """
        Check the dataset and give conditions for the test case.

        If conditions satisfies append it to the result.
        :return: list[tuple[int, Any]]
        :rtype: int and string
        """
        result = []
        for row in self.ref:
            if row[5] == "India" and row[4] == "NULL":
                result.append((int(row[0]), row[1]))
        return result


class Main:
    """Main class read the CSV and do feature engineering."""

    def __init__(self, file_path) -> None:
        """Giving the path of the Dataset."""

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
    path = os.path.dirname(__file__) + "/../data/all.csv"
    main = Main(path)
    ref = main.get_data()
    ram = RightArmMedium(ref)
    print("\nPlayers with right arm medium as bowling skill:")
    print(ram.get(limit=100))
    count_batsmen = CountBatsmen(ref)
    print("\nCount of left and right hand batsmen by country:")
    print(count_batsmen.get())
    main = Main("../data/all.csv")
    ref = main.get_data()
    inb = IndianNoBowling(ref)
    print("Indian players who have no bowling skills: ", inb.get())
    players = Players(ref)
    print("\nList of Players:")
    print(players.get())
