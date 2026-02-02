first_name = 'murali'
last_name = 'krishna'
country = 'India'
city = 'Hydrabad'
age = 17
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python','java']
person_info = {
    'firstname': 'Murali',
    'lastname': 'Krishna',
    'country': 'India',
    'city': 'Hydrabad'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Murali', 'Krishna', 'India', 17, 'False'

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)