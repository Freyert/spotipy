import urllib2
import re
import json
import urllib

class Spotify:
	trackurl = "http://ws.spotify.com/search/1/track?%s"
	headers = [("Accept", "application/json")]
	opener = urllib2.build_opener()
	opener.addheaders = headers

	def search(self, artist="", track="", album=""):
		search = self._buildsearch(_artist=artist, _track=track, _album=album)
		print(search)
		try:
			jdata = json.loads(self.opener.open(search).read())
		except urllib2.HTTPError as error:
			jdata = {}
			print error
		return jdata
		


	def _buildsearch(self, _artist="", _track="", _album=""):
		fields = ['artist:', 'track:', 'album:']
		query = [_artist.strip(), _track.strip(), _album.strip()]
		query = filter(lambda a: a != "", query)
		searchdict = { 'q' : ''}
		for idx in range(len(query)):
			if(idx < len(query) - 1 and len(query) > 1):
				searchdict['q'] += fields[idx] + query[idx] + " AND "
			else:
				searchdict['q'] += fields[idx] + query[idx]
		return  self.trackurl % urllib.urlencode(searchdict)	
	
