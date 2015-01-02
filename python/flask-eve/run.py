import uuid

from eve import Eve
from eve.auth import TokenAuth
from werkzeug.security import check_password_hash

class MyAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        # check token
        print token
        users = app.data.driver.db['users']
        return users.find_one({'token': token})
        # check authorizations

        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['users']
        lookup = {'username': username}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account and check_password_hash(account['password'], password)

def add_token(documents):
    for document in documents:
        token = uuid.UUID()
        document["token"] = token.hex()
     
app = Eve(auth=MyAuth)
app.on_insert_users += add_token

if __name__ == '__main__':
    with app.app_context():
        team_id = app.data.driver.db['teams'].insert({'name': 'team-esl', 'points': 42})
        app.data.driver.db['users'].insert({'name': 'm1ch3l', 'team': team_id, 'token': 'oui'})
    app.run(debug=True)
