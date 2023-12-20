# Write a function called collect_makes. collect_makes should
# take as input one parameter, a list. Every item in the list
# will be a string.
#
# The strings will all represent the names of cars, such as
# "Mazda Miata", "Ford F150", and "Nissan Leaf". Every car
# will be given by a two-word name, with the first word being
# the car "make" (the brand) and the second word being the
# car "model" (the specific type of car). You may assume that
# we will only include one-word makes and one-word models;
# we won't include a Tesla Model S, Jeep Town & Country, etc.
#
# Your function should return a dictionary. The keys of the
# dictionary should be all the car makes found in the list.
# The values should be alphabetically-sorted lists of models
# found corresponding to the given makes.
#
# For example:
#
# car_list = ["Mazda Miata", "Ford F150", "Nissan Leaf",
#            "Ford Fusion", "Nissan Rogue", "Nissan Murano"]
# collect_makes(car_list) -> {"Mazda": ["Miata"],
#                            "Ford": ["F150, Fusion"],
#                            "Nissan": ["Leaf", "Murano", "Rogue"]}
#
# Remember, the order of dictionary keys does not matter.
# However, you should make sure the lists of car models
# is sorted alphabetically! (Notice that Murano is listed
# before Rogue under Nissan above.)


# Write your function here!
def collect_makes(car_data):
    result = {}
    for car in car_data:
        car = car.split()
        model = car[1]
        brand = car[0]
        if brand not in result:
            result[brand] = []
        result[brand].append(model)
        result[brand].sort()
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (with keys possibly in a different order):
# {"Mazda": ["Miata"], "Ford": ["F150, Fusion"], "Nissan": ["Leaf", "Murano", "Rogue"]}
car_list = [
    "Mazda Miata",
    "Ford F150",
    "Nissan Leaf",
    "Ford Fusion",
    "Nissan Rogue",
    "Nissan Murano",
]
print(collect_makes(car_list))
