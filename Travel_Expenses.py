# Here we are gathering the number of times the user rode the bus last month
times_riding_the_bus = input('How many times did you ride the bus last month?')
# Here we are gathering the cost of one bus ride from the user
cost_of_one_bus_ride = input('What is the cost of one bus ride?')

# In this line we are multiplying the number of times riding the bus by cost of one bus ride
# This equation gives of the total cost of riding the bus for one month
total_cost_of_riding_the_bus = int(times_riding_the_bus) * float(cost_of_one_bus_ride)

# In this line we are printing how many times the user rode the bus, cost of one bus ride, and their total cost
# This data is print into a sentence form
print('You rode the bus ' + times_riding_the_bus + ' times last month. ' + 'One bus ride costs $'
      + cost_of_one_bus_ride + '. Our total cost was $' + str(total_cost_of_riding_the_bus))

