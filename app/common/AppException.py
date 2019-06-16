# flask pattern: http://flask.pocoo.org/docs/1.0/patterns/apierrors/


class AppException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        map_representation = dict(self.payload or ())
        map_representation['message'] = self.message
        return map_representation
