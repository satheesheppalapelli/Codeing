value_input = str(input("Enter Any String:"))
value_size = len(value_input)
new_string = " "
while value_size:
    value_size -= 1
    new_string =  new_string + value_input[value_size]
print(new_string)