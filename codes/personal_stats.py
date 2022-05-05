# Find frequency of artist, track and album
# Store in files :
# artist_stats.json, album_stats.json, tracks_stats.json
# These files contains the frequency of artists, albums and tracks

import json
import os
import pickle
import collections

artist_uri_freq = collections.Counter()
tracks_uri_freq = collections.Counter()
album_uri_freq = collections.Counter()
map_artist_uri = {}
map_tracks_uri = {}
map_album_uri = {}

def ordering_tracks():
    #Change this as per directory
    path = '/home/irlab/Documents/recsys/mpd/data'
    filenames = os.listdir(path)
    count=1
    for filename in  sorted(filenames):
        file_name = os.sep.join((path,filename))
        js = open(file_name)
        mpd = json.load(js)
        for playlist in mpd['playlists']:
            print(count) 
            arrange_playlist(playlist)
            count+=1
            
def arrange_playlist(playlist):
    tracks = playlist['tracks']
    for track in tracks:
        artist_uri_freq[track['artist_uri']]+=1
        tracks_uri_freq[track['track_uri']]+=1
        album_uri_freq[track['album_uri']]+=1
        if track['artist_uri'] not in map_artist_uri.keys():
            map_artist_uri[track['artist_uri']] = track['artist_name']
            #print(track['artist_name'])
        
        if track['track_uri'] not in map_tracks_uri.keys():
            map_tracks_uri[track['track_uri']] = track['track_name']
            #print(track['track_name'])
            
        if track['album_uri'] not in map_album_uri.keys():
            map_album_uri[track['album_uri']] = track['album_name']
            #print(track['album_name'])

ordering_tracks()

with open('/home/irlab/Documents/recsys/mpd/codes/artist_stats.json','w') as file1:
     json.dump(artist_uri_freq,file1)

with open('/home/irlab/Documents/recsys/mpd/codes/album_stats.json','w') as file1:
     json.dump(album_uri_freq,file1)

with open('/home/irlab/Documents/recsys/mpd/codes/tracks_stats.json','w') as file1:
     json.dump(tracks_uri_freq,file1)

with open('/home/irlab/Documents/recsys/mpd/codes/artist_mapping.json','w') as file1:
     json.dump(map_artist_uri,file1)
     
with open('/home/irlab/Documents/recsys/mpd/codes/tracks_mapping.json','w') as file1:
     json.dump(map_tracks_uri,file1)

with open('/home/irlab/Documents/recsys/mpd/codes/album_mapping.json','w') as file1:
     json.dump(map_album_uri,file1)
