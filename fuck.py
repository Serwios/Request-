import webbrowser
import os
import time
import threading

threads = []
lst = ["https://cutt.ly/shMIIid", "https://cutt.ly/uhMISOT",
       "https://cutt.ly/ThMICtj", "https://cutt.ly/3hMINtA",
       "https://cutt.ly/nhMIMKX", "https://cutt.ly/9hMI0Bg",
       "https://cutt.ly/fhMKzBb", "https://cutt.ly/jhMKciq",
       "https://cutt.ly/VhMKvZT", "https://cutt.ly/KhMKbld",
       "https://cutt.ly/PhMKb1z", "https://cutt.ly/5hMKn0A",
       "https://cutt.ly/nhMKQbY", "https://cutt.ly/0hMKWaw",
       "https://cutt.ly/ZhMKW4f", "https://cutt.ly/UhMKE58",
       "https://cutt.ly/mhMKTel", "https://cutt.ly/3hMKYgs",
       "https://cutt.ly/3hMKYgs", "https://cutt.ly/0hMKURs",
       "https://cutt.ly/ahMKIuu", "https://cutt.ly/thMKI5Z",
       "https://cutt.ly/BhMKPyC", "https://cutt.ly/YhMKPZu",
       "https://cutt.ly/VhMKAHQ", "https://cutt.ly/vhMKSoV",
       "https://cutt.ly/YhMKSMg", "https://cutt.ly/JhMKFoB",
       "https://cutt.ly/vhMKJrg", "https://cutt.ly/4hMKXuR",
       "https://cutt.ly/rhMKBQo", "https://cutt.ly/IhMKM9Y",
       "https://cutt.ly/hhMK0FR", "https://cutt.ly/VhMK2Vt",
       "https://cutt.ly/ehMK3W6", "https://cutt.ly/7hMK44X",
       "https://cutt.ly/ehMK5FI", "https://cutt.ly/vhMK6N9",
       "https://cutt.ly/YhMLw5q", "https://cutt.ly/zhMLe7k",
       "https://cutt.ly/yhMLtPL", "https://cutt.ly/khMLymV",
       "https://cutt.ly/bhMLumO", "https://cutt.ly/IhMLifL",
       "https://cutt.ly/IhMLifL", "https://cutt.ly/IhMLaAx",
       "https://cutt.ly/6hMLsn1", "https://cutt.ly/8hMLdWf",
       "https://cutt.ly/4hMLfPs", "https://cutt.ly/9hMLgje",
       "https://cutt.ly/7hMLhAe", "https://cutt.ly/8hMLjh5",
       "https://cutt.ly/MhMLjSj", "https://cutt.ly/QhMLkOa",
       "https://cutt.ly/ihMLljm", "https://cutt.ly/ghMLzrf",
       "https://cutt.ly/ahMLxwf", "https://cutt.ly/khMLx7d",
       "https://cutt.ly/bhMLcRu", "https://cutt.ly/0hMLvla"]


def fuckIt(performTime):
    key = True
    count = 0

    while key:
        for link in lst:
            webbrowser.open(link)
        count += 1
        print("Count: ", count)

        if performTime == count:
            time.sleep(30)
            os.system("taskkill /im chrome.exe")
            key = False

    print("End")


threads.append(threading.Thread(target=fuckIt(20)))
map(lambda x: x.start(), threads)