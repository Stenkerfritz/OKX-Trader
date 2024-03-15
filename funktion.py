import config
import main
import okx.Account as Account
import okx.Trade as Trade
from datetime import datetime, timezone
import time



# timestamp = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'



def kauf(waehrung, budget, flag):
    tradeAPI = Trade.TradeAPI(config.YOUR_API_KEY, config.YOUR_SECRET_KEY, config.YOUR_PASS, use_server_time=time.time(), flag=flag)
    result =tradeAPI.place_order(instId="BTC-USDT", tdMode="cash",  side="buy", ordType="limit", px="19000", sz="0.01")
    print(result)

    if result["code"] == "0":
        print("Successful order request，order_id = ", result["data"][0]["ordId"])
    else:
        print("Unsuccessful order request，error_code = ", result)
            # ", Error_message = ",result["data"][0]["sMsg"])


def verkauf():
    print("verkaufen")

def warten():
    print("nix")


