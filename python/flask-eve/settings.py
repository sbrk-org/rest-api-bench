# MongoDB Configuration

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'api'
MONGO_PASSWORD = 'api'
MONGO_DBNAME = 'api-bench'

# API
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# /teams
teams = {
    # allow teams to be modified
    'resource_methods': ['GET', 'POST'],
    # allow teams to be retrieved by name
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name',
        },
    # what a team looks like in mongodb
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 10,
            'unique': True,
            },
        'points': {
            'type': 'integer',
            },
        },
    }

# /users
users = {
    # allow users to be modified
    'resource_methods': ['GET', 'POST'],
    # allow users to be retrieved by name
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'login',
        },
    # what a user looks like in mongodb
    'schema': {
        'login': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 10,
            'unique': True,
            },
        'role': {
            'type': 'list',
            'allowed': ['participant', 'guest', 'admin']
            },
        'team': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'teams',
                'field': '_id',
                },
            },
        },
    }

DOMAIN = {
    'users': users,
    'teams': teams,
    }
