Puzzingly Accountable

data.pcap contine mai multe stream-uri HTTP impartite in chunk-uri mai mici. Practic fiecare HTTP req corespunde unei serii de mai multe response-uri care contin bucati consecutive din aceeasi resursa.
Flag-ul se gaseste in cele 2 .png-uri trimise: SoV1xW80.png si libAFo31.png
Din Wireshark: cauti GET-ul corespunzator pentru fiecare din png-uri si dai Follow > TCP Stream. Show data as raw. Copy de la inceputul resursei (hex format).
Din editorul de text preferat, se strip-uiesc "\n"-urile.
Cu scriptul de Python atasat (da, alea 3 linii) exporti hexstring-ul intr-un fisier png
"python pygen.py > img1.png"

Am atasat si imaginile corespunzatoare.