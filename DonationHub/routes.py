from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, json
from sqlalchemy import func, select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import charities, counties, poverty, states, unemployment, Form
from BackEnd.backend import *
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, Form
from wtforms.fields import SelectMultipleField, SubmitField
from statistics import mean

import sqlite3
import pandas as pd
import requests

#initialize the flask app
app = Flask(__name__)
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#tell sqlalchemy where the database file is
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#initialize the database
db = SQLAlchemy(app)
con = sqlite3.connect("data.db", check_same_thread=False )
cur = con.cursor()

# For state dropdown
choices = []
class Form(FlaskForm):
    global choices
    state = SelectField('state', choices=[])
    county = SelectField('county', choices=[])
    select_multiple_field = SelectMultipleField(choices=choices)
    position = SelectMultipleField(u'Choose position:')
    submit = SubmitField()



########################################
# Unemployment 
########################################
@app.route('/', methods=['GET', 'POST'])
def index():
    # Headings for the table
    headings = ("State FIPS","State Name","Abbreviation","State Population", "County FIPS","County Name","County Population", "Unemployed People","Unemployed Rate")
    # Make dropdown for state options
    form = Form()
    form.state.choices = [(state.STATEID, state.STATENAME) for state in states.query.all()]

    # SELECT 
    if request.method == 'POST':
        state_l = states.query.filter_by(STATEID=form.state.data).first()
        stateArray = []
        stateObj = state_l.STATENAME
        stateArray.append(stateObj)
        return redirect(url_for('unemployment_county', state_l=stateArray))

     # put states in a list
    state_na = db.session.query(states.STATENAME).all()
    stateArray = []
    for state_info in state_na:
        stateObj = state_info.STATENAME
        stateArray.append(stateObj)
    #print(stateArray)

    # put counties in a list
    count_na = db.session.query(counties.COUNTYNAME).all()
    countyArray = []
    for county_info in count_na:
        countyObj = county_info.COUNTYNAME
        countyArray.append(countyObj)
    choices = countyArray

    form_data = form.select_multiple_field.data
    print(form_data)

    # Make table
    result = getOnlyUnemploymentTable(stateArray,choices)
    tot_unemp_people = getTotalUnEmployedPeople(result)
    avg_unemp_people = getAverageUnEmployedPeople(result)
    avg_unemp_rate = getAverageUnEmploymentRate(result)
    return render_template('unemployment_table_state.html', form=form, result=result, headings=headings, tot_unemp_people=tot_unemp_people, avg_unemp_people=avg_unemp_people, avg_unemp_rate=avg_unemp_rate)

@app.route('/unemployment_county', methods=['GET', 'POST'])
def unemployment_county():
    state_l = request.args['state_l']
    headings = ("State FIPS","State Name","Abbreviation","State Population", "County FIPS","County Name","County Population", "Unemployed People","Unemployed Rate")
    state = states.query.filter(states.STATENAME==state_l).first()
    county_l = counties.query.filter(counties.STATEID==state.STATEID).all()

    stateArray = []
    statename = state.STATENAME
    stateArray.append(statename)
    print("county in post", county_l)

    countyArray = []
    for county_info in county_l:
        countyObj = county_info.COUNTYNAME
        countyArray.append(countyObj)

    if request.method == 'POST':
        # Retrieve county selection from dropdown
        county_list = request.form.getlist('c_list')

        # Make table
        result = getOnlyUnemploymentTable(stateArray,county_list)
        # Data computations
        tot_unemp_people = getTotalUnEmployedPeople(result)
        avg_unemp_people = getAverageUnEmployedPeople(result)
        avg_unemp_rate = getAverageUnEmploymentRate(result)

        return render_template('unemployment_table_county.html', county_list=county_l, result=result, headings=headings, tot_unemp_people=tot_unemp_people, avg_unemp_people=avg_unemp_people, avg_unemp_rate=avg_unemp_rate)

    # Make table
    result = getOnlyUnemploymentTable(stateArray,countyArray)
    # Data computations
    tot_unemp_people = getTotalUnEmployedPeople(result)
    avg_unemp_people = getAverageUnEmployedPeople(result)
    avg_unemp_rate = getAverageUnEmploymentRate(result)

    return render_template('unemployment_table_county.html', county_list=county_l, result=result, headings=headings, tot_unemp_people=tot_unemp_people, avg_unemp_people=avg_unemp_people, avg_unemp_rate=avg_unemp_rate)

if __name__ == '__main__':
    app.run()