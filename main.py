# ======== MATCH TO BLOCKCHAIN ==========
from AllClass import postMatch_ToBC, Uniqid, postMatch_ToRM
from client_connect import alreadyInWaiting, reconnectionTest, oneRoom, twoRoom, fiveRoom, tenRoom, fiftyRoom, joinTour


def match_ToBC(match_id):
    data_json_raw = {
        "match_id": match_id,
        "tournament_id": 0,
        "player1_score": 0,
        "player2_score": 10,
        "player1_id": 12348546545,
        "player2_id": 12348546545,
        "winner_id": 12348546545,
        "timestamp": 12348546545
    }
    return data_json_raw


# postMatch_ToBC(match_ToBC(1035))
# postMatch_ToBC(match_ToBC(1036))
# postMatch_ToBC(match_ToBC(1037))
# postMatch_ToBC(match_ToBC(1037))
# postMatch_ToBC(match_ToBC(1038))

# ======== TOURNAMENT RESULT TO ROOM MANAGER ==========
def tour_ToRM(id_match, tournament, p_a, p_b):
    data_json_raw = {
        "match_id": id_match,
        "tournament_id": tournament,
        "player1_score": 0,
        "player2_score": 10,
        "player1_id": p_a,
        "player2_id": p_b,
        "winner_id": p_b
    }
    return data_json_raw

joinTour()

tour_id, pA, pB, pC, pD = "275317150979901770", Uniqid.generate(), Uniqid.generate(), Uniqid.generate(), Uniqid.generate()

postMatch_ToRM(tour_ToRM("297917151745654778", tour_id, pA, pB))
postMatch_ToRM(tour_ToRM("795017151745654737", tour_id, pC, pD))
postMatch_ToRM(tour_ToRM("357917151745654735", tour_id, pB, pD))


# ======== MATCH RESULT TO ROOM MANAGER ==========
def match_ToRM(id_match, p_a, p_b):
    data_json_raw = {
        "match_id": id_match,
        "tournament_id": 0,
        "player1_score": 0,
        "player2_score": 10,
        "player1_id": p_a,
        "player2_id": p_b,
        "winner_id": p_b
    }
    return data_json_raw


# id_already_exist = Uniqid.generate()
# postMatch_ToRM(match_ToRM(id_already_exist, Uniqid.generate(), Uniqid.generate()))
# postMatch_ToRM(match_ToRM(id_already_exist, Uniqid.generate(), Uniqid.generate()))
# postMatch_ToRM(match_ToRM(Uniqid.generate(), Uniqid.generate(), Uniqid.generate()))
# postMatch_ToRM(match_ToRM(Uniqid.generate(), Uniqid.generate(), Uniqid.generate()))

# ======== MATCHMAKING TO ROOM MANAGER ==========

#alreadyInWaiting()
#reconnectionTest()
#oneRoom()
#twoRoom()
#fiveRoom()
#tenRoom()
#fiftyRoom()

