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




