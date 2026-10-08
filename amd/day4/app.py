from flask import Flask, render_template
import uuid
app = Flask(__name__)
# Default home page
@app.route('/')
def home():
    """Default home page"""
    return "Welcome to Day-4 learning of Flask!"
# Generate UUID route
@app.route('/generate')
def generate_uuid():
    """Generate a UUID"""
    generated_id = uuid.uuid4().hex
    print(generated_id)
    return f"THE generated Id is: {generated_id}"
@app.route('/index')
def indexpage():
    """Render the index page"""
    return render_template('index.html')
@app.route('/about')
def aboutpage():
    """Render the about page"""
    return render_template('about.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)