from flask import Flask, render_template, request
from math import sin, tan, cos, pi, asin, acos, atan


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
            'ctg': round(1 / tan(angle), precision),
            'asin': round(asin(angle), precision),
            'acos': round(acos(angle), precision),
            'atg': round(atan(angle), precision),
            'actg': round(1/atan(angle), precision)
        }

        return render_template("trig_calulator.html", result=result)

    return render_template("trig_calulator.html")

if __name__ == "__main__":
    app.run(debug=True)