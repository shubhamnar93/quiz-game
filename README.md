This code is of true false quiz game where quetions is generated with the help of open trivia api. The different components of project are:

1. `data.py`: it contain the data extracted from api

2. `main.py`: it contain `question_bank` list which contains only questions and answers from data extracted from api ,it passes `question_bank` list to `QuizzBrain` class and `QuizzBrain` to `QizzUI` class

3. `question_bank.py`: helps the main.py to get the data in question_bank

4. `quizz_brain.py`: it coantains `still_has_question` method when there is question left it returs ture else it returns false, `next_question` method it returns next question whenever it is called in the form f string containing question number, `check_answer` method which checks that user_answer matches the correct answer and return true it does matches else false

5. `ui.py`: it contains entire window setup including `label`,`canvas` and `button`, it calls `check_question` from quizz_brain and passes true or false as string based on the button clicked it also convert the canvas backgroug color to green or red based of wrong and right answers and it also calls `still_has_quetion` after 1 sec delay to check wheter there is more queston or not if there is more question it calls `next_question` to display next question on canvas and if there is no more question it shows 'the end' text on the canvas and disable both the buttons 




https://github.com/user-attachments/assets/dde10fd9-0988-421a-bc0d-8ed76740652f

