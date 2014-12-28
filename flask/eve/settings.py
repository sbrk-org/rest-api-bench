# MongoDB Configuration

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'api'
MONGO_PASSWORD = 'api'
MONGO_DBNAME = 'api-bench'

# API
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

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
        'users': {
            'login': {
                'type': 'string',
                'minlength': 3,
                'maxlength': 10,
                },
            'role': {
                'type': 'list',
                'allowed': ['participant', 'guest', 'admin']
                },
            },
        },
    }

DOMAIN = {
    'users': users,
    }
