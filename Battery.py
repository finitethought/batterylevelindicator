# -*- coding: utf-8 -*-
"""
code of file1.py 
Run file1.py , after which you execute file2.py 
both files should be in the same project
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
axes = plt.axes()

def animate(i):
    graph_data = open('Samplefile.txt','r').read()
    
    lines = graph_data.split("\n")
    xs = []
    ys = []
    x_minute = []
    y_minute = []
    x_hour = []
    y_hour = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(int(x))
            ys.append(int(y))
    
    for ra in range(0,len(ys),60):
        y_minute.append(np.mean(ys[ra:ra+60]))
        x_minute.append(ra/60)
        
    for rb in range(0, len(y_minute), 60):
        try:
            y_hour.append(np.mean(y_minute[rb:rb+60]))
            x_hour.append(rb)
        except:
            pass
    
    plt.cla()
    plt.ylim([0, 105])
    plt.yticks(np.arange(0, 110, 10))
    if (len(xs) < 1000):
        plt.plot(xs,ys)
        plt.ylabel("Battery %")
        plt.xlabel("Time in sec")
    elif(len(xs) >= 1000 & len(x_minute) < 1000):
        plt.plot(x_minute,y_minute)
        plt.ylabel("Battery %")
        plt.xlabel("Time in minutes")
    else:
        plt.plot(x_hour,y_hour)
        plt.ylabel("Battery %")
        plt.xlabel("Time in Hour")
    
ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()

"""
code of file2.py
"""

import time
import numpy as np

battery = 100
state = "Charged"
for i in range(1,7000):
    with open("Samplefile.txt", "a") as f:
        f.write("{},{}\n".format(i,battery))
    
    time.sleep(0.05)
    if state == "Charged" and i % 10 == 0:
        battery = battery - np.random.randint(0,4)
        if battery == 20 or battery < 20:
            state = "Discharged"
        
    if state == "Discharged" and i % 10 == 0:
        battery = battery + 2
        if battery == 100:
            state = "Charged"
               
    
    
