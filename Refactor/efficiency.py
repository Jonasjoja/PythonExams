from memory_profiler import profile # used to line by line see memory usage
# python -m memory_profiler effiency.py
from time import time





    #BAD CODE
def imNotPretty():
    my_numbers = [1,2,3,4,5]
    odd_numbers = []
    for item in my_numbers:
        if item % 2 == 1:
            odd_numbers.append(item)
    return odd_numbers # [1, 3, 5]

#“Flat is better than nested”

# — Tim Peters, Zen of Python

    #REFACTORED USING LIST COMPREHENSION
    #FLAT.
def imQuitePretty():
    my_numbers2 = [1,2,3,4,5]
    odd_numbers2 = [item for item in my_numbers2 if item % 2 == 1]
    return odd_numbers2

#imNotEfficient()
#imEfficient()

@profile #Using a decorator to measure memory usage line by line
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_func() #doing memory intensive stufff


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


