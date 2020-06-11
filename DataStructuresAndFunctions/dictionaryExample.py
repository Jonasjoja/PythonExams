users = {"name": "Jonas",
"age": "22",
"country": "Denmark"}

print(users["age"]) #provide key, gets value

    #How to iterate through the dict with a for loop
for value in users.values():
    print(value)


    #Iterate through it all using .items
for key,value in users.items():
    print(f"key is {key} and value is {value}")


    #Data modelling a "playlist" with dictionary and list nested. Would be cool to get from spotify api
playlist = {"title": "random playlist", 
"author": "Jonas",
"songs": [
    {"title" : "song1", "artist" : ["Really cool singer"], "duration": 3.0 },
    {"title" : "song2", "artist" : ["Really cool singer", "Also a really cool singer"], "duration": 4.1 },
    {"title" : "song3", "artist" : ["very not nice singer"], "duration": 10.5 }
]}

    #figure out how long the playlist is
totalPlaytime = 0
for song in playlist["songs"]:
    totalPlaytime += song["duration"]
print(f"The total playtime of your playlist is: {totalPlaytime}")

    #Dictionary comprehension
capitalizedUsers = { k.upper() : v.upper() for k,v in users.items()} #using a comprehension to create a new dict from users, but capitalized.
print(capitalizedUsers)

    #with conditional logic
print({num:("even" if num % 2 == 0 else "odd") for num in range(1,13)}) #this will set the key to the number and the value to odd or even
