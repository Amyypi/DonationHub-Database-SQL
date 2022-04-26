from flask import Flask, render_template, url_for, flash, redirect, request
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from DonationHub import app, db
from DonationHub.models import charities, counties, poverty, states, unemployment
import requests

#@app.route('/')
#def main():
#	return render_template('DataDashboard.html')

#db.create_all()

# Info: https://datatables.net/reference/option/
##################################
#  Unemployment table page
##################################
@app.route('/')
def index():
    return render_template('unemployment_table.html', title='Unemployment Data')

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
   #    'recordsFiltered': total_filtered,
        'recordsTotal': unemployment.query.count(),
        'draw': request.args.get('draw', type=int),
    }


if __name__ == '__main__':
    app.run()

print("Running routes.py\n");