import os
import json

input_data_dir = 'C:\\Users\\sotir\\Desktop\\ML Datasets\\spotify_million_playlist_datasets\\data\\'
output_data_dir = 'C:\\Users\\sotir\\PycharmProjects\\deitel\\'

with open(output_data_dir + "data.txt", "w", encoding='utf-8') as output:



    for filename in os.listdir(input_data_dir):
        if ('.json' in filename):
            filepath = input_data_dir + filename
            print(filepath)
            data = json.load(open(filepath))
            playlists = data["playlists"]
            for p in playlists:
                line = p["name"].lower()
                output.write(line+'\n')