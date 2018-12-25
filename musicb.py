# Import the module
import musicbrainzngs
import database_mysql
import pymysql

db_host = "localhost"
db_user = "radioszpieg"
db_password = "ko1wa3le5s"
db_name = "radioszpieg"

# If you plan to submit data, authenticate
musicbrainzngs.auth("user", "password")

# Tell musicbrainz what your app is, and how to contact you
# (this step is required, as per the webservice access rules
# at http://wiki.musicbrainz.org/XML_Web_Service/Rate_Limiting )
musicbrainzngs.set_useragent("Example music app", "0.1", "http://example.com/music")
musicbrainzngs.set_hostname("beta.musicbrainz.org")

db = pymysql.connect(db_host, db_user, db_password, db_name)
cursor = db.cursor()
zapytanie = "select id from years order by id desc limit 1"
cursor.execute(zapytanie)
result = cursor.fetchone()
il_literacjiroz = result[0]
print (il_literacjiroz)


db = pymysql.connect(db_host, db_user, db_password, db_name)
cursor = db.cursor()
zapytanie = "SELECT id, artist, title FROM lastfm"
cursor.execute(zapytanie)
il_literacji = cursor.rowcount
# print(il_literacji)
for x in range(0, il_literacji):
    result = cursor.fetchone()
    # print(result)
    doszukania = result[1]+" - "+result[2]
    songid = result[0]
    if (songid>il_literacjiroz):
        print(doszukania)
        wynik = musicbrainzngs.search_recordings(doszukania)
        try:
            wynik = wynik['recording-list'][0]['release-list'][0]['date']
        except:
            wynik = "0000"
        print(wynik)
        database_mysql.insert_year(songid, wynik)

db.close()

# If you are connecting to a different server


# print(wynik["relase-list":"date"])
