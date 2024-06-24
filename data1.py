import pandas as pd, json

df = pd.read_csv('results.csv',
                sep=',')
with open('russia copy.geojson','r',encoding='UTF-8') as response:
        counties = json.loads(response.read())

