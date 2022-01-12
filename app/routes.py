import asyncio
import threading

from flask import render_template
from app import app
from app.core.download import download_all_file


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query', methods=['POST', 'GET'])
def query():
    print(f"Inside flask function: {threading.current_thread().name}")
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_file())
    return render_template("index.html")
