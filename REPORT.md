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

## Questions
1.Who are the players with right arm medium as bowling skill from player id 1-100?
2.How many right-hand and left-hand batsman in each country?
3. Who are the Indian players with no bowling skills? 
4. Name the players and country with batting skill right hand and bowling 
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

### Question 1:
•	Under `Right_Arm_Medium` class `get()` method answers this query.
•	Limit the players data with the `limit` argument provided.
•	Filter out the players on **Bowling_Skill = Right-Arm medium** and store them in `output` variable.
•	Once the all the players are looped return the `output`.
### Question 2:
•	Under `Count_Batsmen` class `get()` method answers this query.
•	Create a `output` dictionary with country as keys and count of right hand and left hand batsmen as values.
•	Once the all the players are looped return the `output


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

### Driver Class:
* The main class is the driver class in the program which would contain the logic that would invoke the methods in other classes to generate the required outputs.

## Testing
* There are three data sets that are created from the base data. While one data set is named as all.csv which would contain all the data elements, fifty.csv would contain fifty entries out of the entire data set and ten.csv would contain ten entries. The three data sets would have different outputs and the program would be tested by reading each of these data sets and comparing the results with the expected outputs.
    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = RightArmMedium(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = RightArmMedium(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = RightArmMedium(ref)
* We get the list of players with right are medium as bowling skill

        def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        ref_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = CountBatsmen(ref_10)
        ref_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = CountBatsmen(ref_50)
        ref = Main(f"{data_dir}/all.csv").get_data()
        self.tasks_all = CountBatsmen(ref)
* We get count of players right hand and left hand batsmens from each country.


## 3. Result:

> 1. **Question 1:**
> * List of tuples, where tuples have player id's as integers and Player names
    as string.
> * **Result:** list[tuple[int, str]]
>
> 2. **Question 2:**
> * Set of tuples, where tuples have Player_name and Country both as a string.
> * **Result:** set[tuple[Player_name, Country]]

1.class RightArmMedium: The output of this method is a list. The list are the players with right arm medium as bowling skill.
2.class CountBatsmen: The output of this method is a dictionary. The keys of the dictionary are the country and the values are the count of the players.


## Evaluation
### What Works and Scope Assumptions
* Assuming the Dataset we got from kaggle,we are able to analyse the data of the players , which country they belong to, what are there skills .
### Immediate Further Development
* The count and name of the players can be obtained based on bowling skills or batting skills. 
Also, the data can be filtered using both batting and bowling skills together in order to obtain the number of all-rounders belonging to each country





