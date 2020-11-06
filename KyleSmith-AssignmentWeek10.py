import os

# Specify the path
print('Please sepcify the final folder path with / in between each folder name:')
path = input()
  
# Specify the file name
print('What would you like to name the text file?')
filename = input()+'.txt'

print('What is your name?')
user_name = input()
print('What is your address?')
user_address = input()
print('What is your phone number?')
user_phone = input()
  
# Creating a file at specified location 
with open(os.path.join(path, filename), 'w') as fp: 
    fp.write(user_name+', '+user_address+', '+user_phone) 

print('The text file has been created in', path, 'take a look!')

