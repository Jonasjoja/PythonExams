#Importing modules
import time
import webbrowser
import random

while True:
    sites = random.choice(["https://www.youtube.com/watch?v=oHg5SJYRHA0","https://www.youtube.com/watch?v=lXMskKTw3Bc","https://www.youtube.com/watch?v=cvh0nX08nRw"])
    webbrowser.open(sites)
    seconds = random.randrange(5, 10)
    time.sleep(seconds)