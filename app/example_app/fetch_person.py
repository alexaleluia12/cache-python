import os
import json

import requests
import redis


def fetch_person(id, police):
    fetch_instance = select_instance(police)
    return fetch_instance.fetch(id)


def select_instance(police):
    maps = {'CTN': FetchCTN, 'NO': FetchNO}
    for internal_police in maps:
        if internal_police == police:
            return maps[internal_police]()

    raise RuntimeError(f'Police {police} not found')


class FetchCTN:
    def __init__(self):
        self.person_location = os.environ['PERSON_LOCATION']
        self.redis_cli = redis.Redis(host=os.environ['REDIS_HOST'])

    def fetch(self, id):
        person = self.redis_cli.get(f'person:{id}')
        if person:
            print('cache hit', flush=True)
            return json.loads(person)
        else:
            print('cache miss', flush=True)
            person = fetch_from_network(self.person_location)
            self.redis_cli.set(f'person:{id}', json.dumps(person))
            return person


class FetchNO:
    def __init__(self):
        self.person_location = os.environ['PERSON_LOCATION']

    def fetch(self, id):
        print('networkonly', flush=True)
        return fetch_from_network(self.person_location)


def fetch_from_network(uri):
    resource = requests.get(uri).json()
    return resource
