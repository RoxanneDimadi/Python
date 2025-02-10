import pytest
from Movie import Movie
from MovieCollectionNode import MovieCollectionNode
from MovieCollection import MovieCollection

# test for Movie
def test_getMovieDetails():
    m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    m2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
    assert m1.getMovieDetails() == "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4"
    assert m2.getMovieDetails() == "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: None"


def test_Movie_initialization():
    m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    assert m1.getMovieName() == "THE GODFATHER"
    assert m1.getDirector() == "DARABONT, FRANK"
    assert m1.getYear() == 1972
    assert m1.getRating() == 9.4

def test__gt__():


    # test MovieCollection Node
    def test_node_initialization(node, movie):
        m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
        assert node.getData() == m1
        assert node.getNext() is None

    def test_get_next(node):
        assert node.getNext() is None

    def test_set_data(node):
        m2 = Movie("The Shawshank Redemption", "Darabont, Frank", 1994, 9.3)
        node.setData(m2)
        assert node.getData() == m2


    def test_set_next(self, node, m0):
        m0 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
        new_node = MovieCollectionNode(m0)
        node.setNext(new_node)
        assert node.getNext() == new_node



# test moviecollection class
def test_isEmpty():
    mc = MovieCollection()
    assert mc.isEmpty() == True

def test_getNumberOfMovies():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    m3 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m4 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    mc.insertMovie(m4)
    assert mc.getNumberOfMovies() == 5

def test_getAllMoviesInCollection():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    m3 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m4 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    mc.insertMovie(m4)
    assert mc.getAllMoviesInCollection() == """CITY LIGHTS directed by CHARLIE CHAPLIN (1931), Rating: 9.0
MODERN TIMES directed by CHARLIE CHAPLIN (1936), Rating: 8.9
CASABLANCA directed by MICHAEL CURTIZ (1942), Rating: 8.8
2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: 9.2
THE MATRIX directed by LANA WACHOWSKI (1999), Rating: 9.1\n"""

def test_getMoviesByDirector():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    m3 = Movie("Work", "Chaplin, Charlie", 1915, 6.2)
    m4 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m5 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)
    m6 = Movie("The Champion", "Chaplin, Charlie", 1915, 6.7)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    mc.insertMovie(m4)
    mc.insertMovie(m5)
    mc.insertMovie(m6)
    assert mc.getMoviesByDirector("Chaplin, Charlie") == """THE CHAMPION directed by CHARLIE CHAPLIN (1915), Rating: 6.7
WORK directed by CHARLIE CHAPLIN (1915), Rating: 6.2
CITY LIGHTS directed by CHARLIE CHAPLIN (1931), Rating: 9.0
MODERN TIMES directed by CHARLIE CHAPLIN (1936), Rating: 8.9\n"""




def removeDirector(self, director):
    director = director.upper()
    current = self.head
    previous = None

    while current:
        if current.getData().getDirector().upper() == director:
            if previous:
                previous.setNext(current.getNext())
            else:
                self.head = current.getNext()
            current = current.getNext()
        else:
            previous = current
            current = current.getNext()



def test_removeDirector():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    m3 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m4 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    mc.insertMovie(m4)

    mc.removeDirector("Chaplin, Charlie")
    assert mc.getAllMoviesInCollection() == "CASABLANCA directed by MICHAEL CURTIZ (1942), Rating: 8.8\n2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: 9.2\nTHE MATRIX directed by LANA WACHOWSKI (1999), Rating: 9.1\n"


def test_avgDirectorRating():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    m3 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    assert mc.avgDirectorRating("Chaplin, Charlie") == 8.95
    assert mc.avgDirectorRating("Curtiz, Michael") == 8.8

def test_recursiveSearchMovie():
    m0 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
    m2 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
    m3 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.8)

    mc = MovieCollection()
    mc.insertMovie(m0)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    assert mc.recursiveSearchMovie("Modern times", mc.head) == True
    assert mc.recursiveSearchMovie("The Matrix", mc.head) == False