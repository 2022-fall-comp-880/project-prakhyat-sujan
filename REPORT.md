# Project Report

## 1. Purpose:

>The purpose of the project is to analyze the data set containing details of
 the players from different countries in order to answer the various 
 questions that are mentioned in the project.

### Working of the Program:
  
> * The dataset is taken from Kaggle, which is open source for the datasets. 
    Harshavardhan is the dataset's author, and it was last updated six years 
    ago. The data set that is used for this project is a set of players that 
    play cricket. There are seven columns in the data set that are associated 
    with the players. Below are the descriptions of the columns in the data set.                            
>* **Player_ID** – This is a unique identification number that is assigned to 
     each player in the data set.
>* **Player_Name** – This column would indicate the name of the players.
>* **DOB**- This column in the data would contain the player's date of birth.
>* **Batting_Hand**- This column would indicate the style of batting of the 
     player. It would contain two values, namely, Right_Hand or Left_Hand.
>* **Bowling_Skill:** This column would indicate the style of the players' 
     bowling. This column contains various values such as Right-arm medium, 
     Right-arm off-break, Right-arm fast-medium, Legbreak googly, etc. The 
     column would also contain NULL values as every player might not bowl in a 
     match.
>* **Country** - This column would contain the name of the country to which a 
     player belongs.
>* **Is_Umpire:** This is a column that would indicate if the player is an 
     umpire or not.

### Questions

> 1. Who are the Indian players with no bowling skills? 
> 2. Name the players and country with batting skill right hand and bowling 
     skill as right arm off-break born between 1980-1990?

## 2. Approach:

### Development of Code:

> * In order to answer the above questions, python language is used to develop 
    the code that could help in data analysis. A total of five classes are used
    to carry out the data analysis, with each of the four classes containing 
    the logic for each of the four questions, and the fifth class is the main 
    class which would call the methods in other classes to generate the 
    required output. Below is the design approach that is followed to answer 
    each of the questions. 
> 
> 
> 1. **Question 1:**
> * Under the `Indian_No_Bowling` class, the `get()` method answers this query.
> * Filter out the players on **Country = India and Bowling_Skill = NULL** and
    store the player's ID and Name as a tuple in the `result` variable.
Once all the players are looped, return the `result.`
> 
> 
> 2. **Question 2:**
> * Under the `Players` class, the `get()` method answers this query.
> * Filter out the players on **Bowling_Skill = Right-Arm off-break, 
    Bating_Skill = Right_Hand, 80 < DOB < 90** and store the player's name and 
    the country as a tuple in the `result` set variable.
> * Once all the players are looped, return the `result.`

## 3. Result:

> 1. **Question 1:**
> * List of tuples, where tuples have player id's as integers and Player names
    as string.
> * **Result:** list[tuple[int, str]]
>
> 2. **Question 2:**
> * Set of tuples, where tuples have Player_name and Country both as a string.
> * **Result:** set[tuple[Player_name, Country]]
