import websocket, json

cc = 'btcusd'
interval = '1m'

socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'

print(socket)

def on_message(ws, message):
    print(message)

def on_close(ws):
    print("### closed ###")

ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)

ws.run_forever()