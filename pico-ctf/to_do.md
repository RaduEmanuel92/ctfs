# File of things to do

Here you can write what you did up until you stopped in order for someone/something to pick-up where you left off and not from scratch.

## TW_GR_E1_ART Level 2
Ok so the script ./web/TW_GR_E1_force_browse.sh doesn't do much.

Next idea: The final floor contains multiple flags out of which 1 is correct (if any).

Need to find a way to call functions in node to reveal correct flag/delete rest of flags/directly print correct flag.

## A Kaley Ceilidh Level 4
Tried to send "humongous" jsons to the REST-ful app. No luck.

(Oh, now i get it hu-MONGO-us, well that's just hell-arious ... not)

I think the data is stored in a NoSQL DB (Mongo if I were to guess), and I think a NoSQL query must be put in a json and sent.

If anyone has prior experience with Mongo, json, or time, then write the query in a file like "query.json" and you can use the bellow curl command to send it:

curl -H "Content-Type: application/json" -H "Refer: http://shell2017.picoctf.com:8080/" -X POST -d @query.json 'http://shell2017.picoctf.com:8080/search'
