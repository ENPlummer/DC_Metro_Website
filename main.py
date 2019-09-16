# Importing Dependencies

import datetime
import os

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#Initialize Flask

app = Flask(__name__)



#Creating the databse tables.

engine = create_engine('postgresql://metro:plum6@localhost/metro')

Base.metadata.bind = engine

# Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Metro_Ridership(Base):
    id = db.Column(db.Integer, primary_key = True)
    DATEMONTHINT = db.Column(db.Integer)
    STATION = db.Column(db.String(255))
    RIDERS_PER_WEEKDAY = db.Column(db.Float)

    def __init__(self,DATEMONTHINT,STATION, RIDERS_PER_WEEKDAY):
        self.DATEMONTHINT = DATEMONTHINT
        self.STATION = STATION
        self.RIDERS_PER_WEEKDAY = RIDERS_PER_WEEKDAY

class Timeperiod_Ridership(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    DATEMONTHINT = db.Column(db.Integer)
    STATION = db.Column(db.String(255))
    PERIOD = db.Column(db.String(255))
    RIDERS_PER_WEEKDAY = db.Column(db.Float)

    def __init__(DATEMONTHINT, STATION, PERIOD, RIDERS_PER_WEEKDAY):
        self.DATEMONTHINT = DATEMONTHINT
        self.STATION = STATION
        self.PERIOD = PERIOD
        self.RIDERS_PER_WEEKDAY = RIDERS_PER_WEEKDAY

# DC Metro Database


# Flask Routes

@app.route("/")
def index():
	# Return the homepage.
	return render_template("index.html")

@app.route("/top25stationsaverage")
def top25stations():
    average_top_25 = Metro_Ridership.query(Metro_Ridership.STATION, func.avg(Metro_Ridership.RIDERS_PER_WEEKDAY)).group_by(Metro_Ridership.STATION).\
    order_by(func.avg(Ridership.RIDERS_PER_WEEKDAY).desc()).limit(25).all()

    average_top_25_dict = dict(average_top_25)
    
    top_25_stations = []
    top_25_averages = []

    for key, value in average_top_25_dict.items():
        top_25_stations.append(key)
        top_25_averages.append(value)

    return jsonify(top_25_stations, top_25_averages)
    
@app.route("/bottom25stationsaverage")
def bottom25stations():
    average_bottom_25 = Metro_Ridership.query(Metro_Ridership.STATION, func.avg(Metro_Ridership.RIDERS_PER_WEEKDAY)).group_by(Metro_Ridership.STATION).\
    order_by(func.avg(Metro_Ridership.RIDERS_PER_WEEKDAY).asc()).limit(25).all()

    average_bottom_25_dict = dict(average_bottom_25)

    bottom_25_stations = []
    bottom_25_averages = []

    for key, value in average_bottom_25_dict.items():
        bottom_25_stations.append(key)
        bottom_25_averages.append(value)

    return jsonify(bottom_25_stations, bottom_25_averages)

@app.route("/top25stationstotal")
def totaltop25stations():
    top_25_total = Metro_Ridership.query(Metro_Ridership.STATION, func.sum(Metro_Ridership.RIDERS_PER_WEEKDAY)).group_by(Metro_Ridership.STATION).\
    order_by(func.sum(Ridership.RIDERS_PER_WEEKDAY).desc()).limit(25).all()

    top_25_total_ridership_dict = dict(top_25_total)
    
    top_25_total_stations = []
    top_25_total_ridership = []

    for key, value in top_25_total_ridership_dict.items():
        top_25_total_stations.append(key)
        top_25_total_ridership.append(value)

    return jsonify(top_25_total_stations, top_25_total_ridership)

@app.route("/bottom25stationstotal")
def totalbottom25stations():

    bottom_25_total = Metro_Ridership.query(Metro_Ridership.STATION, func.sum(Metro_Ridership.RIDERS_PER_WEEKDAY)).group_by(Metro_Ridership.STATION).\
    order_by(func.sum(Ridership.RIDERS_PER_WEEKDAY).asc()).limit(25).all()

    bottom_25_total_ridership_dict = dict(bottom_25_total)

    bottom_25_total_stations = []
    bottom_25_total_ridership = []

    for key, value in bottom_25_total_ridership_dict.items():
        bottom_25_total_stations.append(key)
        bottom_25_total_ridership.append(value)

    return jsonify(bottom_25_total_stations, bottom_25_total_ridership)

@app.route("/timeperiodaverage")
def timeperiod_average_ridership():
    timeperiod_average = Timeperiod_Ridership.query(Timeperiod_Ridership.PERIOD, func.avg(Timeperiod_Ridership.RIDERS_PER_WEEKDAY)).\
    group_by(Timeperiod.PERIOD).all()

    timeperiod_average_ridership = dict(timeperiod_average)

    time_periods = []
    time_period_averages = []

    for key, value in timeperiod_average_ridership.items():
        time_periods.append(key)
        time_period_averages.append(value)

    return jsonify(time_periods, time_period_averages)

@app.route("/timeperiodridershiptotal")
def timeperiodtotalridership():
    timeperiod_total =  Timeperiod_Ridership.query(Timeperiod_Ridership.PERIOD, func.sum(Timeperiod_Ridership.RIDERS_PER_WEEKDAY)).\
    group_by(Timeperiod.PERIOD).all()

    timeperiod_total_ridership = dict(timeperiod_total)

    time_periods_total = []
    time_period_total_ridership = []

    for key, value in timeperiod_total_ridership.items():
        time_periods_total.append(key)
        time_period_total_ridership.append(value)

    return jsonify(time_periods_total, time_period_total_ridership)

# initiate the app.py.

if __name__ == '__main__':
    app.run(host='127.0.0.0', port=8080, debug=True)





