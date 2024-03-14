import config
import main
import okx.Account as Account
import okx.Trade as Trade
import datetime




timestamp = datetime.now().isoformat(timespec='milliseconds') + 'Z'

def kauf(waehrung, budget, flag):
    tradeAPI = Trade.TradeAPI(config.YOUR_API_KEY, config.YOUR_SECRET_KEY, config.YOUR_PASS, timestamp,flag=flag)
    result =tradeAPI.place_order(instId="BTC-USDT", tdMode="cash", clOrdId="b15", side="buy", ordType="limit", px="19000", sz="0.01")
    print(result)

    if result["code"] == "0":
        print("Successful order request，order_id = ", result["data"][0]["ordId"])
    else:
        print("Unsuccessful order request，error_code = ",
              #result["data"][0]["sCode"], ", Error_message = ",
              result)


def verkauf():
    print("verkaufen")

def warten():
    print("nix")


