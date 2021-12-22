#!/user/bin/python
import RPi.GPIO as io
import time
from datetime import datetime
import sqlite3
import json
import os

os.chdir("/home/pi/led/")
io.setmode(io.BCM)
led1 = 23
io.setup(led1, io.OUT)

#variable declaration
x = "LED Status"
#dictionary
d = {}
#id
num = 0



#to connect to database
conn = sqlite3.connect('sharks.db')
cur = conn.cursor()

#now = datetime.now()




while 1:
    j = open("new.json", "r")
    d = json.load(j)
    j.close()
    num = d.get("ID")

    num = num + 1
    now = datetime.now()
    io.output(led1, True)
    x = "LED ON"
    #print(x)
    d1 = now.strftime("%d/%m/%Y")
    #print("d1 = ", d1)
    t1 = now.strftime("%H:%M:%S")
    #print("time =", t1)
        
    d["Date"]= d1
    d["Time"]= t1
    d["Status"]= x
    d["ID"]= num

    j = open("new.json", "w")
    json.dump(d, j)
    j.close()

    cur.execute("INSERT INTO led (Date, Time, Status, ID) values(?,?,?,?)", (d1, t1, x, num))
    conn.commit()

    print(d)
    time.sleep(3)

    num = num + 1
    now = datetime.now()
    io.output(led1, False)
    x = "LED OFF"
    #print(x)
    d1 = now.strftime("%d/%m/%Y")
    #print("d1 = ", d1)
    t1 = now.strftime("%H:%M:%S")
    #print("time =", t1)
    
    time.sleep(1)
    
    d["Date"]= d1
    d["Time"]= t1
    d["Status"]= x
    d["ID"]= num

    j = open("new.json", "w")
    json.dump(d, j)
    j.close()

    cur.execute("INSERT INTO led (Date, Time, Status, ID) values(?,?,?,?)",(d1, t1, x, num))
    conn.commit()
    print(d)
    time.sleep(3)
    
