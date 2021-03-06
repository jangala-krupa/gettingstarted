from flask import Flask, make_response, request
import io
import csv
import tablib
app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=",",")


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>FAQ IMPORT</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/transform', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    print(csv_input)
    #for row in csv_input:
        #print(row)

    stream.seek(0)
    result = transform(stream.read())

    response = make_response(result)
   # response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response
@app.route('/transform_view')
def transform_view2():
    dataset=tablib.Dataset()
    dataset.csv = result.csv
    return dataset.html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)