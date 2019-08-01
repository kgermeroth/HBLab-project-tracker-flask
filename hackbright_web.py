"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)
app.secret_key = "ssssshhhhsecret"

@app.route("/")
def show_students_projects():
    """Shows a list of students and list of projects"""

    githubs = hackbright.get_students()
    projects = hackbright.get_projects()

    return render_template("homepage.html",
                            githubs=githubs,
                            projects=projects)

@app.route("/student/<github>")
def get_student(github):
    """Show information about a student."""

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    return render_template("student_info.html", first=first, 
                                                last=last, 
                                                github=github,
                                                projects=projects)

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

@app.route("/projects/<title>")
def project_info(title):
    """Lists project information"""

    project = hackbright.get_project_by_title(title)
    student_grades= hackbright.get_grades_by_title(title)

    return render_template("project.html", project=project, student_grades=student_grades)


if __name__ == "__main__":  
    hackbright.connect_to_db(app)
    app.run(debug=True)
