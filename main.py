from flask import Flask,render_template,request
import requests

app = Flask(__name__)

api_key = "4ae4691e7fa27007a8071fc92ab08e16"


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount")
        amount = float(amount)
        if firstCurrency == secondCurrency:
            result = amount

        elif firstCurrency == "BTC" and secondCurrency == "USD":
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            app.logger.info(response)

            infos = response.json()
            result_raw = (infos["bpi"]["USD"]["rate_float"])
            result = result_raw * amount
        elif firstCurrency == "BTC" and secondCurrency == "EUR":
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            app.logger.info(response)

            infos = response.json()
            result_raw = (infos["bpi"]["EUR"]["rate_float"])
            result = result_raw * amount
        elif firstCurrency == "BTC" and secondCurrency == "ETH":
            response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=ETH')
            app.logger.info(response)
            infos = response.json()
            result_raw = (infos['ETH'])
            result = result_raw * amount

        elif firstCurrency == "ETH":
            if secondCurrency == "USD":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
                app.logger.info(response)
                infos = response.json()
                result_raw = (infos['USD'])
                result = result_raw * amount
            elif secondCurrency == "EUR":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR')
                app.logger.info(response)
                infos = response.json()
                result_raw = (infos['EUR'])
                result = result_raw * amount
            elif secondCurrency == "BTC":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC')
                app.logger.info(response)
                infos = response.json()
                result_raw = (infos['BTC'])
                result = result_raw * amount
        elif firstCurrency == "USD":
            if secondCurrency == "EUR":
                response = requests.get("http://data.fixer.io/api/latest?access_key=" + api_key)
                app.logger.info(response)
                infos = response.json()
                result_raw = infos["rates"]["USD"]
                result = amount / result_raw
            elif secondCurrency == "BTC":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=BTC')
                app.logger.info(response)
                infos = response.json()
                result_raw = infos['BTC']
                result = result_raw * amount
            elif secondCurrency == "ETH":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=ETH')
                app.logger.info(response)
                infos = response.json()
                result_raw = infos['ETH']
                result = result_raw * amount
        elif firstCurrency == "EUR":
            if secondCurrency == "USD":
                response = requests.get("http://data.fixer.io/api/latest?access_key=" + api_key)
                app.logger.info(response)
                infos = response.json()
                result_raw = infos["rates"]["USD"]
                result = amount * result_raw
            elif secondCurrency == "BTC":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=BTC')
                app.logger.info(response)
                infos = response.json()
                result_raw = infos['BTC']
                result = result_raw * amount
            elif secondCurrency == "ETH":
                response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=ETH')
                app.logger.info(response)
                infos = response.json()
                result_raw = infos['ETH']
                result = result_raw * amount

        currencyInfo = dict()

        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info=currencyInfo)
    else:
        return render_template("index.html" )


if __name__ == "__main__":
    app.run(debug=True)
