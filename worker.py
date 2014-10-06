"""
get songs from internet
"""

import song
import urllib2
import json


class Worker(object):

    """docstring for duomi_songlist"""

    list_id = 1
    _format_url = "http://www.duomi.com/media-getsong?listid=%s&pi=1&pz=%s&_=282499981&lckey="
    _tug_url = None
    url = None
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml; \
        q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "text/html",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://www.baidu.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
    }

    def __init__(self, list_id):
        super(Worker, self).__init__()
        self.list_id = list_id
        self._tug_url = self._format_url % (list_id, 1)
        self.url = self._format_url % (list_id, 100)

    def get_content(self, url):
        req = urllib2.Request(url, None, self.headers)

        response = urllib2.urlopen(req)
        html = response.read()
        content = json.loads(html)

        return content

    def get_total(self):
        print 'get your total music count..'

        content = self.get_content(self._tug_url)
        total = content["response"]["total"]
        return total

    def get_songs(self):
        total = self.get_total()
        # total = 2
        self.url = self._format_url % (self.list_id, total)

        content = self.get_content(self.url)
        trackers = content["response"]["listtracks"]

        songs = []

        for item in trackers:
            tracker = item["track"]
            s = song.Song()
            s.parse_tracker(tracker)

            songs.append(s)

        return songs
