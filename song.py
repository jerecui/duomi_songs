"""
The song model

"""


class Song(object):
    title = None
    album = None
    album_cover_url = None
    artist = []
    url = []

    def parse_tracker(self, tracker):
        """
        the tracker example is:

        "track":{"album":{
                        "cover":"\/p1\/10\/10\/71286742.jpg",
                        "id":2564947,
                        "name":"Moodswings"
                        },
                "artists":[{
                        "id":61595317,
                        "name":"Maxine Ashley",
                        "num_albums":0,
                        "num_tracks":0,
                        "portrait":"\/p1\/28\/04\/70882024.jpg",
                        "valid":true
                }],
                "availability":"1110",
                "dlyric":"",
                "down_media_ids":null,
                "duration":215,
                "id":26866794,
                "lyric":"",
                "medias":[{
                        "format":"m4a",
                        "id":201188450,
                        "size":1820672,
                        "url":"m4a_64\/24\/09\/26866794_4325.m4a?type=0&pos=1"
                        }],
                "mv":0,
                "popularity":4,
                "ring_id":201188456,
                "slyric":"",
                "streaming_media_ids":[201188450],
                "title":"Between You and I"}


        """
        self.title = tracker["title"]

        if tracker.get('artists'):
            self.artist = [a["name"]
                           for a in tracker["artists"] if a.get('name')]

        if tracker.get('album'):
            if tracker['album'].get('name'):
                self.album = tracker["album"]["name"]
            if tracker['album'].get('cover'):
                c = tracker['album']['cover']
                if (c and c[0] == '/'):
                    c = c[1:]
                self.album_cover_url = 'http://pic.cdn.duomi.com/%s' % c

        if tracker.get('medias'):
            self.url = ["http://m1.app.duomiyy.com/%s" % a["url"]
                        for a in tracker.get('medias') if a.get('url')]

    def get_artist(self):
        return ",".join([a for a in self.artist])

    def simple_info(self):
        return "%s : <%s> by %s" % (self.title, self.album, self.get_artist())

    def detail_info(self):
        return "%s : <%s> by %s --> %s  [%s]" % (self.title, self.album, self.get_artist(), ','.join(self.url), self.album_cover_url)
