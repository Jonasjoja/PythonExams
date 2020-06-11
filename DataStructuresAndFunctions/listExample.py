#access all data in list with for loop
numbers = [1,2,3,4]

for number in numbers:
    print(number)

#access all data with while loop
#for loops is usually cleaner here, but while can be used if u need the index/do something at an index
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#Nested list - could be useful in games or if u want store coordinates etc
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
nested_list[0][1] #will access "2"
nested_list[1][-1] #will access "6"

#List comprehensions
nums= [1,2,3]
nums2 = [x*10 for x in nums]
print(nums2)

#Nested list comprehension
board = [[num for num in range(1,4)] for val in range(1,4)] #will be [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(board)

#List comprehension with conditional logic
nums3 = [1,2,3,4,5,6]
evens = [num for num in nums3 if num % 2 == 0]
odds = [num for num in nums3 if num % 2 != 0]