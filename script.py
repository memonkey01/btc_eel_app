from __future__ import print_function	# For Py2/3 compatibility
import eel
import requests
eel.init('web')                     # Give folder containing web files

def print_btc_value(price_mxn):
    response = requests.get('https://api.bitso.com/v3/order_book/?book=btc_mxn')
    json_response = response.json()
    price_mxn = float(price_mxn)
    value = 0
    for i in range(150):
        price = float(json_response['payload']['asks'][i]['price'])
        amount = float(json_response['payload']['asks'][i]['amount'])
        value += price*amount
        #print(value,i)
        if value > price_mxn:
            price_btc = price 
           # global value_btc
            value_btc = (price_mxn / price_btc)*1.01
            #print(value_btc)
            print("El precio del BTC {}".format(price_btc))
            print("El valor de {} MXN en BTC {}".format(price_mxn,value_btc))
            break
    return value_btc

@eel.expose  
def handleinput(x):
    if x != '0':
        returnval = print_btc_value(x)
        eel.display_info(str(returnval))   # Call a Javascript function

eel.start('btc_payment_2.html', size=(700, 750))    # Start