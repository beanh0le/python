import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])
el = list(df["ELEV"])

def color_producer(el):
    if el < 1000:
        return "green"
    elif 1000 <= el <= 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[41.7,-101.8] , start_zoom=8, tiles="Stamen Terrain") #start_zoom and tiles not mandatory

fgv = folium.FeatureGroup(name="Volcanoes")

for lat,lon,el in zip(lat,lon,el):
    # add_child() adds features like markers to the feature group 
    fgv.add_child(folium.CircleMarker(location=[lat,lon], popup=str(el)+" m", fill_color=color_producer(el), radius=6, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
# adding another layer to the map
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor" : "green" if x['properties']['POP2005']<20000000
else "orange" if 1000000<x['properties']['POP2005']<20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
# below line should be added only after adding the above 2 lines of code
map.add_child(folium.LayerControl())

map.save("Map1.html")