import time
from libs.openexchange import OpenExchangeClient

APP_ID = "ac3f1e7a5d4c444fb78e241fd2c940a2"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'First call took {time.time() - start} seconds.')

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'After, 10 calls took {time.time() - start} seconds.')

print(f"USD {usd_amount} is GBP {gbp_amount}")

# print(exchange_rates)
