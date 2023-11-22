


# AI Weather by Meteosource
# https://rapidapi.com/MeteosourceWeather/api/ai-weather-by-meteosource/
# API名稱 daily
import requests
from datetime import datetime
import pandas as pd

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

qurey_df.to_csv('C:/Users/asus\Documents/World_weather_summary/qurey_df.csv')
#display(qurey_df)

headers = {
	"X-RapidAPI-Key": "52e62fcc97mshd861568b73fda40p112a1ajsn7e0d8542c825",
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json()['daily']['data'])
#print(response.json()['lat'])
#print(response.json()['lon'])


col = ['day','weather','temperature','feels_like','precipitation','storm','freeze','humidity']
df = pd.DataFrame(columns=col)

forecast_daily_data = response.json()['daily']['data']
for i in forecast_daily_data:
    date_obj = datetime.strptime(i['day'], "%Y-%m-%d")
    new_row = pd.DataFrame({"day": date_obj,"weather": i['weather'], "temperature": i['temperature'], "feels_like": i['feels_like'], "precipitation": i['probability']['precipitation'], "storm" : i['probability']['storm'], "freeze" : i['probability']['freeze'], "humidity": i['humidity']},index=[0])
    df = pd.concat([df,new_row],axis=0, ignore_index=True)

df['storm'] = df['storm'].apply(lambda x : x*100.0) 
df['freeze'] = df['freeze'].apply(lambda x : x*100.0)    

#display(df)
df.to_csv('C:/Users/asus\Documents/World_weather_summary/df.csv')

#C:/Users/asus\Documents/World_weather_summary/df.csv