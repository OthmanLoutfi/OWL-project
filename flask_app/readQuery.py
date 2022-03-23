import rdflib
from rdflib import Graph



def readHotel():
	#read the rdf file
    g = Graph()
    g.parse("static/data/data.rdf")
    query="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://www.owl-ontologies.com/unnamed.owl#>

SELECT * WHERE {
  ?poi rdf:type ns:Hotel.
  ?poi ns:hasLatitude ?lat.
  ?poi ns:hasLongitude ?long.
  ?poi ns:hasName ?name.
  ?poi ns:hasDistrict ?district.
}

"""

    qres=g.query(query)

    poi = [] 
    for row in qres:
        s = {"Name":row.name, "District":row.district, "Latitude":row.lat, "Longitude":row.long }
        poi.append(s)

    return poi

def readStation():
	#read the rdf file
    g = Graph()
    g.parse("static/data/data.rdf")
    query="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://www.owl-ontologies.com/unnamed.owl#>

SELECT * WHERE {
  ?poi rdf:type ns:Station.
  ?poi ns:hasLatitude ?lat.
  ?poi ns:hasLongitude ?long.
  ?poi ns:hasName ?name.
  ?poi ns:hasDistrict ?district.
}

"""

    qres=g.query(query)

    poi = [] 
    for row in qres:
        s = {"Name":row.name, "District":row.district, "Latitude":row.lat, "Longitude":row.long }
        poi.append(s)

    return poi



def historyTrip():
	#read the rdf file
	g = Graph()
	g.parse("static/data/data.rdf")
	query="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://www.owl-ontologies.com/unnamed.owl#>

SELECT * WHERE {
  ?t rdf:type ns:Trip.
  ?t ns:hasDeparture ?dep.
  ?t ns:hasArrival ?ar.
  ?dep ns:hasName ?depName.
  ?dep ns:hasDistrict ?depDistrict.
  ?ar ns:hasName ?arName.
  ?ar ns:hasDistrict ?arDistrict.
  ?dep ns:hasLatitude ?latdep.
  ?dep ns:hasLongitude ?longdep.
  ?ar ns:hasLatitude ?latar.
  ?ar ns:hasLongitude ?longar.
  
  
}

"""
	qres=g.query(query)
	poi = [] 
	for row in qres:
		departure = {"Name":row.depName, "District":row.depDistrict, "Latitude":row.latdep, "Longitude":row.longdep }
		arrival = {"Name":row.arName, "District":row.arDistrict, "Latitude":row.latar, "Longitude":row.longar }

		s = {"departure" : departure, "arrival" : arrival}
		poi.append(s)

	return poi
