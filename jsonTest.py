import csv
import json
from geojson import Feature, FeatureCollection, Point

features = []
with open('CrashSeverity.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for latitude, longitude, score in reader:
        if latitude != 'x':
            latitude, longitude = map(float, (latitude, longitude))
            features.append(
                Feature(
                    geometry=Point((longitude, latitude)),
                    properties={
                        'score': float(score)
                    }
                )
            )

collection = FeatureCollection(features)
with open("GeoObs.geojson", "w") as f:
    f.write('%s' % collection)
