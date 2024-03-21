import config
import main
import okx.Account as Account
import okx.Trade as Trade
from datetime import datetime, timezone
import time



# timestamp = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'



def GET_KAUF(flag, budget):
    tradeAPI = Trade.TradeAPI(config.GET_API_KEY(flag), config.GET_SECRET_KEY(flag), config.GET_PASS(flag), False)
    # Simple mode, limit order
    result = tradeAPI.place_order(
        instId="BTC-USDT",
        tdMode="cash",
        clOrdId="b15",
        side="buy",
        ordType="market",
        px="",
        sz=budget
    )
    print(result)

    if result["code"] == "0":
        print("Successful order request，order_id = ", result["data"][0]["ordId"])
        print(result)
    else:
        print("Unsuccessful order request，error_code = ", result)
            # ", Error_message = ",result["data"][0]["sMsg"])


def verkauf():
    print("verkaufen")

def warten():
    print("nix")


