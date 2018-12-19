import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    #Query for currency exchange rate
    currency = request.form.get("currency")
    print(currency)
    res = requests.get("http://data.fixer.io/api/latest", params = {
        "access_key" : "4a4c2226924f2d46cb6509aba2ea0f96",
        #"base" : "USD",#base is restricted
        "symbols" : currency})
    #Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success" : False})

    #make sure currency is in response
    data = res.json()
    print(data)
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success" : True, "rate" : data["rates"][currency]})
    
    

