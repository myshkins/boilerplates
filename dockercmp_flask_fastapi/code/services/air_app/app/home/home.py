"""homepage routes"""
from flask import Blueprint, render_template


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')

@home_bp.route('/', endpoint='home', methods=['GET', 'POST'])
def home():
    """render home page view"""
    return render_template("index.html")
