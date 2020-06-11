def countUpTo(max):
    count = 1
    while count <= max:
        yield count
        count += 1


countUpTo(5) #This will return a generator object

counter = countUpTo(5)
print(counter) #this will show it returns a generator object
#u will have to use methods to iterate over it if u want data out

#Each time this will increase by 1
#It stores one thing at a time, the most recent one
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

