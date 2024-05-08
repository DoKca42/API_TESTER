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
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp("ws://localhost:8000/ws/room/",
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

    def sendFindGame(self):
        self.ws.send(json.dumps({
            "type": "matchmaking",
            "action": "find_game",
            "ia_game": "none",
            "player_id": self.player_id
        }))

    def sendFindTour(self):
        self.ws.send(json.dumps({
            "type": "matchmaking",
            "action": "find_tournament",
            "ia_game": "none",
            "player_id": self.player_id
        }))

    def close_connection(self):
        if self.ws:
            self.ws.close()
            self.printDATA("Connection closed.")
        else:
            self.printDATA("No active connection to close.")

    def reopen_connection(self):
        self.printDATA("Reopening connection...")
        self.connect()


def buildClient(clients, threats, max_clients, post):
    for i in range(max_clients):
        clients.append(Client(post + str(i)))

    for i in range(max_clients):
        threats.append(threading.Thread(target=clients[i].run))

    for i in range(max_clients):
        threats[i].start()


def joinClient(threats, max_clients):
    for i in range(max_clients):
        threats[i].join()


def leaveClient(clients, threats, max_clients):
    for i in range(max_clients):
        clients[i].close_connection()


# ====== TESTS =====

def alreadyInWaiting():
    clients = []
    threats = []
    max_player = 1

    buildClient(clients, threats, max_player, "playerA_")
    time.sleep(2)
    clients[0].sendFindGame()
    time.sleep(2)
    clients[0].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def reconnectionTest():
    clients = []
    threats = []
    max_player = 1

    buildClient(clients, threats, max_player, "playerB_")
    time.sleep(2)
    clients[0].sendFindGame()
    time.sleep(2)
    clients[0].close_connection()
    time.sleep(2)
    clients[0].reopen_connection()
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def oneRoom():
    clients = []
    threats = []
    max_player = 2

    buildClient(clients, threats, max_player, "playerC_")
    time.sleep(2)
    clients[0].sendFindGame()
    time.sleep(2)
    clients[1].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def twoRoom():
    clients = []
    threats = []
    max_player = 4

    buildClient(clients, threats, max_player, "playerD_")
    time.sleep(2)
    clients[0].sendFindGame()
    time.sleep(2)
    clients[1].sendFindGame()
    time.sleep(2)
    clients[2].sendFindGame()
    time.sleep(2)
    clients[3].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def fiveRoom():
    clients = []
    threats = []
    max_player = 10

    buildClient(clients, threats, max_player, "playerE_")
    for i in range(max_player):
        time.sleep(2)
        clients[i].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def tenRoom():
    clients = []
    threats = []
    max_player = 20

    buildClient(clients, threats, max_player, "playerF_")
    for i in range(max_player):
        time.sleep(1)
        clients[i].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def fiftyRoom():
    clients = []
    threats = []
    max_player = 100

    buildClient(clients, threats, max_player, "playerG_")
    for i in range(max_player):
        time.sleep(0.5)
        clients[i].sendFindGame()
    time.sleep(5)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)


def joinTour():
    clients = []
    threats = []
    max_player = 4

    buildClient(clients, threats, max_player, "playerH_")
    for i in range(max_player):
        time.sleep(0.25)
        clients[i].sendFindTour()
    time.sleep(4)
    leaveClient(clients, threats, max_player)
    joinClient(threats, max_player)
