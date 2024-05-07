# ======== MATCH TO BLOCKCHAIN ==========
from client_connect import alreadyInWaiting, reconnectionTest, oneRoom, twoRoom, fiveRoom, tenRoom


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

# ======== MATCH RESULT TO ROOM MANAGER ==========

#alreadyInWaiting()
#reconnectionTest()
#oneRoom()
#twoRoom()
#fiveRoom()
#tenRoom()
