<h1>DonationHub</h1>
Team: Anshika Patel, Amy Phan, and Parth Patel.

### Introduction:
DonationHub, a new statistical webpage, is similar in nature to statistical dashboard produce by Feeding America's [data page](https://www.google.com/url?sa=D&q=https://map.feedingamerica.org/%3F_ga%3D2.10632375.2037159941.1647393264-2115671929.1647393264&ust=1648349280000000&usg=AOvVaw2dKWdVCliQINm6QsQwM_M2&hl=en&source=gmail). DonationHub webpage includes various data such as population information of counties and states, rates of poverty and homelessness, list of official donation organizations and charities, and personal income info on a county level. More specifically, DonationHub will show data of each state and county in the United States and display the appropriate data categories for each. Additionally it will allow the user to filter through the data and have it calculate statistical data for them to view.

## Data Set Sources:

**Income**
- https://www.bea.gov/data/income-saving personal-income-county-metro-and-other-areas
- https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas
- Example-Dataset-file-provided: https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas 

**Unemployment + Poverty/homelessness Info**
- https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas
- [Example-dataset-file-provided](https://docs.google.com/spreadsheets/d/1OZzh2ByZRDAfWtM55pKj4VhBUfwvjn1z/edit?usp=sharing&amp;ouid=117748847086221195801&amp;rtpof=true&amp;sd=true)

**List of U.S. Charities**
- [Example-dataset-file-provided](https://docs.google.com/spreadsheets/d/1OZzh2ByZRDAfWtM55pKj4VhBUfwvjn1z/edit?usp=sharing&amp;ouid=117748847086221195801&amp;rtpof=true&amp;sd=true)

**State and country population**
- state: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html 
- County:https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html

## Project Installations
<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**
<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://d2knvm16wkt3ia.cloudfront.net/assets/svg-icon/flask.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a></p>

(HTML5/CSS3/Bootstrap/Flask/Python)

## Installation:

Go to our GitHub page and export our project files (clone/downloading the zip) into a workspace folder: 

https://github.com/UMBC-CMSC461-SP2022/project-donationshub 
 
Through terminal (or VSCode’s terminal), move into the workspace folder. From there, you can do the following steps to install the virtual environment and the rest of the dependents. From there you should be able to run the site: 

You can refer to this [tutorial page](https://www.google.com/amp/s/www.geeksforgeeks.org/profile-application-using-python-flask-and-mysql/amp/) for more details, but below are the simplified steps for the installations.

**Windows:**

1. Install python 3.6, which should come with pip. Follow the installation instructions and check if it’s correctly installed by typing: 
```
py –version 
```
2. Install and set up a virtualenv: 
```
sudo py –m pip install virtualenv 
mkdir <project name> 
cd<project name> 
py –m venv venv 
Call venv\Scripts\activate
```

3. Install the extensions 
```
py -m pip install flask 
```

4. Once you’ve installed these dependents, create a flask command that will be used to specify how to load the application (assuming you’re using bash, otherwise check out the flask site): 
```
// activate the python environment 
$ set FLASK_APP=run.py 
$ flask run 
```
(Make sure you’re within the project foldeeer) 

5. You should be able to run and open the application now. 

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
sudo python3 -m pip install virtualenv
mkdir <project name>
cd <project name>
python3 -m venv <name of environment>
source <name of environment>/bin/activate
```

3. Once you've entered your virtualenv, do the following in the command line 

```
python -m pip install flask
```
4. Once you've installed these dependents, create a flask command that will be used to specify how to load the application <i>(assuming you're using bash, otherwise check out the [flask site](https://flask.palletsprojects.com/en/2.0.x/cli/)</i>:
```
$ export FLASK_APP=run
$ flask run
```
(Make sure you’re within the project folder)

5. You should be able to run and open the application now.


####
