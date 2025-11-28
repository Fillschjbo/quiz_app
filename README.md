# Quiz Game

## Project Description
This is a console-based Trivia Quiz Game written in Python. The game loads questions from a data source (originally a JSON file, later migrated to MySQL), presents them to the user with multiple-choice options, tracks the score, and displays final results with statistics. The project demonstrates object-oriented design, file/database handling, error management, and team-based software development practices.

## Team Members
- Truls Johan
- Fillip Husebø

## Install/Usage Instructions

### Installation
1. Clone this repository:
   ```bash
   git clone git@github.com:Fillschjbo/quiz_app.git
2. Install the packages:
   ```bash
   pip install mysql-connector-python python-dotenv
3. Run the init.sql file in order to create the quiz_db.
4. Run the insert.py file in order to import the data from question.json, into the quiz_db.
5. Now you can run app.py to play the quiz game.

In a real setting, you would also have to add a .env file and fill inn the correct info.
You would also have to sett the password to match in the init.sql file.

### Usage
1. To start the quiz, you can simply run the app.py file after doing the installation steps above.
2. Then you will see a game menu in the console where you choose between game 1-5 or mixed quiz(m).
3. After you select game, you can answer the quiz questions in the console by the corresponding letter(a-d).
4. Then at the end of the quiz, you will get a score board and a list of the questions with the correct answers.


## Members Contribution & Reflection

### Truls Contributions
- app.py: main_menu() and show_results()
- Both did 50/50 on insert.py
- .env
- Readme.md

### Fillip Contributions
- app.py: Connect() and question_loop()
- Both did 50/50 on insert.py
- init.sql

### Team Reflection
We think this project was interesting, as we needed to combine all the things we learned so far.
On the other hand, maby not the best tasks for a group project. In order for both 
to partake in the same task, we had to split the task in different functions. This can be a bit
challenging as it can lead to merge conflicts. It also makes the other person dependent on you finishing your task
before continuing. In other words maby a bit "stagnated". Fortunately we both worked efficiently, so it worked itself
out nicely.

Despite the things mentioned above, it went very smooth as a team. We communicated well, and both
contributed to the task. Maby there is a better way for us to divide the tasks so it don´t feel so "stagnant", but
it worked out ether way. We also have prior experience working together, witch probably helps as well.
To sum it up, I think we did a good job and both did their part:)

## Acknowledgments
- questions.json file form Gokstad Akademiet



