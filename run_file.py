from restaurant_functions import *


user_food = input('What do you want to eat?\n')
user_file = input('Name your order so we can identify you\n')

write_to_file(user_food, user_file)

print(open_and_print(user_file).count)
