# movie class

class Movie:
    def __init__(self, movieName, director, year, rating=None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
        self.rating = rating
    def getMovieName(self):
        return self.movieName

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year

    def getRating(self):
        return self.rating

    def getMovieDetails(self):
        last_name, first_name = self.director.split(", ")
        director_formatted = "{} {}"\
            .format(first_name, last_name)
        return "{} directed by {} ({}), Rating: {}" \
            .format(self.movieName, director_formatted, self.year, self.rating)

    def __gt__(self, other):
        if self.director > other.director:
            return True
        elif self.director < other.director:
            return False
        else:
            if self.year > other.year:
                return True
            elif self.year < other.year:
                return False
            else:
                return self.movieName > other.movieName


