from flask import Flask
application = Flask(__name__)

@application.route("/status")
def hello():
    return "Hey Dinesh"

if __name__ == "__main__":
    application.run()
