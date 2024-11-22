from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample course data
courses = {
    "web-development": {
        "name": "Web Development",
        "duration": "12 weeks",
        "start_date": "January 15, 2024"
    },
    "data-science": {
        "name": "Data Science",
        "duration": "16 weeks",
        "start_date": "February 1, 2024"
    },
    "cloud-computing": {
        "name": "Cloud Computing",
        "duration": "10 weeks",
        "start_date": "March 5, 2024"
    }
}

enrollments = []  # Store enrollment data

@app.route('/')
@app.route('/templates/home.html')
def home():
    return render_template('home.html')

@app.route('/templates/course.html')
def course_list():
    return render_template('courses.html', courses=courses)

@app.route('/templates/login.html')
def login():
     return render_template('login.html')

@app.route('/templates/register.html')
def register():
     return render_template('register.html')

@app.route('/templates/contact us.html')
def contact():
     return render_template('contact us.html')


if __name__ == '__main__':
    app.run(debug=True)
