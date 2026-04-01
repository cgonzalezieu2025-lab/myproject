import pandas as pd 
import numpy as np 

data1 = pd.read_csv(r"/mnt/c/Users/Claudia Gonzalez/Downloads/export (3).csv")
data1 = data1.dropna() 
print(data1.columns)
data1 = data1.drop(columns= ["tmin","tmax","wpgt"])

data1 = data1.rename(columns={
    "date": "datetime",
    "tavg": "temperature",
    "prcp": "precipitation",
    "pres": "pressure",
    "wspd": "wind_speed",
    "wdir": "wind_direction",
    "tsun": "sun_time"

})
print(data1.columns)

data1["datetime"] = pd.to_datetime(data1["datetime"])





























