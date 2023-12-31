
# AI Weather by Meteosource
# https://rapidapi.com/MeteosourceWeather/api/ai-weather-by-meteosource/
# API name : daily
import os
import requests
from datetime import datetime
import pandas as pd

basedir = os.getcwd()

X_RapidAPI_Key = "xxxxxxxxxxx Your_RapidAPI_Key xxxxxxxxxxxx"
X_RapidAPI_Host = "xxxxxxxxxx Your_RapidAPI_Host xxxxxxxxxxxxxxx"


print("Pakage were imported...")

lat = input("Input latutude： ")
lon = input("Input longtitude : ")

print("lat : ", lat )
print("lon : ", lon)

#lat = "37.81021"
#lon = "-122.42282"

url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"

querystring = {"lat":lat,"lon":lon,"language":"en","units":"auto"}

qurey_df = pd.DataFrame(querystring, index=[0])

qurey_df.to_csv(os.path.join(basedir,"qurey_df.csv"))

headers = {
	"X-RapidAPI-Key": X_RapidAPI_Key,
	"X-RapidAPI-Host": X_RapidAPI_Host
}

response = requests.get(url, headers=headers, params=querystring)


col = ['day','weather','temperature','feels_like','precipitation','storm','freeze','humidity']
df = pd.DataFrame(columns=col)

forecast_daily_data = response.json()['daily']['data']
for i in forecast_daily_data:
    date_obj = datetime.strptime(i['day'], "%Y-%m-%d")
    new_row = pd.DataFrame({"day": date_obj,"weather": i['weather'], "temperature": i['temperature'], "feels_like": i['feels_like'], "precipitation": i['probability']['precipitation'], "storm" : i['probability']['storm'], "freeze" : i['probability']['freeze'], "humidity": i['humidity']},index=[0])
    df = pd.concat([df,new_row],axis=0, ignore_index=True)

df['storm'] = df['storm'].apply(lambda x : x*100.0) 
df['freeze'] = df['freeze'].apply(lambda x : x*100.0)    

df.to_csv(os.path.join(basedir,"df.csv"))
