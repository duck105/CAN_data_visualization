# CAN Data Visualization Website

### 架構

* Python server (app.py): data visualization 
* Post.py: code running on Raspberry pi for sending Arduino's data to Python server



### Run server

* 一台Mac or Linux電腦，並且有安裝python3
* 安裝flask (Web framework) 套件

``` 
$ pip install flask
```

* 跑Python server

```
$ python3 app.py
```

* 查看server的IP (以Mac為例會出現下圖，看en0的部分IP為多少)

指令: ``` $ ifconfig```
結果: ![screenshot](/Users/duck/Desktop/大五上資料/賽車隊/SensorVIsualization/screenshot.png)


* 接著只要跟server連同一個網路的任何裝置，都可以在瀏覽器輸入``` http://192.168.50.15:5000```  連上網站

* P.S. 如果不想用筆電，可以利用heroku (一個提供雲端機器的服務，上面就像一台Linux環境來跑server)。reference: https://www.heroku.com/python

### Code for sending data

* post.py的部分會跑在Raspberry pi上，要記得把 post_data() 中的URL 中的localhost:5000 上面改成server的IP or domain (i.e. 192.168.50.15:5000)

* 想在本機測試的話，剛剛的server不要關，額外開一個terminal跑
  ```
  $ python3 post.py
  ```

  就可以在網站上看到隨機的數字

### SSH 不用打密碼

* 連上Raspberry pi 時要輸入密碼有點麻煩，可以利用ssk key 來做到免密碼登入(安全性甚至更好)

  1. 在Raspberry pi 加目錄新增.ssh 資料夾，並更改權限為700 (如果資料夾已存在就不用)

     ```
     $ cd ~
     $ mkdir .ssh
     $ chmod 700 .ssh
     ```

  2. 在Raspberry pi .ssh 資料夾中新增authorized_keys 檔案，並把權限改為600如果資料夾已存在就不用)

     ```
     $ vim .ssh/authorized_keys 並wq存擋
     $ chmod 600 .ssh/authorized_keys
     ```

  3. 在本機家目錄產生ssh key (一組公私鑰)，reference: https://xenby.com/b/220-%E6%95%99%E5%AD%B8-%E7%94%A2%E7%94%9Fssh-key%E4%B8%A6%E4%B8%94%E9%80%8F%E9%81%8Ekey%E9%80%B2%E8%A1%8C%E5%85%8D%E5%AF%86%E7%A2%BC%E7%99%BB%E5%85%A5

     ```
     $ cd ~
     $ ssh-keygen
     接下來問題通常都直接按enter(用預設的就好)
     ```

  4. 把產生的公鑰(.pub檔) 貼到Raspberry pi .ssh 資料夾中的authorized_keys 檔案中，私鑰就只能放在本機中不要流出去

     ```
     $ cat ~/.ssh/ubuntu_id_rsa.pub 
     複製下來，之後進去Raspberry pi
     RPi: $ vim .ssh/authorized_keys 貼上並wq存擋
     RPi: $ exit回到本機
     ```

  5. 接著在本機登入測試看看，應該不用密碼就能進去

     ```
     $ ssh username@server_host
     ```

     