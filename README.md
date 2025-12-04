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

In a real setting, you would also have to add a .env file and fill in the correct info.
You would also have to set the password to match in the init.sql file.

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

### Truls Reflection
I think this was a good opportunity to get some experience working with backend as a team.
The task went really well, and we managed to collaborate in an efficient way. For the first task, I made
the main game menu in the console. It makes an array of questions from the question.json file and displays them
in the console as "game 1" and so on. It also allows for the user to select a mixed question quiz. I also made
"show results", where you get your total score and the questions you got wrong. This went quite well, although I had to make
some adjustment so it would work smoothly with Fillip´s code. The .env file was quick and easy to implement, and added it to the gitignore file.
The insert fie also went quite smoothly, but had some problems with my interpreter. It was luckily a quick fix.
At the end I made the Readme.md file, with installation, usage instructions and so on. All in all, it when very well I think.
Both me and Fillip was already familiar with git, witch made the collaboration process very easy. 

### Fillip Contributions
- app.py: Connect() and question_loop()
- Both did 50/50 on insert.py
- init.sql

### Fillip reflection
This project went relatively smoothly, and with no major hiccups. My Role in the project was to create the database and stored procedures,
connect the app to the database, display the questions and answers, the user input for answers and store the answers data for
the results function. The database is set up to match the questions.json file, to make migration as simple as possible. It is
comprised of a games table and a questions table. The app takes the game ID to get the requested game and then loops through and displays the questions
one by one. It then appends an array that stores the question, the option answered, and the correct answer for later use.
The app was first made to work with the provided JSON file, and was then converted to be used with the SQL database.
I am overall pleased with how the final product came out, and with the collaboration with my team member, Truls. We are both familiar
with using git and working on projects as a team, which significantly simplified our collaboration.

### Team Reflection
We think this project was interesting, as we needed to combine all the things we learned so far.
On the other hand, maybe not the best tasks for a group project. In order for both 
to partake in the same task, we had to split the task into different functions. This can be a bit
challenging as it can lead to merge conflicts. It also makes the other person dependent on you finishing your task
before continuing. In other words maybe a bit "stagnated". Fortunately we both worked efficiently, so it worked itself
out nicely.

Despite the things mentioned above, it went very smoothly as a team. We communicated well, and both
contributed to the task. Maybe there is a better way for us to divide the tasks so it doesn´t feel so "stagnant", but
it worked out either way. We also have prior experience working together, which probably helps as well.
To sum it up, we think we did a good job and both did their part:)

## Acknowledgments
- questions.json file from Gokstad Akademiet



