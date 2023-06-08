class Viewer:
    
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        if isinstance(username,str) and 6 <= len(username) <=16:
            self._username = username
        else:
            raise AttributeError("Viewer.username must be a str")
    
    def reviews(self):
        return [review for review in Review.all if review.viewer == self]
    
    def reviewed_movies(self):
        pass
    
    def has_reviewed_movie(self, movie):
        pass

from classes.review import Review
from classes.movie import Movie