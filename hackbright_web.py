"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, session

import hackbright

app = Flask(__name__)
app.secret_key = "ssssshhhhsecret"


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html", first=first, last=last, github=github)

@app.route("/student-search")
def get_student_form():
    """Show form for searching a student"""
    return render_template("student_search.html")


@app.route("/student-add")
def add_student_form():
    """Shows form for getting new student information"""

    return render_template("student_add.html")


@app.route("/student-info", methods=['POST'])
def add_new_student():
    """Adds a new student to the student database"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    github = request.form['github']

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("new_student.html", first_name=first_name,
                                            last_name=last_name,
                                            github=github)


if __name__ == "__main__":  
    hackbright.connect_to_db(app)
    app.run(debug=True)
