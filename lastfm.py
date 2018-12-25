import pylast
import sys
import database_mysql
# coding: utf-8

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "api_key"  # this is a sample key
API_SECRET = "api_secret"

username = "lastfm_username"
password_hash = pylast.md5("lastfm_password")

def insert_lastfm_row(song, id):
    net_lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username,
                                      password_hash=password_hash)
    song = song.strip()
    song = song.split(" - ")
    wykonawca = song[0]
    try:
        utwor = song[1]
    except:
        print(song)
        utwor = "err"
    lfm_track = net_lastfm.get_track(wykonawca, utwor)

    try:
        lfm_listeners = lfm_track.get_listener_count()
    except:
        lfm_listeners = 0
    try:
        lfm_album = lfm_track.get_album()
    except:
        lfm_album = "None"
    try:
        lfm_cover = lfm_track.get_cover_image()
    except:
        lfm_cover = "None"
    try:
        lfm_url = lfm_track.get_url()
    except:
        lfm_url = "None"
    try:
        lfm_duration = lfm_track.get_duration()
    except:
        lfm_duration = 0
    try:
        lfm_mbid = lfm_track.get_mbid()
    except:
        lfm_mbid = "None"


# def insert_lastfm(id, artist, title, listeners, album, coverurl, url, duration, mbid):
    database_mysql.insert_lastfm(id, wykonawca, utwor, lfm_listeners, lfm_album, lfm_cover, lfm_url, lfm_duration, lfm_mbid)
    # print("Nowy utwór:")
    # print(id)
    # print(wykonawca)
    # print(utwor)
    # print(lfm_listeners)
    # print(lfm_album)
    # print(lfm_cover)
    # print(lfm_url)
    # print(lfm_duration)
    # print(lfm_mbid)
    # print("----")
