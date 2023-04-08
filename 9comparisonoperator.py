#Comparison Operators
is_greater = 1 > 5
is_lesser = 1 < 5
# 1 <= 5
# 1 >= 5
is_not_equal = 1 != 5
is_equal = 1 == 5

#Logical Operators
# or -> (atleast one is true)
# and -> (both are true)
# not -> (reverses any value)

number = 2
print(number > 3)
print(number < 3)
print(not number > 3)
print(not number < 3)

print(number > 3 and number > 1)
print(number > 3 or number > 1)


#If statements
age = 13

if age >= 18:
   print("you are an adult")
   print("you can vote")
elif age < 3:
   print("you are a child")
else:
   print("you are in school")
print("thank you")
