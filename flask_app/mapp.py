import folium
import pandas as pd

def generate_map(data, color, icon, loc = None):

    df = pd.DataFrame.from_dict(data)
    #center = [lat,long]
    #loc = [[(l1, l2),(l1, l2)]]

    my_map = folium.Map(
        location=[46, 2],
        tiles='cartodbpositron',
        zoom_start=6
    )

    df.apply(lambda row:folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["Name"], icon=folium.Icon(color=color,icon=icon,prefix='fa')).add_to(my_map), axis=1)

    
    if(loc != None):
        folium.PolyLine(loc,
                color='green',
                weight=15,
                opacity=0.8).add_to(my_map)



    my_map.save("templates/mymap.html")

    return my_map._repr_html_()

def generate_map_several(data, color, loc = None):


    my_map = folium.Map(
        # center: Hong Kong Space Museum
        location=[46, 2],
        tiles='cartodbpositron',
        zoom_start=6
    )

    for i in range(len(data)):
        df = pd.DataFrame.from_dict(data[i])
        df.apply(lambda row:folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["Name"], icon=folium.Icon(color=color[i], prefix='fa fa-circle-o')).add_to(my_map), axis=1)
        if(loc != None):
            folium.PolyLine(loc,
                color='red',
                weight=15,
                opacity=0.8).add_to(my_map)



    my_map.save("templates/mymap.html")

    #return my_map._repr_html_()