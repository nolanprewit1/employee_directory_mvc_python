### IMPORT REQUIRED PYTHON MODULES ###
import json
from flask import Flask, render_template, request

### IMPORT CONFIG FILE ### 
with open("config.json") as config_file:
    config = json.load(config_file)

### DEFINE THE FLASK APP ###
server = Flask(__name__)

### DEFINE THE ROUTES ###
@server.route("/")
@server.route("/index")
def index():
    return render_template('index.html')

### START AND RUN THE SERVER ###
if __name__ == "__main__":    
    server.run(debug=False,host='0.0.0.0',port=config.get("web_port"))