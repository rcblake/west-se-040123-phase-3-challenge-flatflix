class Viewer:
    
    all=[]
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    
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
        return [review.movie for review in self.reviews()]
    
    def has_reviewed_movie(self, movie):
        return movie in self.reviewed_movies()

from classes.review import Review
from classes.movie import Movie