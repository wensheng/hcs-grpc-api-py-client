"""
This is an example of using mirror node REST API (and has nothing to do with grpc client).
It finds accounts that have >10 million hbars and display them in order.
"""
import json
import requests

params = {"account.balance": "gt:1000000000000000"}
r = requests.get("https://mainnet-public.mirrornode.hedera.com/api/v1/balances", params=params)
data = r.json()

sorted_data = sorted(data['balances'], key=lambda x: x['balance'], reverse=True)
for b in sorted_data:
    print("account: %10s balance: %.2f m" % (b['account'], b['balance']/1e14))
print("total:", len(sorted_data))
