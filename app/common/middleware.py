from functools import wraps

from flask import jsonify

# middleware pattern - http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/


def json_response(f):
    """Return an JSON response with 200. The wrapped need return dict Object"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        call_result = f(*args, **kwargs)
        if call_result:
            return jsonify(call_result)
        raise RuntimeError('The callable has no output to send as JSON')
    return decorated_function
