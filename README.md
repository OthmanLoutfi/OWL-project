# HotelRain

## Files

### Ontology
- [Hotelrain.owl](Hotelrain.owl)
- [Hotelrain - RDF.rdf](Hotelrain%20-%20RDF.rdf)

### Queries
- [Queries.txt](Queries.txt)

### Notebook with SPARQL query tool and scripts used to populate the ontology
- [rdflib2.ipynb](rdflib2.ipynb)

### Individuals data in csv files
- [hebergements-classes.csv](hebergements-classes.csv)
- [garesnet.csv](garesnet.csv)

### Word Report
- [Rapport_KABRO_JEYARATNAM_LOUTFI.pdf](Rapport_KABRO_JEYARATNAM_LOUTFI.pdf)

#### old/backup files
- [old/](old)


## Installation

If you want to have a copy of the code, you can : 

* Clone this repo : `git clone git@github.com:OthmanLoutfi/OWL-project.git`

In your computer : 

* In the shell, go into the repository using `cd PATH_TO_REPO`
* Install all the necessary packages by running in the shell `pip install -r requirements.txt`
* Then enter the app folder by typing `cd flask_app`
* Make some set-up to prepare the app
  * On Linux, Mac
  ```console
  $ export FLASK_APP = app
  $ export FLASK_ENV = development
  ```
  * On windows
  ```console
  > set FLASK_APP = app
  > set FLASK_ENV = development
  ```
* Run the server by typing `flask run`
* Open a web browser like Chrome and go to this URL : http://localhost:5000/


## How to use the app

Once the web page is loaded, you can navigate through all the pages

1. **Welcome page** : You can access to three maps, one with all the stations in France, one with all the Hotels and the last one with all the sations and hotels.
2. **Make A Trip** : You can decide to make a Trip and visualize it in a Map, you just have to choose a station of departure and a stations of arrival
3. **History of all Trips** : You can access to a history of all the trips and visualize them in a map
4. **Traveler** : You can access to the history of trips from one traveler in particular.
