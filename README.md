# APIweb
------------set up--------------
-------------------------------------------
cmd โฟลเดอร์นี้
python -m venv venv
ถ้าใช้ window           / mac,linux
venv\Scripts\activate / source venv/bin/activate
ใน backend + models ( cd backend , cd models )
pip install -r requirements.txt ( ไปก็อปชื่อทุกอันมา pip install )
------------------------------------------- (อันนี้กูว่ามันแค่บล็อก libary จากโฟลเดอร์อื่น)
---- api ----
cd backend 
python app.py

ถ้าปกติมันจะประมาณนี้ 
----
* Serving Flask app 'app' 
* Debug mode: on WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
* Running on http://127.0.0.1:5000 Press CTRL+C to quit 
* Restarting with stat 
* Debugger is active! 
* Debugger PIN: 838-199-432
----
check ด้วยการเข้า http://127.0.0.1:5000/health
ปกติ 
{"status":"ok"}
---- api ----

------------- Running -----------
เปิด cmd ไหม่ 
cd frontend 
python -m http.server 8000
http://127.0.0.1:8000/index.html
------------ Running ------------

มีอะไรถาม chat
