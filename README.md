# ndemo-master
personal website build with django

## setup
The first thing to do is to clone this repository:

>$ git clone https://github.com/ndemo-richard/ndemo-master.git <br />
>$ cd ndemo-master
<br />
create a virtual enviroment to install dependencies in and activate it: <br />

>$ pip install virtualenv <br />
>$ virtualenv env <br />
>$ source env/bin/activate <br />
>$ python manage.py runserver

Then install the dependencies:<br />
> (env)$pip install -r requirements.txt <br />

# Issues I had


#couple of things you should check to fine tune towards your needs
You should change the settings file <br />
uncomment the last line in common.py in settings and the `import django-heroku'
change the database engine to match your settings

#### TODO update this README.md with graphic
#### TODO https://pythonspeed.com/articles/build-secrets-docker-compose/
#### TODO https://www.freecodecamp.org/news/the-docker-handbook/