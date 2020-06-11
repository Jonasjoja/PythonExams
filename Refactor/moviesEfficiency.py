import cProfile, pstats, io

def profile(fnc): #Defining decorator
    
    """A decorator that uses cProfile to profile a function"""
    #this code snippet is taken from pythons docs
    #https://docs.python.org/3/library/profile.html#profile.Profile
    
    def inner(*args, **kwargs):
    
        pr = cProfile.Profile() 
        pr.enable()#start the profiler
        retval = fnc(*args, **kwargs) #execute the function
        pr.disable() #stop the profiler
        s = io.StringIO() #get the results and below print it out
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval #return the returnval of the executed func, in this case the duplicate list

    return inner


def readMovies(src):#read all the titles from file and splits by line.
    with open(src) as fd: #Opening with contextmanager
        return fd.read().splitlines()

def isDuplicate(needle,haystack): #movietitle is needle, other movie titles as haystack. then checks for duplicates
    for movie in haystack:
        #if needle.lower() == movie.lower():  <-- this is the old, inefficient way
        if needle == movie: #to be case insensivitve
            return True
    return False

@profile
def findDuplicateMovies(src='movies.txt'):

    movies = readMovies(src)
    movies = [movie.lower() for movie in movies] #Do a list comprehension here instead converts each movie to lowercase. 
    #Means it only has to be done as many times as there's movies.
    duplicates = [] #empty list for the duplicates
    while movies:
        movie = movies.pop() #Popping, takes index -1 as default
        if isDuplicate(movie, movies): #checks if its a duplicate, it it is, append
            duplicates.append(movie)
    return duplicates

findDuplicateMovies()
