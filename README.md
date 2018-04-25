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

## Deploy to gCloud

#### install gunicorn
```
pip install gunicorn
```

#### install [google cloud sdk](https://cloud.google.com/sdk/downloads)

* set up STATIC_ROOT, ALLOWED_HOSTS in settings.py

```
ALLOWED_HOSTS = [
    os.environ['DEPLOY_HOST'],
    '127.0.0.1',
]
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```
* create a file named _app.yaml_ in project root directory

sample file:
```
entrypoint: gunicorn -b :$PORT postsproject.wsgi
env: flex
runtime: python

env_variables:
  DEBUG: 'False'
  DEPLOY_HOST: "XXXXXXXXX.appspot.com"

handlers:
- url: /static
  static_dir: static
```
* run 
```
python manage.py collectstatic
```
#### gcloud init
Run 
```
gcloud init 
```
select your gcloud account and your project
Run
```
gcloud app deploy
```
see your app with
```
gcloud app browse
```

Links:
* [Beginner’s Guide to Deploying a Django + PostgreSQL project on Google Cloud’s Flexible App Engine](https://codeburst.io/beginners-guide-to-deploying-a-django-postgresql-project-on-google-cloud-s-flexible-app-engine-e3357b601b91)
* [Running Django on App Engine Standard Environment](https://cloud.google.com/python/django/appengine)