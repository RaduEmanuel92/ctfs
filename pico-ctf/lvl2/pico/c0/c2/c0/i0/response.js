var res = {'data':'HTTP/1.1 200 Partial Content\x0aX-Powered-By: Express\x0aAccept-Ranges: bytes\x0aCache-Control: public, max-age=0\x0aLast-Modified: Fri, 31 Mar 2017 03:32:13 GMT\x0aETag: W/\x221af-15b226baa48\x22\x0aContent-Type: application/javascript\x0aContent-Range: bytes 0-430/431\x0aContent-Length: 431\x0aDate: Sun, 02 Apr 2017 09:06:19 GMT\x0aConnection: keep-alive\x0a\x0avar mongo\x09= require(\x22mongodb\x22).MongoClient;\x0avar nconf\x09= require(\x22nconf\x22);\x0a\x0anconf.argv().env();\x0a\x0alet db;\x0a\x0amongo.connect(`mongodb://localhost:27017/blundertale`)\x0a\x09.then((d) =\x3e {\x0a\x09\x09db = d;\x0a\x09\x09return db.authenticate(nconf.get(\x22MONGO_USER\x22), nconf.get(\x22MONGO_PASS\x22));\x0a\x09})\x0a\x09.then(() =\x3e {\x0a\x09\x09return db.createCollection(\x22games\x22);\x0a\x09})\x0a\x09.catch((err) =\x3e {\x0a\x09\x09console.error(\x22[DB] DB connection failed\x22, err);\x0a\x09})\x0a\x09.then(() =\x3e {\x0a\x09\x09db.close();\x0a\x09});'}