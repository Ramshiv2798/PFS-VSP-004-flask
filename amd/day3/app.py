from flask import Flask

app = Flask(__name__)

# Avoid shadowing route parameter names
user_name = "sanjay rocky"

@app.route('/')
def home():
    """Default home page"""
    return "Hello, World!"

@app.route('/about/')
def details():
    """About page"""
    return "This is the about page."

@app.route('/sanjay/')
@app.route('/profile/')
@app.route('/rocky/')
@app.route('/kumar/')
def profile():
    """Profile page"""
    return "This is the profile page."

@app.route('/name/<name>')
def show_name(name):
    """Name page"""
    return f"Hello, {name}!"

@app.route('/course/<course_name>')
def course(course_name):
    """Course page"""
    return f"This is the <b>{course_name}</b> course page."
@app.route('/student/<int:student_id>')
def student(student_id):
    """Student page"""
    return f"This is the profile page for student with ID: {student_id}"
@app.route('/percentage/<float:percentage>')
def percentage(percentage):
    """Percentage page"""
    return f"This is the percentage page for {percentage}%."
@app.route('/user/<string:username>')
def user_profile(username):
    """User profile page"""
    return f"This is the profile page for user: {username}"
@app.route('/path/<path:file_name>')
def show_path(file_name):
    """Path page"""
    return f"This is the path page for: {file_name}"
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    """Student ID page"""
    return f"This is the student ID page for: {stu_id}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
