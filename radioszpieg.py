#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import config
import get_title
import database_mysql
import stations
import lastfm





radio = stations.radio
title_pomijanie = stations.title_pomijanie



pomin = 0

# print (radio[2]["service"])

for x in radio:
    # print(x)
    radio_name = str(x["radio"])
    radio_stream = str(x["stream"])
    radio_service = str(x["service"])

    if radio_service != "NULL":
        listeners = get_title.get_service(radio_service)
    else:
        listeners = 0
    # print(radio_name)
    song_title = get_title.get_shoutcast(radio_stream)
    for y in title_pomijanie:
        if song_title == y:
            pomin = 1

    if pomin == 0:
        song_title = song_title.replace("  ", " - ")
        song_title = song_title.replace(" - - ", " - ")
        # print(radio_name+': '+song_title)
        song_last = database_mysql.get_last_song(radio_name)
        # print(song_last)
        if song_last != song_title:
            # print("Nowy kawalek")
            songid = database_mysql.search_songid(song_title)
            if songid == 0:
                songid = database_mysql.get_maxsongid()
                # lastfm(song_title)
                lastfm.insert_lastfm_row(song_title, songid)


            database_mysql.insert(radio_name, song_title, listeners, songid)
    pomin = 0

