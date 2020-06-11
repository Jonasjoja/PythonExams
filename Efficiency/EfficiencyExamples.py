while True:
    length = int(input("Enter the length: "))
    if length > 0:
        break

while True:
  width = int(input("Enter the width: "))
  if length > 0:
    break
print("The area is", length * width)

    #REFACTORED
def input_positive_integer(prompt):
    
      while True:
        input_value = int(input(prompt))
        if input_value > 0:
            return input_value


length = input_positive_integer("Enter the length: ")
width = input_positive_integer("Enter the width: ")
print("The area is", length * width)


    #BAD CODE
my_numbers = [1,2,3,4,5]
odd_numbers = []

for item in my_numbers:
  if item % 2 == 1:
    odd_numbers.append(item)
print(f"Im odd_numbers {odd_numbers}") # [1, 3, 5]

#“Flat is better than nested”

# — Tim Peters, Zen of Python

    #REFACTORED USING LIST COMPREHENSION
my_numbers2 = [1,2,3,4,5]
odd_numbers2 = [item for item in my_numbers2 if item % 2 == 1]
print(f"I'm odd_numbers2: {odd_numbers2}")