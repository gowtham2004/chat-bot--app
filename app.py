from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot",method = ["post"])


def response():
    query = dict(request.form)['query']
    result = query+" "+time.ctime()
    return jsonify({"response": "hello"})



