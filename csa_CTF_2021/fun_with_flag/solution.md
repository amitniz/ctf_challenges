# There are 2 bugs that allows us to get the flag.
# The first is that in the sell function the program set flag_to_sell out side of the loop,
# so it's possible to sell a flag and then enter a negative number that will cause selling the flag again and 
# gain twice the price (or even more). 
# The second bug is that the program dont check before deviding by zero, so we can hold only russia flag,
# which have zero stars and then try to buy CSA.