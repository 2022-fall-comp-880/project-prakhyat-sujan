# Cricket Dataset

There are 7 columns in the dataset providing the information about a player from the IPL games.

1. **Player_Id**: The identifier of the player.
2. **Player_Name**: The name of the player.
3. **DOB**: Player's Date of Birth.
4. **Batting_Hand**: Player's baiting hand.
5. **Bowling_Skill**: Player's bowling skill if player bowls.
6. **Country**: Country player plays to.
7. **Is_Umpire**: Binary variable indicating if the player is umpire or not.

## Directories

1. `src` - Contains `main.py` file, which has five classes, `Main` and four other classes for the four tasks.
2. `test` - Contains four test python files for respective four tasks. Each test file contain three test scenarios.
3. `data` - Contains three datasets, `all.csv`, `ten.csv`, `fifty.csv`.


### Who are the Indian players who have no bowling skills with their player ID ?

* Create a class with classname as `Indian_No_Bowling`.
* Create a method `__init__` for initializing the method which can be called 
  automatically and pass the arguments in it and assign it to the object.
* Create a method `get()`. For testing the test cases.
* Create a variable and assign it to an empty list `list[]`.
* Use loop for checking the data in dataset.
* Use if condition for checking the Bowling skill as NULL. Store the players ID
  and Name as a tuple in `result` variable.
* If condition satisfies append it to the list and return the result.

## `test_indian_no_bowling.py`

- Contains three test cases for three data files `all.csv`, `ten.csv`, `fifty.csv`
- Test cases for testing the `get()` method for class `Indian_No_Bowling`.


### Who are the players and their country with batting skill (right hand) and bowling skill as (right arm off break) born between 1980-1990?

* Create a class with classname as `Players`.
* Create a method `__init__` for initializing the method which can be called 
  automatically and pass the arguments in it and assign it to the object.
* Create a method `get()` for the test case players.
* Create a variable for the result and assign it to aan empty `set()`.
* Use loop for checking the data in dataset.
* Use if condition for checking the DOB between 1980 and 1990.
* Give condition which satisfies **Bowling_Skill = Right-Arm offbreak, 
  Bating_Skill = Right_Hand**.
* Store player's name and country as a tuple in `result` set variable.
* Once all the players are looped return the `result`

## `test_players.py`

- Contains three test cases for three data files `all.csv`, `ten.csv`, `fifty.csv`
- Test cases for testing the `get()` method for class `Players`.

