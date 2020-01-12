import requests


def print_btc_value(price_mxn):
    response = requests.get('https://api.bitso.com/v3/order_book/?book=btc_mxn')
    json_response = response.json()
    price_mxn = price_mxn
    value = 0
    for i in range(50):
        price = float(json_response['payload']['asks'][i]['price'])
        amount = float(json_response['payload']['asks'][i]['amount'])
        value += price*amount
        print(value,i)
        if value > price_mxn:
            price_btc = price 
            value_btc = (price_mxn / price_btc)*1.04
            print("El precio del BTC {}".format(price_btc))
            print("El valor de {} MXN en BTC {}".format(price_mxn,value_btc))
            break
    return value_btc
