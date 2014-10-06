# coding: utf-8
from worker import Worker


def main():
    w = Worker('1133079545973309867')
    songs = w.get_songs()
    print "\n".join([x.simple_info() for x in songs])


if __name__ == "__main__":
    main()
