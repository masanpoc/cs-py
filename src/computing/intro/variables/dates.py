from datetime import date
import datetime

todays_date = date.today()
year = todays_date.year
month = todays_date.month
day = todays_date.day

# output YYYY/MM/DD
print(str(year) + "/" + str(month) + "/" + str(day))

# print("date", todays_date.day)
# print("time", current_time)


current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second = current_time.second

# output eg 13/5/14 (HH/M/S)
print(type(current_time.hour))
print(current_time.minute)
print(current_time.second)

print(str(hour) + ":" + str(minute) + ":" + str(second))

user_input = input("Enter a number: ")
print("Your original input: " + user_input)
user_input_as_float = float(user_input)
print("Your input as a float:", user_input_as_float)
user_input_as_int = int(user_input)
print("Your input as an integer:", user_input_as_int)
