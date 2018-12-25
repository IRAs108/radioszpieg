#!/usr/bin/env python

# coding: utf-8

from __future__ import print_function
import re
import struct
import urllib
from ast import literal_eval

import sys

try:
    import urllib2
except ImportError:  # Python 3
    import urllib.request as urllib2


def get_shoutcast(input):
    # url = 'http://stream4.nadaje.com:13322/radiobielsko'  # radio stream
    # url = str(sys.argv[1])
    url = str(input)
    # print(input)
    encoding = 'iso-8859-1'  # default: iso-8859-1 for mp3 and utf-8 for ogg streams
    request = urllib2.Request(url, headers={'Icy-MetaData': 1})  # request metadata
    response = urllib2.urlopen(request)
    # print(response.headers, file=sys.stderr)
    metaint = int(response.headers['icy-metaint'])
    for _ in range(4):  # # title may be empty initially, try several times
        response.read(metaint)  # skip to metadata
        metadata_length = struct.unpack('B', response.read(1))[0] * 16  # length byte
        metadata = response.read(metadata_length).rstrip(b'\0')
        # print(metadata, file=sys.stderr)
        # extract title from the metadata
        m = re.search(br"StreamTitle='([^']*)';", metadata)
        strm = metadata
        strm = '"'+str(metadata.decode(encoding))+'"'
        strm = str(strm)
        strm = strm[14:-3]
        # print(len(strm), file=sys.stderr)

        # print (len(strm))
        # print(strm)
        # strm = strm.replace("\'" "8")
        strm = strm.replace("';StreamUrl='","")
        # strm = strm.replace("StreamTitle=","")
        # strm = strm.replace(";", "")
        # strm = strm.replace("s'", "")
        if strm == "":
            strm="ERROR"

        # strm = strm.replace("'", "**")


        # print(strm, file=sys.stderr)
        # strm = strm.replace("b\"s'", "")
        if strm:
            title = strm
            if title:
                break
        else:
            title = "b'no title found'"
    # song = str(title.decode(encoding, errors='replace'))
    song = strm
    # song = title.decode("iso-8859-1")
    # song = song.encode("utf-8")
    # song = song[2:-1]
    return song

def get_service(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    mystr = mystr.replace("null", "\"NULL\"")
    mystr = literal_eval(mystr[1:-1])
    listeners = mystr["recipients_count"]
    return listeners