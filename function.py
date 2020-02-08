from baby_poll import get_initial
first_name = input ('please enter first name: ')
last_name = input ('Please enter last name: ')
print ("your baby's initials are: " + first_name.title() \
    + ' ' + get_initial(last_name))
# print(get_initial.__doc__)