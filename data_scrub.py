import csv
import mariadb
import sys
from googletrans import Translator

try:
    conn = mariadb.connect(
        user="REDACTED",
        password='REDACTED',
        host="localhost",
        database="board_games"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

data_file = "BGGdata.csv"

fields = []
rows = []
name_fields = []
other_fields = {}
board_games = {}

with open(data_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

for field in fields:
    if "name" in field:
        name_fields.append(fields.index(field))

required_fields = {
        1: "average",
        5: "weight",
        7: "minplayers",
        8: "maxplayers",
        9: "playingtime",
        17: "yearpublished",
        161: "description",
        162: "thumbnail"
}

other_fields = {
        37: "designer0",
        38: "designer1",
        47: "artist0",
        48: "artist1",
        57: "subdomain0",
        58: "subdomain1",
        59: "subdomain2",
        60: "category0",
        61: "category1",
        62: "category2",
        63: "category3",
        64: "category4",
        65: "category5",
        66: "category6",
        67: "category7",
        68: "category8",
        69: "category9",
        70: "mechanic0",
        71: "mechanic1",
        72: "mechanic2",
        73: "mechanic3",
        74: "mechanic4",
        75: "mechanic5",
        76: "mechanic6",
        77: "mechanic7",
        78: "mechanic8",
        79: "mechanic9",
        80: "family0",
        81: "family1",
        82: "family2",
        83: "family3",
        84: "family4",
        85: "family5",
        86: "family6",
        87: "family7",
        88: "family8",
        89: "family9",
        90: "publisher0",
        91: "publisher1"
}

translator = Translator()

for row in rows[15341:]:
    print(row[0])
    found = False
    game_name = ""
    board_game = []
    for field in name_fields:
        if row[field] != '' and row[field].isascii():
            s = translator.detect(row[field])
            if s.lang == "en" and found == False:
                try:
                    sub_s = translator.detect(row[field].split(':')[1])
                    if sub_s.lang == "en":
                        game_name = row[field]
                        found = True
                except IndexError:
                    game_name = row[field]
                    found = True
    if game_name == "" and found == False:
        board_game.append(row[0])
    else:
        board_game.append(game_name)
    for field in required_fields.keys():
        if row[field] == "":
            board_game.append(None)
        else:
            board_game.append(row[field])
    for field in other_fields.keys():
        if row[field] == "":
            board_game.append(None)
        else:
            board_game.append(row[field])
    try:
        cur.execute("""INSERT INTO games  
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,NEXTVAL(game_id))""",
            board_game
        )
        try:
            print(f"Committing {board_game[0]}")
            conn.commit()
        except Error:
            pass
    except mariadb.DatabaseError.DataError:
        pass

