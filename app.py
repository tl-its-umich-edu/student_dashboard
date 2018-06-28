import flask
from flask import render_template
from flask import request


app = flask.Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', course_id=None)

@app.route("/course_id/<int:course_id>")
def index_with_param(course_id=None):
    return render_template('index.html', course_id=course_id)


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
