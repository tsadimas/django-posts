# How to use this repo
* create a folder, let's say myproject
* cd myproject
* create a virtualenv
```
virtualenv -p python3 venv
```
* move into virtual environment and activate it
```
cd venv
source bin/activate
```
* clone this repo
```
git clone https://github.com/tsadimas/django-posts
```
* install the dependencies
```
pip install -r requirements.txt
```

## Use a database backend
* create a file db.json in git root directory, with the following 
```
{
    "NAME": "dbname",
    "USER": "user",
    "PASSWORD": "pass",
    "HOST": "localhost",   
    "PORT": "3306"
}
```

