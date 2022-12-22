## Questions
1.Who are the players with right arm medium as bowling skill from player id 1-100?
2.How many right-hand and left-hand batsman in each country?

### Question 1:
•	Under `Right_Arm_Medium` class `get()` method answers this query.
•	Limit the players data with the `limit` argument provided.
•	Filter out the players on **Bowling_Skill = Right-Arm medium** and store them in `output` variable.
•	Once the all the players are looped return the `output`.
### Question 2:
•	Under `Count_Batsmen` class `get()` method answers this query.
•	Create a `output` dictionary with country as keys and count of right hand and left hand batsmen as values.
•	Once the all the players are looped return the `output

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

### Results 
1.class RightArmMedium: The output of this method is a list. The list are the players with right arm medium as bowling skill.
2.class CountBatsmen: The output of this method is a dictionary. The keys of the dictionary are the country and the values are the count of the players.
    

## Evaluation
### What Works and Scope Assumptions
* Assuming the Dataset we got from kaggle,we are able to analyse the data of the players , which country they belong to, what are there skills .
### Immediate Further Development
* The count and name of the players can be obtained based on bowling skills or batting skills. 
Also, the data can be filtered using both batting and bowling skills together in order to obtain the number of all-rounders belonging to each country
