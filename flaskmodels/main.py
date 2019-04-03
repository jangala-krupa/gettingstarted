from flask import Flask, render_template
import tablib
import os
 
app = Flask (__name__)
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'TEST200.csv')) as f:
    dataset.csv = f.read()
 
@app.route("/")
def index():    
    return dataset.html    
 
if __name__ == "__main__":
    app.run(debug= True, port = 9000)