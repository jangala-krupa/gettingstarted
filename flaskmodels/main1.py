from flask import Flask, render_template
import tablib
import os
from werkzeug import secure_filename
import requests
 
app = Flask (__name__)
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
dataset = tablib.Dataset()
@app.route('/uploader', methods = ['POST'])
def upload1_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
   f1= open(f)
   dataset.csv = f1.read()    
   return dataset.html    
 
if __name__ == "__main__":
    app.run(debug= True, port = 5000)