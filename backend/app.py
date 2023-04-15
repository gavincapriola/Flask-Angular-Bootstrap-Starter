import os

from flask import Flask, send_from_directory
from flask_cors import CORS

dir_path: str = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path + "/../my-app/")

os.system(
    "ng build --configuration production --output-path ../backend/dist/my-app/")

os.chdir(dir_path)


app = Flask(__name__, static_folder="dist/my-app")
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
