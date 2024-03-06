# 1. Mainmethode
# 2. Funktionen für Eingabe der Grundwerte
# 3. Funktionen für die Berechnung des Depotwertes
# 4. Funktionen für den websocket-Zugriff
# 5. Funktionen für den Zugriff auf die API
# 6. Schleife um alles, was immer wieder ausgeführt werden soll


#import okx.Account as Account
#import okx.MarketData as MarketData
#import okx.PublicData as PublicData
import funktion

if __name__ == "__main__":
#    print("Test")

# API initialization
#apikey = "YOUR_API_KEY"
#secretkey = "YOUR_SECRET_KEY"
#passphrase = "YOUR_PASSPHRASE"

#flag = "1"  # live trading: 0, demo trading: 1
#marketDataAPI = MarketData.MarketAPI(flag=flag)
#publicDataAPI = PublicData.PublicAPI(flag=flag)

#accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    start = funktion.startbetrag
    stufen = funktion.sicherheit
    quote = funktion.steigung

# Get maximum buy/sell amount or open amount
#result = accountAPI.get_max_order_size(
#    instId="BTC-USDT",
#    tdMode="isolated"
#)
#print(result)