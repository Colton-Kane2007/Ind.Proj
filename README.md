# KDA (Emphasis on the 'A'): Predicting Wins In League of Legends
# Project description with goals:
* This is a notebook where I analyze drivers of blue team wins within the dataset from Kaggle. Using the data science pipeline, I grab the data, prepare it, explore it, visualize it, train models on it, and use statistical testing in order to answer questions about the data.


# Initial hypotheses and/or questions I have of the data, ideas:
* The main question I'm asking of the data is 'What are the main drivers of wins' and subsequently 'What can I recommend on what works or doesn't work in predicting wins?'
## Columns I initially suspect to be drivers of blue team win:
* bluefirstblood
* bluekills
* bluedeaths
* blueelitemonsters
* blueexperiencediff
* bluegolddiff
* bluetotalexperience
* bluekilldiff
* blueassistdiff

# Data Dictionary:
|Feature|Dtype, Description|
|:--------|:-----------|
|blueWins|	int64, Number of blue team wins|
|blueWardsPlaced|	int64, Number of blue team wards placed|
|blueWardsDestroyed|	int64, Number of blue team wards destroyed|
|blueFirstBlood|	int64, First kill or not|
|bluekills|	int64, Number of blue team kills|
|bluedeaths|	int64, Number of blue team deaths|
|blueassists|	int64, Number of blue team assists|
|blueelitemonsters|	int64, Number of blue team elite monster kills (herald and dragon)|
|bluedragons|	int64, Number of blue team dragon kills|
|blueheralds|	int64, Number of blue team herald kills|
|bluetowersdestroyed|	int64, Number of blue team towers destroyed|
|bluetotalgold|	int64, Total blue team gold|
|blueavglevel|	float64, Blue team average level|
|bluetotalexperience|	int64, Total blue team experience|
|bluetotalminionskilled|	int64, Total blue team minions killed|
|bluetotaljungleminionskilled|	int64, Total blue team jungle minions killed|
|bluegolddiff|	int64, Difference between blue gold and red gold earned|
|blueexperiencediff|	int64, Difference between blue experience and red experience earned|
|bluecspermin|	float64, Blue team minion kills per minute|
|bluegoldpermin|	float64, Blue team gold per minute|
|redwardsplaced|	int64, Number of red team wards placed|
|redwardsdestroyed|	int64, Number of red team wards destroyed|
|redfirstblood|	int64, First kill or not|
|redkills|	int64, Number of red team kills|
|reddeaths|	int64, Number of red team deaths|
|redassists|	int64, Number of red team assists|
|redelitemonsters|	int64, Number of red team elite monster kills (herald and dragon)|
|reddragons|	int64, Number of red team dragon kills|
|redheralds|	int64, Number of red team herald kills|
|redtowersdestroyed|	int64, Number of red team towers destroyed|
|redtotalgold|	int64, Total red team gold|
|redavglevel|	float64, Red team average level|
|redtotalexperience|	int64, Total red team experience|
|redtotalminionskilled|	int64, Total red team minions killed|
|redtotaljungleminionskilled|	int64, Total red team jungle minions killed|
|redgolddiff|	int64, Difference between red gold and blue gold earned|
|redexperiencediff|	int64, Difference between red experience and blue experience earned|
|redcspermin|	float64, Red team minion kills per minute|
|redgoldpermin|	float64, Red team gold per minute|
|bluekilldiff|	int64, Difference between blue kills and red kills|
|blueassistdiff	|	int64, Difference between blue assists and red assists|

# Project planning:
* Aquire data from Kaggle
 
* Prepare data
   * Create engineered columns from existing data
       * blueassists
       * bluekills
   * Convert all letters to lowercase
   * Set gameid to index
 
* Explore data in search of drivers of blue team wins
   * Answer the following initial questions
       * Are there any surprises in the data?
       * Does a higher KDA (Kill/Death/Assist ratio) lead to higher rate of wins?
       * How often has winning occured compared to losing?
       * Does vision control (wards placed and destroyed) affect win rate?
       * Does whether the team gets the first kill affect win rate?
       * Do elite monster kills affect win rate?
       * Do minion kills affect win rate?
       * Does difference in gold or experience compared to the other team affect win rate?
       * Does gold per minute affect win rate?
      
* Develop a model to predict if a diamond player will win or not based off the first 10 minutes of a game
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data


# Instructions or an explanation of how someone else can reproduce my project and findings (What would someone need to be able to recreate my project on their own?):
* In order to recreate this project, another user would need a similar wrangle.


# Key findings, recommendations, and takeaways from my project:
## My main takeaway: I recommend that players work as a team and focus on getting higher KDA, gold, and XP than opponents to increase win rate. We can use a KNN model with 5 neighbors and uniform weight to predict win off of these features with 78% accuracy.
