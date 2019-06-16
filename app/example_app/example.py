from ..common import AppException
from .fetch_person import fetch_person


def handler_person(id, police, attrs):
    attributes = attrs.split(',')
    raw_person = fetch_person(id, police)
    return filter_person(raw_person, attributes)


def filter_person(person, keys):
    new_person = {}
    for key in keys:
        new_person[key] = person[key]

    return new_person
