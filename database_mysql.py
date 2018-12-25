#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

db_host = "localhost"
db_user = "db_user"
db_password = "db_password"
db_name = "db_name"


def get_last_song(radio):
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "SELECT song FROM historia WHERE radio=\"" + radio + "\" ORDER BY id DESC LIMIT 1"
    cursor.execute(zapytanie)
    data = cursor.fetchone()
    db.close()
    last_song = data
    if cursor.rowcount == 0:
        last_song = "INIT"
    else:
        last_song = data[0]
    # print(last_song)
    return last_song


def insert(radio, song, listeners, songid):
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "INSERT INTO historia (radio, song, listeners, song_id) VALUES (\"" + radio + "\", \"" + song + "\", " + str(
        listeners) + ", " + str(songid) + ")"
    cursor.execute(zapytanie)
    db.commit()
    db.close()


def get_maxsongid():
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "select song_id from historia where  song_id is not NULL ORDER BY ABS(song_id) DESC LIMIT 1;"
    cursor.execute(zapytanie)
    data = cursor.fetchone()
    db.close()
    if cursor.rowcount == 0:
        ust_songid = 1
    else:
        ust_songid = int(data[0])
        ust_songid = ust_songid + 1
        # lastfm search
        # print(ust_songid)
    return ust_songid


def search_songid(utw_zm):
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "select song_id from historia where song=\"" + utw_zm + "\" and song_id is not null limit 1"
    cursor.execute(zapytanie)
    data = cursor.fetchone()
    db.close()
    if cursor.rowcount == 0:
        songid = 0
    else:

        songid = int(data[0])
    return songid


def insert_lastfm(idt, artist, title, listeners, album, coverurl, url, duration, mbid):
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "INSERT INTO lastfm (id, artist, title, listeners, album, coverurl, url, duration, mbid) VALUES (" + str(idt) + ", \"" + str(artist) + "\", \"" + str(title) + "\", " + str(listeners) + ", \"" + str(album) + "\", \"" + str(coverurl) + "\", \"" + str(url) + "\", " + str(duration) + ", \"" + str(mbid) + "\")"
    cursor.execute(zapytanie)
    db.commit()
    db.close()

def insert_year(songid, date):
    db = pymysql.connect(db_host, db_user, db_password, db_name)
    cursor = db.cursor()
    zapytanie = "INSERT INTO years (id, date) VALUES (" + str(songid) + ", '" + str(date) + "')"
    cursor.execute(zapytanie)
    db.commit()
    db.close()
