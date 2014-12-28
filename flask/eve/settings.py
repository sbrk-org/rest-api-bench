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
    'resource_methods': ['GET', 'POST'],
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
