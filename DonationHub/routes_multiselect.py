from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, json
from sqlalchemy import func, select
from sqlalchemy.orm import Bundle
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import charities, counties, poverty, states, unemployment, Form
from BackEnd.backend import *
from flask_wtf import FlaskForm
from wtforms import widgets, RadioField, SelectMultipleField, SubmitField, SelectField
import sqlite3
import pandas as pd
from statistics import mean
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

@app.route('/', methods=['GET', 'POST'])
def index():
    # Headings for the table
    headings = ("State FIPS","State Name","Abbreviation","State Population", "County FIPS","County Name","County Population", "Unemployed People","Unemployed Rate")

    # Make dropdown for state options
    form = Form()
    form.state.choices = [(state.STATEID, state.STATENAME) for state in states.query.all()]

    state_list = states.query
    county_list = counties.query

    # put states in a list
    state_na = db.session.query(states.STATENAME).all()
    stateArray = []
    for state_info in state_na:
        stateObj = state_info.STATENAME
        stateArray.append(stateObj)
    print(stateArray)

    # put counties in a list
    count_na = db.session.query(counties.COUNTYNAME).all()
    countyArray = []
    for county_info in count_na:
        countyObj = county_info.COUNTYNAME
        countyArray.append(countyObj)

    # Make table
    result = getOnlyUnemploymentTable(stateArray,countyArray)

    # SELECT 
    if request.method == 'POST':
        state = states.query.filter_by(STATEID=form.state.data).first()
        county_list = counties.query.filter_by(STATEID=form.county.data).all()
        #result = db.session.query( states.ABBREVIATION, counties.COUNTYNAME, unemployment.UNEMPLOYED_PEOPLE, unemployment.UNEMPLOYMENT_RATE).join(counties).join(states).all()


        # put states in a list
        stateArray = []
        stateObj = state.STATENAME
        stateArray.append(stateObj)


        result = getOnlyUnemploymentTable(stateArray,countyArray)

        state_n = state.STATENAME
        return render_template('unemployment_table.html',form=form, result=result, headings=headings, state_list=state_list, county_list=county_list)

    
    #print(Count_example)
    return render_template('unemployment_table.html',form=form, result=result, headings=headings, state_list=state_list, county_list=county_list)

    # Make dropdown for state options
    form = Form()
    form.state.choices = [(state.STATEID, state.STATENAME) for state in states.query.all()]
  
    # put states in a list
    state_na = db.session.query(states.STATENAME).all()
    stateArray = []
    for state_info in state_na:
        stateObj = state_info.STATENAME
        stateArray.append(stateObj)
    print(stateArray)

    # put counties in a list
    count_na = db.session.query(counties.COUNTYNAME).all()
    countyArray = []
    for county_info in count_na:
        countyObj = county_info.COUNTYNAME
        countyArray.append(countyObj)

    # Make table
    result = getOnlyUnemploymentTable(stateArray,countyArray)

    # SELECT 
    if request.method == 'POST':
        county = counties.query.filter_by(STATEID=form.county.data).first()
        state = states.query.filter_by(STATEID=form.state.data).first()

        # put states in a list
        stateArray = []
        stateObj = state.STATENAME
        stateArray.append(stateObj)

        # put counties in a list
        countyArray = []
        countyObj = county.COUNTYNAME
        countyArray.append(countyObj)

        # Make table
        result = getOnlyUnemploymentTable(stateArray,countyArray)

        # Data computations
        tot_unemp_people = getTotalUnEmployedPeople(result)
        avg_unemp_people = getAverageUnEmployedPeople(result)
        avg_unemp_rate = getAverageUnEmploymentRate(result)

        state_n = state.STATENAME
        county_n = county.COUNTYNAME
        return render_template('unemployment_table.html', form=form, result=result, headings=headings, tot_unemp_people=tot_unemp_people, avg_unemp_people=avg_unemp_people, avg_unemp_rate=avg_unemp_rate)
    
    tot_unemp_people = getTotalUnEmployedPeople(result)
    avg_unemp_people = getAverageUnEmployedPeople(result)
    avg_unemp_rate = getAverageUnEmploymentRate(result)
    
    return render_template('unemployment_table.html', form=form, result=result, headings=headings, tot_unemp_people=tot_unemp_people, avg_unemp_people=avg_unemp_people, avg_unemp_rate=avg_unemp_rate)


@app.route('/county/<get_county>')
def county(get_county):
    # put counties in list
    state_data = counties.query.filter_by(STATEID=get_county).all()
    countyArray = []
    for county_info in state_data:
        countyObj = {}
        countyObj['STATEID'] = county_info.STATEID
        countyObj['COUNTYNAME'] = county_info.COUNTYNAME
        countyArray.append(countyObj)
    return jsonify({'county_list' : countyArray})

if __name__ == '__main__':
    app.run()