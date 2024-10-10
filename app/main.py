from flask import Blueprint, render_template

app_routes = Blueprint('main', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')




