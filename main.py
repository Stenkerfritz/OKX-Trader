# 1. Mainmethode
# 2. Funktionen für Eingabe der Grundwerte
# 3. Funktionen für die Berechnung des Depotwertes
# 4. Funktionen für den websocket-Zugriff
# 5. Funktionen für den Zugriff auf die API
# 6. Schleife um alles, was immer wieder ausgeführt werden soll

import config
import okx.Account as Account
import okx.MarketData as MarketData
import okx.PublicData as PublicData
import okx.SpreadTrading as SpreadTrading
import funktion
import json
from datetime import datetime,timezone
import time
if __name__ == "__main__":
    #    print("Test")

    # API initialization
    apikey = config.YOUR_API_KEY
    secretkey = config.YOUR_SECRET_KEY
    passphrase = config.YOUR_PASS

    flag = "0"  # live trading: 0, demo trading: 1
    marketDataAPI = MarketData.MarketAPI(flag=flag)
    publicDataAPI = PublicData.PublicAPI(flag=flag)

    # stufen = funktion.sicherheit
    # quote = funktion.steigung

# Get maximum buy/sell amount or open amount
    handelsBudget = float(input("Bitte geben Sie den Startbetrag ein!"))
    sicherheit = input("Bitte geben Sie an wie oft nachgekauf werden darf!")
    steigung = input("Bitte geben Sie die Steigerungquote ein!")

# spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    marketDataAPI = MarketData.MarketAPI(flag=flag)
# get tickers
    result = marketDataAPI.get_tickers(instType="SPOT")
    print(result["code"])
    print(result["msg"])
    print(result["data"])
    json.dump(result,open('api-resultat.json','w'),indent=4,sort_keys=True)

    result = marketDataAPI.get_ticker(instId="BTC-USDT")
    json.dump(result, open('api-resultat-BTC-USDT".json', 'w'), indent=4, sort_keys=True)
    handelsWaehrung = result["data"][0]["instId"]
    handelsKurs = result["data"][0]["last"]
    print(handelsWaehrung)
    print(handelsKurs)

    # funktion.kauf(handelsWaehrung, handelsBudget, flag)

    zeit = time.time()
    print(int(zeit))





    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get account balance
    result = accountAPI.get_account_balance()
    print(result)




