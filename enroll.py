from flask import Flask, render_template, request

app = Flask(__name__)
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

@app.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses)

@app.route('/enroll/<course_id>')
def enroll(course_id):
    course = courses.get(course_id, {})
    if not course:
        return "Course not found", 404
    return render_template(
        'enroll.html',
        course_name=course["name"],
        course_duration=course["duration"],
        course_start_date=course["start_date"]
    )

@app.route('/enroll', methods=["POST"])
def submit_enrollment():
    # Handle the enrollment submission
    data = request.form
    print("Enrollment Data:", data)
    return f"Successfully enrolled in {data['course_name']}!"

if __name__ == "__main__":
    app.run(debug=True)

