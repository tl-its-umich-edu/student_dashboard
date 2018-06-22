import flask
from flask import render_template
app = flask.Flask(__name__)
 
@app.route("/files")
def files(name=None):
    return render_template('files.html', name=name)


@app.route("/grades")
def grades():
    return render_template('grades.html')

@app.route("/files/multiple_bar")
def multiple_bar():
    return render_template('small_multiples_files_bar_chart.html')

if __name__ == "__main__":
    app.run()
