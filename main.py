# 1. Mainmethode
# 2. Funktionen für Eingabe der Grundwerte
# 3. Funktionen für die Berechnung des Depotwertes
# 4. Funktionen für den websocket-Zugriff
# 5. Funktionen für den Zugriff auf die API
# 6. Schleife um alles, was immer wieder ausgeführt werden soll

import confic
import okx.Account as Account
import okx.MarketData as MarketData
import okx.PublicData as PublicData
import okx.SpreadTrading as SpreadTrading
import funktion

if __name__ == "__main__":
#    print("Test")

# API initialization
    apikey = confic.YOUR_API_KEY
    secretkey = confic.YOUR_SECRET_KEY
    passphrase = input("Passwort")

    flag = "1"  # live trading: 0, demo trading: 1
    marketDataAPI = MarketData.MarketAPI(flag=flag)
    publicDataAPI = PublicData.PublicAPI(flag=flag)

    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    start = funktion.startbetrag
    stufen = funktion.sicherheit
    quote = funktion.steigung

# Get maximum buy/sell amount or open amount
spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get tickers
result = spreadAPI.get_ticker(sprdId="BTC-USDT")
print(result)
