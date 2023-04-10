from flask import Flask, jsonify, request
from flask import render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return "HI"

if __name__ == "__main__":
    app.run(debug=True)
