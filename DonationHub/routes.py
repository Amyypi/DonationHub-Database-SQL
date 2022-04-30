from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, json
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from DonationHub import app, db
from DonationHub.models import charities, counties, poverty, states, unemployment, Form
#from DonationHub.backend import table_queries, computations
from DonationHub.BackEnd.backend import *
from flask_wtf import FlaskForm
from wtforms import SelectField

import requests

##################################
#  Default Page
##################################
@app.route('/', methods=['GET', 'POST'])
def index():
    #Count_example= Count(['Maryland','Alaska'])
    #unemployment_result = db.session.query(states, counties, unemployment, ).join(counties).join(unemployment).all()
    state_list = states.query
    county_list = counties.query

    form = Form()
    form.state.choices = [(state.STATEID, state.STATENAME) for state in states.query.all()]
  
    if request.method == 'POST':
        county = counties.query.filter_by(STATEID=form.county.data).first()
        state = states.query.filter_by(STATEID=form.state.data).first()
        return '<h1>State : {}, county: {}</h1>'.format(state.STATENAME, county.COUNTYNAME)
    return render_template('unemployment_table.html', form=form, state_list=state_list, county_list=county_list)

    #print(Count_example)
    #return render_template('unemployment_table.html', title='Unemployment Data', state_list=state_list, county_list=county_list)

@app.route('/county/<get_county>')
def county(get_county):
    state_data = counties.query.filter_by(STATEID=get_county).all()
    countyArray = []
    for county_info in state_data:
        countyObj = {}
        countyObj['STATEID'] = county_info.STATEID
        countyObj['COUNTYNAME'] = county_info.COUNTYNAME
        countyArray.append(countyObj)
    return jsonify({'county_list' : countyArray})

# Info: https://datatables.net/reference/option/
##################################
#  Unemployment table page
##################################
@app.route('/api/unemploymentData')
def data():
    query = unemployment.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            unemployment.COUNTYID.like(f'%{search}%'),
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['COUNTYID', 'UNEMPLOYED_PEOPLE', 'UNEMPLOYMENT_RATE']:
            col_name = 'COUNTYID'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(unemployment, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [unemployment.to_dict() for unemployment in query],
       'recordsFiltered': total_filtered,
        'recordsTotal': unemployment.query.count(),
        'draw': request.args.get('draw', type=int),
    }


if __name__ == '__main__':
    app.run()

print("Running routes.py\n")