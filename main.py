import sys
from songtoyoutubeurl import SongToYoutubeUrl


def main():
    if len(sys.argv) < 2:
        print("usage: main.py <title> [artist] [length (seconds)]")
        exit(1)

    title = sys.argv[1]

    if len(sys.argv) > 2:
        artist = sys.argv[2]
    else:
        artist = ""

    if len(sys.argv) > 3:
        length = sys.argv[3]
        try:
            length = int(length)
        except ValueError:
            print(f"Length '{length}' is not a valid length in seconds. Please try again.")
            exit(1)
    else:
        length = None

    url = SongToYoutubeUrl.url(title, artist, length)
    print("Found url:", url)


if __name__=="__main__":
    main()
