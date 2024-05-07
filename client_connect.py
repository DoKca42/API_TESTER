import json
import websocket
import threading
import time


class Client:

    def __init__(self, player_id):
        self.player_id = player_id
        self.ws = None

    def printDATA(self, msg):
        print("\33[31m" + self.player_id + ": \33[37m" + str(msg))

    def run(self):
        self.ws = websocket.WebSocketApp("ws://localhost:8000/ws/room/",
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

        # Running without dispatcher that involves signal handling
        self.ws.run_forever()

    def sendFindGame(self):
        if self.ws:
            self.printDATA("Sending find game")
            self.ws.send(json.dumps({
                "type": "matchmaking",
                "action": "find_game",
                "ia_game": "none",
                "player_id": self.player_id
            }))
        else:
            print("WebSocket is not connected.")

    def on_message(self, ws, message):
        data = json.loads(message)
        self.printDATA(data)
        if data["type"] == "connection_etalished":
            ws.send(json.dumps({
                "type": "auth",
                "session_id": self.player_id,
                "player_id": self.player_id
            }))

    def on_error(self, ws, error):
        self.printDATA(self, str(error))

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(self, ws):
        print("Opened connection")


client_a = Client("player1")
client_b = Client("player2")

thread_a = threading.Thread(target=client_a.run)
thread_b = threading.Thread(target=client_b.run)

thread_a.start()
thread_b.start()

time.sleep(2)
client_a.sendFindGame()
time.sleep(2)
client_b.sendFindGame()

thread_a.join()
thread_b.join()
