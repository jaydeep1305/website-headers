import os
import re
import json
import time
import random
import requests
from loguru import logger
from flask import Flask, request, render_template
from hasura import Hasura


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/save', methods=['POST'])
def save():
    try:
        if request.method == 'POST':
            headers = request.form.get('headers')
            website_name = request.form.get('website_name')
            Hasura.save(headers, website_name)
            return 'Saved'
    except Exception as ex:
        logger.error(ex)
        return 'Error'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081, debug=True)

