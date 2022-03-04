from app.base import blueprint
from flask import render_template


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html')
