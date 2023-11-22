# Get-world-weather-forecast

撰寫python script 接受經緯座標輸入，並使用WeatherAPI.com 的open api服務，向該網站的資料庫請求未來20天的天氣預報，再自動地將結果用power bi做視覺化描述。

![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_pic1.png)

# 環境佈署
1. 安裝完power bi 之後(安裝連結 :https://powerbi.microsoft.com/zh-tw/desktop/)，選定本機安裝好的其中一個python interpreter，並確保安裝以下的package:
    1. requests
    2. datetime
    3. pandas

2. 將World_weather_summary資料夾下載到本機，可以選擇自己喜歡的位置。

3. 打開World_weather_summary資料夾，您會看到一個script.py，在檔案名稱上點擊右鍵，鼠標移到"開啟檔案(H)"上方，在目錄跑出來之後選擇"選擇其他應用程式(C)"。
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step3.png)

4. 此時，你看到螢幕上跳出一個檔案瀏覽器。
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step5.png)

5. 找到python作為打開py檔案的應用程式，勾選下方"一律使用此應用程式來開啟.py檔案"。如果不想選錯python interpreter或是找不到app，勾選下方"一律使用此應用程式來開啟.py檔案"，接者，利用這個檔案瀏覽器尋找你一開始選定的python interpreter，檔案名稱應為"python.exe"。

6. 如果成功設定的話，您應該會看到這個console window :
  ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/console_win.png)

7. 按照指示輸入經緯度，執行之後即可完成更新資料的動作。

8. 點開World_weather_summary.pbix，進入power bi之後，你需要將資料來源指向World_weather_summary資料夾的目錄才能夠正確更新資料。
    ![alt text](https://github.com/ilovec8763/Get-world-weather-forecast/blob/main/demo_step5.png)
   
10. 到 常用>>取得資料>>文字/CSV ，找到World_weather_summary資料夾中csv檔的位置(df.csv和qurey_df.csv)，打開之後，按下"載入"，即可完成dash board和資料源的連接。

11. 如果您往後想要更新資料，直接執行script.py後，再回到power bi 更新頁面即可完成資料更新。

