#!/usr/bin/env python

import json
import requests

url = 'http://localhost:5000'

def index():
    resp = requests.get(url='{0}/'.format(url), params={})
    data = json.loads(resp.text)
    print('GET / ==> {0}'.format(data))

def main():
    index()
    pass

if __name__ == '__main__':
    main()
