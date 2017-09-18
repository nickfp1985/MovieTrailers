import webbrowser


class Movie():
    """ stores movie info and produces trailers """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ stores movie info given in entertainment_center.py """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ opens the movie trailer when its poster is clicked """
        webbrowser.open(self.trailer_youtube_url)
