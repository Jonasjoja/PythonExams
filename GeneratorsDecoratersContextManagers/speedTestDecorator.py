#Defining a speedtest decorator
from functools import wraps
from time import time

def speedtest(fn):
    def wrapper(*args,**kwargs):
        startTime = time() #Capturing the start time
        result = fn(*args,**kwargs) #running the code, whatever the function is
        endTime = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed:  {endTime - startTime}")
        return result

    return wrapper

#Using the decorator to speedtest this
#Should be noted its not the most accurate benchmark, doesnt take in account memory etc
@speedtest
def sumNumsGen():
    return sum(x for x in range(50000000))

@speedtest
def sumNumsList():
    return sum([x for x in range(50000000)])


#Returns the same number but will show a time difference
print(sumNumsGen())
print(sumNumsList())

