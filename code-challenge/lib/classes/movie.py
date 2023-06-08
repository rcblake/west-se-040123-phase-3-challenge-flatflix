from statistics import mean

class Movie:
    
    all=[]
    
    def __init__(self, title):
        self.title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and title[0]:
            self._title = title
        else:
            raise AttributeError("Move.title must be a str")
    
    def reviews(self):
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        return list({review.viewer for review in self.reviews()})
    
    def average_rating(self):
        return mean(review.rating for review in self.reviews())
    
    @classmethod
    def highest_rated(cls):
        pass
    
from classes.review import Review
from classes.viewer import Viewer
