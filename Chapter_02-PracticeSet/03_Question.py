# Check the type of variable assigned using input() function.

user_input = input("Enter something: ")

input_type = type(user_input)

print("The type of the input is: ", input_type )

if type(user_input) == str:
    print("The input is a string.")
