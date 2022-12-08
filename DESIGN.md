
# Cricket Dataset
=======
## COLLABORATORS : SUJAN VARMA & PRAKYATH BOMMANA

## `main.py`

This is the main file for the application. It contains a series of functions and methods to process the data.

### Main Class

- `read()` method reads the csv file as a list of lists and store in `ref` variable.
- `get_data()` method returns the above `ref` variable.

### Who are the players with right arm medium as bowling skill within the limit provided?

- Under `Right_Arm_Medium` class `get()` method answers this query.
- Limit the players data with the `limit` argument provided.
- Filter out the players on **Bowling_Skill = Right-Arm medium** and store them in `output` variable.
- Once the all the players are looped return the `output`.

### Count of right hand and left hand batsmen from each country?

- Under `Count_Batsmen` class `get()` method answers this query.
- Create a `output` dictionary with country as keys and count of right hand and left hand batsmen as values.
- Once the all the players are looped return the `output`.

## Test Cases

## `test_count_batsmen.py`

- Contains three test cases for three data files `all.csv`, `ten.csv`, `fifty.csv`
- Test cases for testing the `get()` method for class `Count_Batsmen`.

## `test_right_arm_medium.py`

- Contains three test cases for three data files `all.csv`, `ten.csv`, `fifty.csv`
- Test cases for testing the `get()` method for class `Right_Arm_Medium`.





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

