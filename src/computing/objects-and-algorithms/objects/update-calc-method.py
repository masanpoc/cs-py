# Previously, you wrote a class called ExerciseSession that
# had three attributes: an exercise name, an intensity, and a
# duration.
#
# Add a new method to that class called calories_burned.
# calories_burned should have no parameters (besides self, as
# every method in a class has). It should return an integer
# representing the number of calories burned according to the
# following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Medium", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
# You may copy your class from the previous exercise and just
# add to it.


# Add your code here!
class ExerciseSession:
    def __init__(self, name, intensity, length):
        self.name = name
        self.intensity = intensity
        self.length = length

    def get_exercise(self):
        return self.name

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.length

    def set_exercise(self, name):
        self.name = name

    def set_intensity(self, intensity):
        self.intensity = intensity

    def set_duration(self, length):
        self.length = length

    def calories_burned(self):
        burned_cals = None
        if self.intensity == "Low":
            burned_cals = 4 * self.length
        elif self.intensity == "Medium":
            burned_cals = 8 * self.length
        elif self.intensity == "High":
            burned_cals = 12 * self.length
        return burned_cals


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# 240
# 360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
