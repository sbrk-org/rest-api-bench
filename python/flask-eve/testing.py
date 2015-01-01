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
    print('GET /team ==> {0}'.format(data))

def get_users():
    resp = requests.get(url='{0}/users'.format(url), params={})
    data = json.loads(resp.text)
    print('GET /users ==> {0}'.format(data))

def main():
    get_index()
    get_teams()
    get_users()

if __name__ == '__main__':
    main()
