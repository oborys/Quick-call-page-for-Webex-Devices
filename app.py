import flask
from flask import Flask, redirect, url_for, render_template, request, flash, jsonify, request

app = Flask(__name__)

# SIP address for testing
SIPLIST = ["fireplace@ivr.vc", "111@bjn.vc", "havnen@expressway.dk", "halloween@ivr.vc", "fireplace@ivr.vc", "111@bjn.vc", "havnen@expressway.dk"]
API_Key = 'a2n619bc-f49c-4330-bd39-56n73041c509'

def clearSIP():
    with open('SIP.txt', 'w') as f:
        f.write('False')

# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.route("/api", methods=['POST'])
def index():
    auth = request.headers.get("X-API-Key", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "X-API-Key"}, 401)
    print("auth ", auth)
    if auth != API_Key:
        return jsonify("Incorrect API Key"), 400
    with open('SIP.txt', 'r') as f:
        SIP = f.read()
    clearSIP()
    return jsonify(SIP), 200


@app.route("/", methods=["GET", "POST"])
def page():
    if request.method == 'POST':
        print("request.form.get('id') ", request.form.get('id'))
        postSIP(SIPLIST[int(request.form.get('id'))])
    elif request.method == 'GET':
        return flask.render_template('script.html')
    
    return flask.render_template('script.html')

@app.route("/postSIP", methods=['POST'])
def postSIP(data):
    with open('SIP.txt', 'w') as f:
        f.write(data)