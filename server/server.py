# Karolina Szafran-Belzowska, December 2020
# HDip Data Analytics, Data Representation project 2020
# Implementing server.py

from flask import Flask, url_for, request, redirect, abort, jsonify


app = Flask(__name__, static_url_path = '', static_folder='')

# in command prompt: - python -m venv venv
#                    - .\venv\Scripts\activate.bat
#                    - pip freeze
#                    - pip install flask
#                    - pip freeze
#                    - python server.py
# The server is running, 
# In other command prompt type: curl http://127.0.0.1:5000/
@app.route('/')
def index():
    return"Welcome to the Data Representation Project"

@app.route('/fruits')
def getAll():
    results = 


if __name__ == "__main__":
    print("in if")
    app.run(debug=True)