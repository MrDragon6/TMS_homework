## Work with python only in virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
## Setup environment variables
```
cp setenv.sh.example setenv.sh
source setenv.sh
```

## Install common dev dependencies
```
pip3 install -r requirements.txt
pre-commit install
```

## Start django server
```sh
cd horeca
pip install .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```

## Prod setup
```sh
python manage.py collectstatic
```
