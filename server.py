from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!!"



@app.route("/game.html")
def send_game():
    return send_from_directory('html', 'game.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
