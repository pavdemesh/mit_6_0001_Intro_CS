# find integers: root and 0 < pwr < 6, such that root ** pwr == num
# Two base solutions:   pwr == 0 works only if num = 1
#                       pwr == 1 works, in this case root == num

# Get int from user
num = int(input("Enter an integer: "))

# Boolean variable to reflect the fact if the root and pwr are found or not
found = False

# Two base solutions:   pwr == 0 works only if num = 1
#                       pwr == 1 works, in this case root == num

# These are not the solutions we are interested in
# That is why we start with the pwr == 2 and go up
pwr = 2

# Repeat until pwr is less than 6
while pwr < 6:

    # Start with root of 2, cause we again are not interested in 0 and 1 cases
    root = 2

    # Start inner loop, increasing root by 1 and comparing root ** pwr against num
    while root ** pwr < num:
        root += 1
    # We arrive at this line if root ** pow >= num
    # In this case we check if equality: we set found to True and break out of the inner loop
    if root ** pwr == num:
        found = True
        break

    # We arrive here in two cases: either by break in the inner loop
    # Or if root ** pwr for the current inner loop was greater than num
    # And this means that for current pwr there is no root, s.t. root ** pwr == num
    # If found - break out of the outer loop
    if found:
        break
    # Else: increment pwr by 1
    else:
        pwr += 1

# After the loop finishes
# If found is True: print root and pwr
if found:
    print(f"root is {root} and pwr is {pwr}")
# If not found: print appropriate message
else:
    print("No such root and pwr found")
