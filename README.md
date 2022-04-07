<h1>DonationHub</h1>
Team: Anshika Patel, Amy Phan, and Parth Patel.

## Introduction:

DonationHub strives to increase efforts to help out the people in need with various sorts of donations and aid programs. Assuming this is a real company client, DonationHub has requested us a new statistical webpage integration for their audience to view. They want a similar statistical dashboard as Feeding America’s [data page](https://www.google.com/url?sa=D&q=https://map.feedingamerica.org/%3F_ga%3D2.10632375.2037159941.1647393264-2115671929.1647393264&ust=1648349280000000&usg=AOvVaw2dKWdVCliQINm6QsQwM_M2&hl=en&source=gmail). However, DonationHub will include various data including population information of counties and states, rates of poverty and homelessness, list of official donation organizations and charities, and personal income info on a county level. More specifically, DonationHub will show data of each state and county in the United States and display the appropriate data categories for each. Additionally it will allow the user to filter through the data and have it calculate statistical data for them to view.

## Data Set Sources:


**Income**
- https://www.bea.gov/data/income-saving personal-income-county-metro-and-other-areas
- [Example-Dataset-file-provided](https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas)

**Unemployment + Poverty/homelessness Info**
- [Unemployment](https://docs.google.com/spreadsheets/d/1OZzh2ByZRDAfWtM55pKj4VhBUfwvjn1z/edit?usp=sharing&ouid=117748847086221195801&rtpof=true&sd=true)
- [Poverty Estimate + Percentage](https://www.census.gov/data/datasets/2017/demo/saipe/2017-state-and-county.html)

**List of U.S. Charities**
- [Example-dataset-file-provided](https://www.kaggle.com/crawford/us-charities-and-nonprofits?select=eo2.csv)

**State and country population (make sure to only include 2017 population num)**
- [State](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html)
    - state_FIPS, only 2 characters long (first 2 num the 5 digit code (if state_FIPS and county_FIPS are combined))
- [County - overall](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html)
- [County - dataset 2017](https://drive.google.com/file/d/15A4ZxKIeYrG7b28WTACp8liX7oCviimu/view?usp=sharing)
    - (STATE (2 digits) + COUNTY (3 digits) columns = 5 digit code (what we will use for <i>county_FIPS</i>, otherwise we will have duplicates)

## Project Installations
<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://d2knvm16wkt3ia.cloudfront.net/assets/svg-icon/flask.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/><a href="https://www.sqlite.org/index.html" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" alt="sqlite" width="40" height="40"/> </a> </a></p>

(HTML5/CSS3/Bootstrap/Flask/Python/SQLite)

## Installation:

Go to our GitHub page and export our project files (clone/downloading the zip) into a workspace folder: 

https://github.com/UMBC-CMSC461-SP2022/project-donationshub 
 
Through terminal (or VSCode’s terminal), move into the workspace folder. From there, you can do the following steps to install the virtual environment and the rest of the dependents. From there you should be able to run the site: 

### Flask and Python

<i>To learn more about Flask, [here](https://www.askpython.com/python-modules/flask/create-hello-world-in-flask) is a tutorial of how to setup and create a Hello World app in flask (This is not required for this project, but will help you understand flask).</i> Otherwise just ignore and follow the next few steps to install + setup for this project. 

If you're using Vscode,  please install the <i>sqlite</i> extension for better view of the database tables.

**Windows:**

1. Install python 3.6, which should come with pip. Follow the installation instructions and check if it’s correctly installed by typing: 
```
py –version 
```
2. Install and set up a virtualenv: 
```
py –m pip install virtualenv 
py –m venv venv 
. venv\scripts\activate
```

3. Install the extensions 
```
py -m pip install flask 
py -m pip install flask-sqlalchemy 
py -m pip install requests 
```

4. Once you’ve installed these dependents, create a flask command that will be used to specify how to load the application (assuming you’re using bash, otherwise check out the flask site): 
```
set FLASK_APP=app.py 
flask run 
```
(Make sure you’re within the DonationHub folder that has app.py)

5. You should be able to run and open the application now. 

6. To deactivate the virtual environment, just type:
```
deactivate
```

**Mac:**

***Notice: Mac OS uses an older version of python, so you want to change it to at least python 3.6+ if you are unable to use the pip command***

1. Install Python 3.6+ which should come with pip. If you have python installed, check the version by typing:
```
python --version
```

If it lists out a python version less than 3.6+, then check out this page and follow the steps:
    https://stackoverflow.com/questions/1687357/updating-python-on-mac


2. Instal and activate virtualenv to check if you have correctly downloaded it:
```
python3 -m pip install virtualenv
python3 -m venv <name of environment>
source <name of environment>/bin/activate
```

3. Once you've entered your virtualenv, do the following in the command line 

```
python -m pip install flask
python -m pip install flask-sqlalchemy
python -m pip install requests
```
4. Once you've installed these dependents, create a flask command that will be used to specify how to load the application <i>(assuming you're using bash, otherwise check out the [flask site](https://flask.palletsprojects.com/en/2.0.x/cli/)</i>:
```
export FLASK_APP=app.py
flask run
```
(Make sure you’re within the DonationHub folder that has app.py)

5. You should be able to run and open the application now.

6. To deactivate the virtual environment, just type:
```
deactivate
```

## Q&A

(Unfinished)

1. SQLite Extension

    https://youtu.be/bKixKfb1J1o

    tutorial

    https://youtu.be/IBgWKTaG_Bs

## Importing Data into the Database

(Unfinished)

N/A

## Table functions

(Unfinished)

https://youtu.be/IsuhCAptNbg 

####

