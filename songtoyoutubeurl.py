import math
from pytube import Search


class SongToYoutubeUrl:
    def video_id(title, artist, length):
        query = title + " " + artist
        search = Search(query)

        # if no length is input, return first search result
        if length == None:
            return search.results[0].video_id

        # otherwise, return search result which best matches length
        best_video_id = None
        minimum_length_difference = math.inf
        
        for result in search.results:
            length_difference = abs(length - result.length)

            if length_difference < minimum_length_difference:
                minimum_length_difference = length_difference
                best_video_id = result.video_id

        return best_video_id

    def url(title, artist, length):
        video_id = SongToYoutubeUrl.video_id(title, artist, length)
        return "https://www.youtube.com/watch?v=" + video_id
