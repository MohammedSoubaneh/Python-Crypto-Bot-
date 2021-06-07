import websocket, json, pprint, talib, numpy
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05

closes = []
in_position = False

client = Client('API KEY', 'API SECRET', tld='us')

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

    
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > 14:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, 14)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > 70:
                if in_position:
                    print("Sell")
                    # put binance sell logic here
                    order_succeeded = order(SIDE_SELL, 0.01, 'BTCUSD')
                    if order_succeeded:
                        in_position = False
                else:
                    print("nothing")
            
            if last_rsi < 30:
                if not in_position:
                    print('buy')
                    order_succeeded = order(SIDE_BUY, 0.01, 'BTCUSD')
                    if order_succeeded:
                        in_position = True
                else:
                    print("nothing")

                
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()