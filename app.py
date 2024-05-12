from flask import Flask, render_template, request
from math import sin, tan, cos, pi


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        angle = float(request.form['angle'])
        precision = int(request.form['precision'])
        units = request.form['units']
        result = {}

        if units == 'degrees':
            angle = angle * pi / 180

        result = {
            'sin': round(sin(angle), precision),
            'cos': round(cos(angle), precision),
            'tg': round(tan(angle), precision),
            'ctg': round(1 / tan(angle), precision)
        }

        return render_template("calculator.html", result=result)

    return render_template("calculator.html")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)