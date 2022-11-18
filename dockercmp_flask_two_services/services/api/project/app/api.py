"""api routes"""
from flask import current_app as app



@app.route('/hi', endpoint='say_hi', methods=['GET'])
def say_hi():
    """hello world function"""
    return "hello"
