from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return send_from_directory('html', 'game.html')

@app.route("/html/<path:path>")
def send_game(path):
    return send_from_directory('html', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
