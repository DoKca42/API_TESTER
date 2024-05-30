import json
import websocket
import threading
import time


class Bot:

    def __init__(self, player_id):
        self.player_id = player_id
        self.ws = None

    def printDATA(self, msg):
        print("\33[31m" + self.player_id + ": \33[37m" + str(msg))

    def run(self):
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp("ws://localhost:8065/ws/room/",
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def on_message(self, ws, message):
        data = json.loads(message)
        self.printDATA(data)
        if data.get("connection_etalished", False):
            self.authenticate(ws)

    def authenticate(self, ws):
        self.printDATA("Auth")
        ws.send(json.dumps({
            "type": "auth",
            "session_id": self.player_id,
            "player_id": self.player_id
        }))

    def on_error(self, ws, error):
        self.printDATA("Error:" + str(error))

    def on_close(self, ws, close_status_code, close_msg):
        self.printDATA("### closed ###")

    def on_open(self, ws):
        #printDATA("Opened connection")
        self.authenticate(ws)

    def close_connection(self):
        if self.ws:
            self.ws.close()
            self.printDATA("Connection closed.")
        else:
            self.printDATA("No active connection to close.")

    def reopen_connection(self):
        self.printDATA("Reopening connection...")
        self.connect()


class BotManager:

    def __init__(self):
        self.clients = {}
        self.threads = {}

    def addBot(self, bot_id):
        self.clients[bot_id] = Bot(bot_id)
        thread = threading.Thread(target=self.clients[bot_id].run)
        self.threads[bot_id] = thread
        thread.start()


bots = BotManager()
while True:
    id_ = input("Salut: ")
    bots.addBot(id_)
    time.sleep(1)

