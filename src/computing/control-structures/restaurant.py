item = "quesadilla"
meat = "steak"
queso = True
guacamole = True
double_meat = True


# -----------------------------------------------------------
# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Let's further expand our previous program to cover a broader
# menu variety. Instead of just burritoes, now the program
# should cover three menu

# items: quesadillas, burritoes, nachos
# booleans(+0.5): "steak", "pork"
# booleans(+0): "chicken", "tofu", "beef",
# booleans(+1): "queso" and items != nachos, "guacamole",
# booleans: "double meat" +1.5 if steak/pork or +1 otherwise


# We still have booleans for
# queso and guacamole, but we also have a boolean for double
# meat.
#
# Your code should calculate the price as follows:
#
# - The base price for a quesadilla is 4.00, for nachos is
#   4.50, and for burritoes is 5.00.
# - If meat is steak or pork, add 0.50. Any other meat adds
#   no money to the price.
# - guacamole always adds 1.00 to the price.
# - queso adds 1.00 to the price UNLESS the item is nachos,
#   in which case it adds nothing.
# - double_meat adds 1.50 if the meat is steak or pork, or
#   1.00 otherwise.


base_price = 4.5
if item == "quesadilla":
    base_price = 4.0
elif item == "burrito":
    base_price = 5.0

if meat == "steak":
    base_price += 0.50
if meat == "pork":
    base_price += 0.50
elif meat == "steak" and double_meat:
    base_price += 1.50
elif meat == "pork" and double_meat:
    base_price += 1.50
elif double_meat:
    base_price += 1.0

if guacamole:
    base_price += 1.0

if queso and not "nachos":
    base_price += 1.0

print(base_price)
