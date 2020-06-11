months = ("January","February","March","April","May","June","July","August") #tuple
#accessible by
print(months[0]) #January

#iterate with for loop
for month in months:
    print(month)

#Tuples could be used as a key in a dictionary, like to store coordinates
locations = {
    (34.213, 40.213) : "Random location 1",
    (12.123, 32.211) : "Random location 2"
}
 #Only methods you get with tuple is count //How many times an item is in the tuple
 # and index, tells which index a given value is found in the tuple


        # SET

s = {1,5,10,15,5,5} #duplicates on purpose - It could be useful to figure out how many unique countries/cities have signed up to something
print(f"printing the set, it will remove the duplicates: {s} ")
#Access all values with a for loop if want
# use .add() to add values to set, .discard to remove without worry of errors, copy to make a copy

