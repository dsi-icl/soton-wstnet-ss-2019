#!/usr/bin/env python
  
#copied from https://stackoverflow.com/a/48586799

import sys, csv, json
from geojson import Feature, FeatureCollection, Polygon

features = []
f = 'sample.csv' if len(sys.argv) < 2 else sys.argv[1]
with open(f) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers

    for id, month, reported_by, falls_within, longitude, latitude, location, lsoa_code, lsoa, crime, outcome, context in reader:
        if crime == 'Criminal damage and arson':
            longitude, latitude = map(float, (longitude, latitude))
            features.append(
                Feature(
                    id = id,
                    properties = {
                        'timestamp': month + '-01T00:00:00Z',
                        'version': '1',
                        'changeset': '0',
                        'name': crime + ',' + outcome
                    },
                    geometry = Polygon([[(longitude, latitude),(longitude, latitude)]])
                )
            )

collection = FeatureCollection(features)
with open(f.replace('.csv', '.json'), 'w') as f:
    f.write('%s' % collection)
