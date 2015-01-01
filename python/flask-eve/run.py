from eve import Eve
from eve.auth import BasicAuth
from werkzeug.security import check_password_hash

class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account and check_password_hash(account['password'], password)


app = Eve()

if __name__ == '__main__':
    app.run(debug=True)

