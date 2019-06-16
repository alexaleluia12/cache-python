from functools import wraps

from flask import Blueprint, jsonify, request, Response

from . import example
from . import utils
from .model import pagamento
from ..common import AppException, middleware

blueprint = Blueprint('example', __name__)


@blueprint.errorhandler(AppException.AppException)
def handle_app_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@blueprint.route('/person/<int:id>/police/<string:police>', methods=['GET'])
@middleware.json_response
def get_person(id, police):
    attrs = request.args.get('attrs')
    return example.handler_person(id, police, attrs)
