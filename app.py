# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:28:32 2023

@author: HP
"""

from flask import Flask, render_template,request,jsonify
from chat import get_response
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
#@app.get("/")
@app.route("/",methods=["GET"])
def index_get():
    return render_template("base.html")
#@app.post("/predict")
@app.route("/",methods=["POST"])
def predict():
    text=request.get_json().get("message")
    #check if text is valid
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)
if __name__=="__main__":
    app.run(debug=True)
