import folium
import pandas as pd
import rdflib
from rdflib import Graph

from flask import Flask, render_template, request, redirect, url_for

from mapp import generate_map, generate_map_several
from readQuery import readHotel, readStation, historyTrip

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        value = request.form.get('s')

        if(value == "all"):
            hotels = readHotel()
            stations = readStation()

            data = [hotels, stations]
            color = ['blue', 'red']

            generate_map_several(data, color)

        elif(value == "h"):
            hotels = readHotel()
            generate_map(hotels, 'blue', 'home', )
            
        elif(value == "s"):
            stations = readStation()
            generate_map(stations, 'red',  'train',)

        else:
            pass

        #generate_map(stations, center)
        #generate_map(stations, 'red')
        return redirect(url_for('map'))
        #return render_template('mymap.html')
            
    elif request.method == 'GET':
        # return render_template("index.html")
        return render_template('index.html')



    

    #return render_template('index.html', stations=stations)

@app.route("/map")
def map():
    return render_template("mymap.html")

@app.route("/chooseTrip", methods=['GET', 'POST'])
def trip():
    stations = readStation()
    if request.method == 'POST':
        
        loc1 = [float(x) for x in request.form["departure"].split(",")]
        loc2 = [float(x) for x in request.form["arrival"].split(",")]

        loc = [[tuple(loc1), tuple(loc2)]]

        generate_map(stations, 'red', 'train', loc)
        return redirect(url_for('map'))

        
            

    elif request.method == 'GET':

        return render_template("chooseTrip.html", stations = stations)


@app.route("/history", methods=['GET', 'POST'])
def history():

    trip = historyTrip()
    stations = readStation()

    if request.method == 'POST':
        
        l = [float(x) for x in request.form.get('t').split(",")]

        loc = [[tuple(l[0:2]), tuple(l[2:])]]

        generate_map(stations, 'red', 'train', loc)
        return redirect(url_for('map'))


        
        
    elif request.method == 'GET':
        return render_template("history.html", trips = trip)


   






