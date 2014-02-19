from spotifyapi import Spotify
import csv
import Queue
import threading
import time

sp = Spotify()
		


with  open("/home/fulton/Dropbox/Programming/Python/spotify/marketplaylist/nodupeslite.csv") as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(1024))
	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	out = open("./playlist.txt", "wb+")
	for row in reader:
		jdata = sp.search(artist=row[0], track=row[1])
		if 'tracks' in jdata:
			if len(jdata['tracks']) > 0:
				print jdata['tracks'][0]['name']
				out.write(jdata['tracks'][0]['href'])
				out.write("\n")
		time.sleep(0.15)
				



