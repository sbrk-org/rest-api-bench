#!/usr/bin/env python

import json
import requests

url = 'http://localhost:5000'

def get_index():
    h={'Authorization': 'oui'}
    resp = requests.get(url='{0}/'.format(url), params={}, headers=h)
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

def post_coupons():
    data = {'hash': 'mobylette2', 'validated_by': '54a69a040d765b36ad3255eb'}
    resp = requests.post(url='{0}/coupons'.format(url), json=data)
    print('POST /coupons ==> {0}'.format(resp.text))

def get_coupons():
    resp = requests.get(url='{0}/coupons'.format(url), params={})
    data = json.loads(resp.text)
    print('GET /coupons ==> {0}'.format(data))

def main():
    get_index()
    get_teams()
    get_users()
    post_team()
    get_teams()
    post_coupons()
    get_coupons()

if __name__ == '__main__':
    main()
