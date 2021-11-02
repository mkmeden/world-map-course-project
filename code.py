import folium
from folium.map import LayerControl
import pandas 

def color_classifier(x):
    if x<1000:
        return "green"
    elif 1000<=x<3000 :
        return "orange"
    else:
        return "red"

map= folium.Map(location =[38.58 , -99.09] , zoom_start = 6 , tiles = "Stamen Terrain")

data = pandas.read_csv("Webmap_datasources\Volcanoes.txt")
lat = tuple(data["LAT"])
lon = tuple(data["LON"])
name  = tuple(data["NAME"])
elev= tuple(data["ELEV"])

fgv =folium.FeatureGroup(name ="Volcano")
fgp =folium.FeatureGroup(name ="Population")

fgp.add_child(folium.GeoJson(data = open("Webmap_datasources\world.json" , "r" , encoding="utf-8-sig").read() , 
style_function=lambda x: {"fillColor" :"green" if x["properties"]["POP2005"]<10000000 else "orange" if 10000000<=x["properties"]["POP2005"]<20000000
else "red"}))

for i , j , k , l in zip(lat ,lon , name , elev) :
    fgv.add_child(folium.CircleMarker(location=[i , j] , radius = 6,popup=k +"\n"+ str(l) +"m" ,color= color_classifier(l) , fillColor=color_classifier(l) , fill =True,fill_opacity =1.0 ))

map.add_child(fgp)

map.add_child(fgv)

map.add_child(LayerControl())

map.save("World Map(practice).html")