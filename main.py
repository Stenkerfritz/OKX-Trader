# 1. Mainmethode
# 2. Funktionen für Eingabe der Grundwerte
# 3. Funktionen für die Berechnung des Depotwertes
# 4. Funktionen für den websocket-Zugriff
# 5. Funktionen für den Zugriff auf die API
# 6. Schleife um alles, was immer wieder ausgeführt werden soll


from openpyxl import Workbook, load_workbook
import config
import requests
from bs4 import BeautifulSoup
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
    # Platz für Abfrage Verkauf in "BTC oder USDT"

    marketDataAPI = MarketData.MarketAPI(flag=flag)
    publicDataAPI = PublicData.PublicAPI(flag=flag)

    # stufen = funktion.sicherheit
    # quote = funktion.steigung

    # Get maximum buy/sell amount or open amount

    # spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    #marketDataAPI = MarketData.MarketAPI(flag=flag)
    # get tickers
    result = marketDataAPI.get_tickers(instType="SPOT")
    print(result["code"])
    print(result["msg"])
    print(result["data"])
    json.dump(result,open('results/api-resultat.json','w'),indent=4,sort_keys=True)

    zeit = time.time()
    print(int(zeit))

    #accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    # Get account balance
    #result = accountAPI.get_account_balance()
    #print(result)

    wb = Workbook()
    ws = wb.active
                                                    # hier kommt noch eine Schleife
    ws.titel = "OKX-Trade aktuell"
    ws["A1"].value = "Vorgangs NR"
    ws["B1"].value = "Waehrung"
    ws["C1"].value = "Kauf-Kurs"
    ws["D1"].value = "Betrag Kauf/Verkauf"
    ws["E1"].value = "gekaufte Menge"
    ws["F1"].value = "Kosten"
    ws["G1"].value = "tatsaechliche Menge"
    ws["H1"].value = "Druchschnittskurs"
    ws["I1"].value = "Gesamt Menge"
    ws["J1"].value = "Gesamt Durchschnitt"
    ws["K1"].value = "Aktion"
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

    ws["A2"].value = str(i) + "." + str(j + 1)
    ws["B2"].value = handelsWaehrung
    ws["C2"].value = handelsKurs
    ws["D2"].value = handelsBudget
    gesamtMenge = float(handelsBudget) * 1 / float(handelsKurs)
    ws["E2"].value = gesamtMenge
    kosten = gesamtMenge * 0.108 / 100
    ws["F2"].value = kosten
    tatsaechlicheMenge = gesamtMenge - kosten
    ws["G2"].value = tatsaechlicheMenge
    druchschnittskurs = handelsBudget/tatsaechlicheMenge
    ws["H2"].value = druchschnittskurs
    ws["I2"].value = ws["G2"].value
    ws["J2"].value = ws["D2"].value
    ws["K2"].value = "Kaufen"

    wb.save("OKX-Trade.xlsx")
    j = j + 1

    while j != 0:
        try:
            marketDataAPI = MarketData.MarketAPI(flag=flag)
            result = marketDataAPI.get_ticker(instId="BTC-USDT")
            handelsKurs = result["data"][0]["last"]
            print(handelsKurs)

            if druchschnittskurs * 0.99 > float(handelsKurs):
                kauf = funktion.GET_KAUF(flag, handelsBudget)
                ws.insert_rows(2)
                ws["A2"].value = str(i) + "." + str(j + 1)
                ws["B2"].value = handelsWaehrung
                ws["C2"].value = handelsKurs
                ws["D2"].value = handelsBudget
                gesamtMenge = float(handelsBudget) * 1 / float(handelsKurs)
                ws["E2"].value = gesamtMenge
                kosten = gesamtMenge * 0.108 / 100
                ws["F2"].value = kosten
                tatsaechlicheMenge = gesamtMenge - kosten
                ws["G2"].value = tatsaechlicheMenge
                gesamtBudget = float(handelsBudget) + float(str(ws["J3"].value))
                eingekauteMenge = tatsaechlicheMenge + float(str(ws["I3"].value))
                ws["I2"].value = eingekauteMenge
                ws["J2"].value = gesamtBudget
                druchschnittskurs = ws["J2"].value / ws["I2"].value
                ws["H2"].value = druchschnittskurs
                ws["K2"].value = "Kaufen"

                wb.save("OKX-Trade.xlsx")
                # j = j + 1

                j = 0                               # nur für den Testlauf

            # elif für verkauf
                #if für Gewinn in BTC erzielen
                # else für Gewinn in USDT erzielen

        except Exception as e:
            print(f"Fehler aufgetreten: {e}")
            continue

