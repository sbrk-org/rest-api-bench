#!/usr/bin/env python

import json
import requests

url = 'http://localhost:5000'

def get_index():
    resp = requests.get(url='{0}/'.format(url), params={})
    data = json.loads(resp.text)
    print('GET / ==> {0}'.format(data))

def get_teams():
    resp = requests.get(url='{0}/teams'.format(url), params={})
    data = json.loads(resp.text)
    print('GET /teams ==> {0}'.format(data))

def post_team():
    data = {'name': 'mobylette', 'points': 0}
    resp = requests.post(url='{0}/teams'.format(url), json=data)
    print('POST /teams ==> {0}'.format(resp.text))

def get_users():
    resp = requests.get(url='{0}/users'.format(url), params={})
    data = json.loads(resp.text)
    print('GET /users ==> {0}'.format(data))
    
def main():
    get_index()
    get_teams()
    get_users()
    post_team()
    get_teams()

if __name__ == '__main__':
    main()
