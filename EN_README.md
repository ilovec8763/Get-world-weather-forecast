# Get-world-weather-forecast

# Functionality

Enter latitude and longitude to obtain the weather forecast worldwide.

The Python script accepts latitude and longitude inputs and uses the AI Weather by Meteosource open API service to request the weather forecast for the next 20 days from the website's database. The results are then automatically visualized using Power BI.

![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_pic1.png)

# Environment Setup

1. After installing Power BI (installation link: https://powerbi.microsoft.com/en-us/desktop/), select one of the installed Python interpreters on your machine and ensure the installation of the following packages:
    1. requests
    2. datetime
    3. pandas

2. Visit the AI Weather by Meteosource page on Rapid API: https://rapidapi.com/MeteosourceWeather/api/ai-weather-by-meteosource/

3. Choose the API named GET daily and obtain the key. You can follow the tutorial in this article (https://reurl.cc/9Rk27x) to get the X-RapidAPI-Key and X-RapidAPI-Host keys.

4. Download the World_weather_summary folder to your local machine, choosing a location you prefer.

5. Open the script.py file in the World_weather_summary folder using an editor. Replace the two variables `X_RapidAPI_Key = "xxxxxxxxxxx Your_RapidAPI_Key xxxxxxxxxxxx"` and `X_RapidAPI_Host = "xxxxxxxxxx Your_RapidAPI_Host xxxxxxxxxxxxxxx"` with the keys obtained earlier.

6. Open the World_weather_summary folder, and you will see a script.py file. Right-click on the file name, hover over "Open with (H)," and select "Choose another app (C)" when the menu appears.
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step3.png)

7. A file browser will appear on the screen.
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step5.png)

8. Find Python as the application to open .py files, check the box below "Always use this app to open .py files." If you don't want to select the wrong Python interpreter or can't find the app, check the box below "Always use this app to open .py files," then use the file browser to locate the Python interpreter you initially selected, which should be named "python.exe."

9. If successful, you should see the console window:
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/console_win.png)

10. Follow the instructions to enter latitude and longitude, and after execution, the data update will be completed.

11. Open World_weather_summary.pbix in Power BI. To correctly update the data, you need to point the data source to the directory of the World_weather_summary folder.
    ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step5.png)
   
12. Go to Home >> Get Data >> Text/CSV, find the location of the CSV files in the World_weather_summary folder (df.csv and query_df.csv), open them, and click "Load" to connect the dashboard and data source.

13. If you want to update the data in the future, simply execute script.py and then return to the Power BI update page to complete the data update.
