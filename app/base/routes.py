from app.base import blueprint
from flask import render_template


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('index.html')


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
