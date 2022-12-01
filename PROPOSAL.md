# Data analysis of Cricket players

**Author**: Sujan Varma & Sai Prakhyat Bommana
**Date**: 11/30/2022


## Motivation 

In this project we pick players dataset from kaggle(https://www.kaggle.com/datasets/harsha547/indian-premier-league-csv-dataset?select=Player.csv)
we try to analyse their skills, country, date of birth, and their id of all the players from 2008-2022 ipl matches ,This program makes us
analyse the data and makes easy to fetch the details of the player by the given following input.


## Investigative Questions 


### Who are the indian players with no bowling skills ?

### Who are the players with right arm medium as bowling skill from player id 1-100?

### What are the skills(Bowling & Batting skill) of given player name?

### What is the players date of birth and country?



## Approach 

* In this project I am taking a Dataset from Kaggle an open source for datasets.In this project I am preparing the Test Cases based on the information and 
  writing logical code for those test cases to work properly by applying the python concepts such as Dictionaries, lists, Functions, Classes and Methods, 
  File Handling concepts. The data set contains the PLayer ID, PLayer Name, Bowling skill, Batting skill. 

## Expected Results 

* For the first investigative question we get a dictionary of the dataset where
  player name as a key, and list of bowling skill and player id as the values 
  of the dictionary. 
* For the second investigative question we get a dictionary where right arm 
  medium (bowling skill) as a key and list of player name and player-id as the 
  values of the dictionary. 
* For the third investigative question we get a dictionary where player name as
  a key and list of batting skill and bowling skill as the values of the 
  dictionary.
* For the fourth investigative question we get a dictionary where player name 
  as the key and list of DOB and Country as the values of the dictionary.


## New Python Packages or Modules 

* Import unittest
* Import os
* Import csv

## Dataset Documentation

* The data set is taken from kaggle which is an open source for datasets.
* The Dataset contains attributes Player Names, Player ID's, DOB, Country, 
  Batting Skill and Bowling Skill. 
* The Data set contains 524 rows and 7 columns.
* This Dataset was posted by HARSHAVARDHAN.
* It was updated 6 years ago.
* The size of the Dataset is 32KB.
* https://www.kaggle.com/datasets/harsha547/indian-premier-league-csv-dataset?select=Player.csv

