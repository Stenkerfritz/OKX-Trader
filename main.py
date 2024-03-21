# 1. Mainmethode
# 2. Funktionen für Eingabe der Grundwerte
# 3. Funktionen für die Berechnung des Depotwertes
# 4. Funktionen für den websocket-Zugriff
# 5. Funktionen für den Zugriff auf die API
# 6. Schleife um alles, was immer wieder ausgeführt werden soll

from openpyxl import Workbook, load_workbook
import config
import okx.Account as Account
import okx.MarketData as MarketData
import okx.PublicData as PublicData
import okx.SpreadTrading as SpreadTrading
import funktion
import json
from datetime import datetime,timezone
import time
import okx.Trade as Trade
if __name__ == "__main__":
    #    print("Test")

    flag = "1"  # live trading: 0, demo trading: 1
    # API initialization
    apikey = config.GET_API_KEY(flag)
    secretkey = config.GET_SECRET_KEY(flag)
    passphrase = config.GET_PASS(flag)

    handelsBudget = float(input("Bitte geben Sie den Startbetrag ein!"))
    sicherheit = input("Bitte geben Sie an wie oft nachgekauf werden darf!")
    steigung = input("Bitte geben Sie die Steigerungquote ein!")

    marketDataAPI = MarketData.MarketAPI(flag=flag)
    publicDataAPI = PublicData.PublicAPI(flag=flag)

    # stufen = funktion.sicherheit
    # quote = funktion.steigung

    # Get maximum buy/sell amount or open amount

    # spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    marketDataAPI = MarketData.MarketAPI(flag=flag)
    # get tickers
    result = marketDataAPI.get_tickers(instType="SPOT")
    print(result["code"])
    print(result["msg"])
    print(result["data"])
    json.dump(result,open('results/api-resultat.json','w'),indent=4,sort_keys=True)

    zeit = time.time()
    print(int(zeit))

    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get account balance
    result = accountAPI.get_account_balance()
    print(result)

    wb = Workbook()
    ws = wb.active
    ws.titel = "OKX-Trade aktuell"

    k = 1
    ws["A"+str(k)].value = "Vorgangs NR"
    ws["B"+str(k)].value = "Waehrung"
    ws["C"+str(k)].value = "Kauf-Kurs"
    ws["D"+str(k)].value = "Betrag Kauf/Verkauf"
    ws["E"+str(k)].value = "gesamt Menge"
    ws["F"+str(k)].value = "Kosten"
    ws["G"+str(k)].value = "tatsaechliche Menge"
    ws["H"+str(k)].value = "Druchschnittskurs"
    ws["I"+str(k)].value = "Aktion"
    wb.save("OKX-Trade.xlsx")

    menge = 0
    j = 0
    i = 1
    kauf = funktion.GET_KAUF(flag, handelsBudget)

    result = marketDataAPI.get_ticker(instId="BTC-USDT")
    json.dump(result, open('results/api-resultat-BTC-USDT.json', 'w'), indent=4, sort_keys=True)
    handelsWaehrung = result["data"][0]["instId"]
    handelsKurs = result["data"][0]["last"]
    print(handelsWaehrung)
    print(handelsKurs)
    budget = str(handelsBudget / float(handelsKurs))

    k = 2
    ws["A"+str(k)].value = str(i) + "." + str(j + 1)
    ws["B" + str(k)].value = handelsWaehrung
    ws["C" + str(k)].value = handelsKurs
    ws["D" + str(k)].value = handelsBudget
    gesamtMenge = float(handelsBudget) * 1 / float(handelsKurs)
    ws["E" + str(k)].value = gesamtMenge
    kosten = gesamtMenge * 0.108 / 100
    ws["F" + str(k)].value = kosten
    tatsaechlicheMenge = gesamtMenge - kosten
    ws["G" + str(k)].value = tatsaechlicheMenge
    druchschnittskurs = handelsBudget/tatsaechlicheMenge
    ws["H" + str(k)].value = druchschnittskurs
    ws["I" + str(k)].value = "Kaufen"
    ws.insert_rows(2)
    wb.save("OKX-Trade.xlsx")
    j = j + 1

    while j != 0:
        time.sleep(1)
        result = marketDataAPI.get_ticker(instId="BTC-USDT")
        handelsKurs = result["data"][0]["last"]
        if druchschnittskurs * 0.99 > float(handelsKurs):
            kauf=funktion.GET_KAUF(flag, handelsBudget)
            ws["A" + str(k)].value = str(i) + "." + str(j + 1)
            ws["B" + str(k)].value = handelsWaehrung
            ws["C" + str(k)].value = handelsKurs
            ws["D" + str(k)].value = handelsBudget
            gesamtMenge = float(handelsBudget) * 1 / float(handelsKurs)
            ws["E" + str(k)].value = gesamtMenge
            kosten = gesamtMenge * 0.108 / 100
            ws["F" + str(k)].value = kosten
            tatsaechlicheMenge = gesamtMenge - kosten
            ws["G" + str(k)].value = tatsaechlicheMenge
            gesamtBudget = handelsBudget * (j +1)
            eingekauteMenge = tatsaechlicheMenge + ws["G3"].value
            druchschnittskurs = gesamtBudget / eingekauteMenge
            ws["H" + str(k)].value = druchschnittskurs
            ws["I" + str(k)].value = "Kaufen"
            ws.insert_rows(2)
            wb.save("OKX-Trade.xlsx")
            # j = j + 1
            j = 0                               # nur für den Testlauf



