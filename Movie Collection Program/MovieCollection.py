from Movie import Movie
from MovieCollectionNode import MovieCollectionNode

class MovieCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None

    def getNumberOfMovies(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertMovie(self, movie):
        temp = MovieCollectionNode(movie)
        current = self.head
        previous = None

        if previous == None and current == None:
            temp.setNext(current)
            self.head = temp
        elif previous == None and current.getData() > temp.getData():
            temp.setNext(current)
            self.head = temp
        else:
            while current != None and temp.getData() > current.getData():
                previous = current
                current = current.getNext()
            if current == None:
                previous.setNext(temp)
            else:
                previous.setNext(temp)
                temp.setNext(current)

    def getAllMoviesInCollection(self):
        current = self.head
        new_string = ""
        while current != None:
            new_string += current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return new_string

    def getMoviesByDirector(self, director):
        director = director.upper()
        current = self.head
        new_str = ""

        while current != None:
            if current.getData().getDirector().upper() == director:
                new_str = new_str + current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return new_str


    def removeDirector(self, director):
        current = self.head
        director = director.upper()
        previous = None

        if current == None:
            return
        previous = None

        while current != None:
            if current == self.head and current.getData().getDirector().upper() == director:
                temp = current.getNext()
                self.head = temp
                current = temp
            elif current.getData().getDirector().upper() == director:
                while current != None and current.getData().getDirector().upper() == director:
                    temp = current.getNext()
                    previous.setNext(temp)
                    current = current.getNext()
                if current != None:
                    previous.setNext(current)
                    previous = current
                    current = current.getNext()
                else:
                    previous.setNext(None)
            else:
                previous = current
                current = current.getNext()


    def avgDirectorRating(self, director):
        director = director.upper()
        current = self.head
        total_rating = 0.0
        count = 0
        while current != None:
            movie = current.getData()
            if movie.getDirector() == director and movie.getRating() != None:
                total_rating += movie.getRating()
                count += 1
            current = current.getNext()
        if count == 0:
            return None
        avg_rating = round(total_rating / count, 2)
        return avg_rating

    def recursiveSearchMovie(self, movieName, movieNode):
        found = False
        if movieNode == None:
            return found
        else:
            if movieNode.getData().getMovieName().upper() == movieName.upper():
                found = True
            else:
                return self.recursiveSearchMovie(movieName, movieNode.getNext())
        return found






