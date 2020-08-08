####RESTful APIs app with Flask and SQLAlchemy ORM

Experimenting with creating a RESTful APIs app 
using the Flask micro-framework and SQLAlchemy

In the journey to learn and develop my knowledge as an inspiring data engineer,
I wanted to learn how to use ORM. ORM(Object Relational Mapping) is an excellent way to bridge the gap between traditional databases and code.
To accomplish this, I decided to use Flask and SQLAlchemy
to create this RESTful API app. 

**Setup** <br>
* The packages needed for this app can be installed by using the requirements.txt file.<br>
         
        $ pip install -r requirements.txt
         
* I used a .env file for storing configuration variables like the database user and password.
To access these variables I used the dotenv python package.
In the repo, you can find a .env(template) file with a template to the configuration variables that I used.
    
        $ pip install -U dotenv
        ------------------------------
        >> from dotenv import load_dotenv
        >> load_dotenv()

**References** <br>
 [SQLAlchemy](https://www.sqlalchemy.org/) <br>
 [Flask](https://flask.palletsprojects.com/) <br>
 [dotenv](https://pypi.org/project/python-dotenv/) <br>
 [Flask RESTPlus](https://flask-restplus.readthedocs.io/)
