from flask import Flask
#create a Flask application instance
app = Flask(__name__)
#__name__ is saying its a flask object
#now we will start defining the routes
@app.route('/')
def home():
    """Default home page"""
    return f'Welcome to AI AGENTS AND FUTURES'
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,debug=True)