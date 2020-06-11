
from contextlib import contextmanager #to decorate a generator function


    #This would be how to do it without a context manager, manually closing the file
# f = open('sampleTxt.tx','w')
# f.write('I am gonna write to this text file')
# f.close() #closing it


    #Doing it with a context manager, keyword with
    #Means I no longer have to close the file myself
    #If it throws an error it will also close down properly

# with open('sampleTxt.txt','w' ) as f:
#    f.write('I am writing to the file!')

#Great for files, but also very useful to connect to and close database for example


    #Custom contextmanager
class Open_File():

    def __init__(self, fileName,mode):
        self.fileName = fileName
        self.mode = mode

    def __enter__(self): #setup of contextmanager
        self.file = open(self.fileName, self.mode)

        return self.file #return the object to work with within the contextmanager

    #the extra parameters are there if an exception is to be thrown
    def __exit__(self, exc_type, exc_val, traceback): #teardown of contextmanager
        self.file.close() #to close the file

with Open_File('sampleTxt.txt','w') as f: #runs init, enter
    f.write('Writing from custom contextmanager') #when this block is exited, it runs exit method

print(f.closed)#check if the file is in fact closed outside of the contextmanager
#should print true.


@contextmanager #decorator
def Open_File_CntxManager(file,mode):
    #try and finally will make sure if any errors, finally will still be run
    try:
        h = open(file,mode)
        yield h
    finally:
        h.close()

#Using the with statement to call generator function
with Open_File_CntxManager('sampleTxt2.txt','w') as h:
    h.write('Written with use of @contextmanager decorator')

print(h.closed) #should be true cause file should be closed.

