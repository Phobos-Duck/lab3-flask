from flask import Flask, render_template, request
from math import sin, tan, cos, pi


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        angle = float(request.form['angle'])
        precision = int(request.form['precision'])
        units = request.form['units']
        result = ""

        if units == 'degrees':
            angle = angle * pi / 180

        result += f"<p>Синус: {round(sin(angle), precision)}</p>"
        result += f"<p>Косинус: {round(cos(angle), precision)}</p>"
        result += f"<p>Тангенс: {round(tan(angle), precision)}</p>"
        result += f"<p>Котангенс: {round(1 / tan(angle), precision)}</p>"

        return render_template("trig_calulator.html", result=result)

    return render_template("trig_calulator.html")

if __name__ == "__main__":
    app.run(debug=True)