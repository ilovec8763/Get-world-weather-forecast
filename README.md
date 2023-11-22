# Get-world-weather-forecast

撰寫python script 接受經緯座標輸入，並使用WeatherAPI.com 的open api服務，向該網站的資料庫請求未來20天的天氣預報，再自動地將結果用power bi做視覺化描述。

![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_pic1.png)

# 環境佈署
1. 選定本機安裝好的其中一個python interpreter，並確保安裝以下pakage:
    1. requests
    2. datetime
    3. pandas

2. 將World_weather_summary下載到本機，可以自己選擇喜歡的位置。

3. 打開World_weather_summary資料夾，您會看到一個script.py，在檔案名稱上點擊右鍵，鼠標移到"開啟檔案(H)"上方，在目錄跑出來之後選擇"選擇其他應用程式(C)"。
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step3.png)

4. 此時，你看到螢幕上跳出一個檔案瀏覽器。
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step5.png)

5. 找到python作為打開py檔案的應用程式，勾選下方"一律使用此應用程式來開啟.py檔案"。如果不想選錯python interpreter或是找不到app，勾選下方"一律使用此應用程式來開啟.py檔案"，接者，利用這個檔案瀏覽器尋找你一開始選定的python interpreter，檔案名稱應為"python.exe"。

6. 如果成功設定的話，您應該會看到這個console window :
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/console_win.png)


