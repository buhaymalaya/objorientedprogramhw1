# How To Whiteboard
# 1. Read the problem out loud
# 2. Making any assumption, ask clarifying questions. (you are establishing good habits)
# 3. coming up with the approach (drawing pictures) (make sure you don't leave us, the viewers in the dust)
# 	- ideally, you can come up with a COUPLE solutions, evaluate their complexities/efficiency/then make your pick
# 4. Finally, write out the code
# 5. Debug / re-evaluate

# Emphasize what is actually being asked in the problem

# ----------- Even or Odd ----------
# DESCRIPTION:
# Create a function that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

# write a func that takes an int
# evaluate whether int is even or odd
# use if statement with modulo to check remainder
# return str "Even" or "Odd"

 # test cases : look at them before solving to ensure understanding of problem

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(109)) 