from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my flash card application!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


if __name__ == "__main__":
    app.run(debug=True)
