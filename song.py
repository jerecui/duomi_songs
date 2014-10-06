"""
The song model

"""


class Song(object):
    title = None
    album = None
    artist = []

    def get_artist(self):
        return ",".join([a for a in self.artist])

    def simple_info(self):
        return "%s : <%s> by %s" % (self.title, self.album, self.get_artist())
