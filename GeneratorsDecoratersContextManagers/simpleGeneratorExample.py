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

#create a list
my_list = [1, 3, 6, 10]

#square each with list comprehension
list_ = [x**2 for x in my_list]

#same thing, but generator expression
#surrounded by () cause generator expr.
generator = (x**2 for x in my_list)

print(list_)
print(generator) #prints a generator object, then use next to iterate
print(next(generator))
print(next(generator)) #and so on