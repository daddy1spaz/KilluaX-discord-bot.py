I used uptime robot for this one

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "i will work a night shift and not enjoy it i will work a night shift and not enjoy it i will work a night shift and not enjoy it i will work a night shift and not enjoy it i will work a night shift and not enjoy it i will work a night shift and not enjoy it i will work a night shift and not enjoy it"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
