## The Bug:
- there are 2 mistyped '==' signs that written as '=' that allow us to jump from coupon type to grocery and back.
- the second thing that we need to sed is the 'is_valid' variable of the coupon  in order to see the flag.
- luckily the writers used union, and that let us set the variable in grocery mode and read it as something as in      
- coupon mode.

## Solution:
- load coupon. (which load into list the coupon but dont show them)
- change the type of the second item to bread
- edit the amount of kilos to one (same position of is_valid),amount of loaves to 0, and amount of items to zero 
- now edit the second item again and thats it.
- show the items.