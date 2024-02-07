# recipe program
# grilled cheese sandwiches
bread_slices = 2
cheese_slices = 1
tomato_slices = 3

people = int(input('How many people want sandwiches?'))

# How many slices of bread are needed?
total_bread = bread_slices * people
print('You will need ' + str(total_bread) + 'slices of bread' )


# How much cheese?
# * symbol for multiplication
total_cheese = cheese_slices * people
print('You will need '+str(total_cheese) + 'slices of cheese')

# What about tomato slices?
total_tomato_slices = tomato_slices * people
print('You will need ' + str(tomato_slices) + 'tomato slices ')


# Let's ask for the number of people instead of writing the number 2

