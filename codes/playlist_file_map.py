#Associate Playlist name with Filename
def playlist_file_mapping():
    playlist_name = []
    count=0
    for filename in sorted(filenames):
        file_path_name = os.sep.join((path,filename))
        f1 = open(file_path_name,'r')
        mpd_train = json.load(f1)
        for playlist in mpd_train['playlists']:
            count+=1
            print(count)
            mapping[normalize_name(playlist['name'])] = filename
            print(normalize_name(playlist['name']),filename)
    print('Loading into JSON file.....')
    fp = open('/home/irlab/files/mappings/track_filename.json','wb')
    json.dump(mapping,fp)
    print('Done')
    
playlist_file_mapping()    

