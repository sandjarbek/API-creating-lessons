from flask import Flask, jsonify

from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = "https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1"
    content = requests.get(url).text

    soup = BeautifulSoup(content, "html.parser")

    currency = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(currency[0:-4])
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dictionary = {"Input_currency":in_cur, "output_currency":out_cur, "rate":rate}
    return jsonify(result_dictionary)


app.run()