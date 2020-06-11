import customModule #importing the module I made
from emoji import emojize #will work when installed 
# pip install emoji 

#check whats inside the module
print(dir(customModule))

msg = "helloooooo woooorld"

#Using the module I imported's function

customModule.shoutAMsg(msg) #Will call the func from custommodule with the string

print(emojize(":snake: is :thumbs_up:"))