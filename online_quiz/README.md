# OnlineQuiz Project
This is an online quiz project, 
developed using Python's web framework Django, 
front-end library Bootstrap5 and Postgres database.

## Project features
- User authentication (signup, login, logout)
- Editable profiles for each user, containing their 
avatar, bio, social link, status (contestant or admin), info
about all completed quizzes
- Quizzes containing custom number of questions,
available for all authenticated users, if their status is set to
"public" by admins. When completing a quiz for the first time, each
user gets points according to the number of correct/incorrect/skipped
questions
- Questions with 4 choices and only 1 right answer. Questions may
contain pictures. Time for answering is limited by timer
- Leaderboard which ranks users by score
- Admin Panel, where admins can add/delete/edit quizzes and questions
or change status for any quiz (public/private) - "public" is available
for all users, "private" is seen only by admins

## Dependencies
- Python==3.10.x
- Django==4.0.5
- PostreSQL

## Running the project
1) Clone this repository
```
git clone https://github.com/MrDragon6/TMS_homework/online_quiz.git
cd online_quiz
```
2) Create the virtualenv
```
python3 -m venv .venv
source .venv/bin/activate
```
3) Setup environment variables
```
cp setenv.sh.example setenv.sh
source setenv.sh
```
4) Install common dev dependencies
```
pip3 install -r requirements.txt
pre-commit install
```
5) Start django server
```
cd horeca
pip install .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```