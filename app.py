from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/templates/home.html')
def home():
     return render_template('home.html')

@app.route('/templates/course.html')
def course():
     return render_template('course.html')

@app.route('/templates/login.html')
def login():
     return render_template('login.html')

@app.route('/templates/register.html')
def register():
     return render_template('register.html')

@app.route('/templates/contact us.html')
def contact():
     return render_template('contact us.html')

@app.route('/templates/enroll.html')
def enroll():
     return render_template('enroll.html')

@app.route('/templates/Profile.html')
def sample():
     return render_template('Profile.html')

if __name__ == '__main__':
    app.run(debug=True)