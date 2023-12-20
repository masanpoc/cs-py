# Write a function called write_nhl_teams. write_nhl_teams will
# take as input two parameters: a string and a list of 5-tuples.
#
# The string will represent the filename to which to write.
#
# Each 5-tuple in the list will contain five strings. The
# strings will represent, in order:
#
# - The location name of a team
# - The mascot of a team
# - The city in which the team plays
# - The state or province in which the team plays
# - The country in which the team plays
#
# write_nhl_teams should write the list of teams to the file given
# by the filename using the following format:
#
# [location] [mascot], [city], [state/province], [country]
#
# Note there is no comma between location and mascot, but
# there are commas between mascot and city, between city and state,
# and between state and country.
#
# So, for this list:
#
# [("New Jersey", "Devils", "Newark", "New Jersey", "USA"),
#  ("Winnipeg", "Jets", "Winnipeg", "Manitoba", "Canada")]
#
# The file printed would look like this:
#
# New Jersey Devils, Newark, New Jersey, USA
# Winnipeg Jets, Winnipeg, Manitoba, Canada
#
# We've included Sample.txt to show you what one of these
# files should look like.


# Write your function here!
def write_nhl_teams(filename, team_data):
    try:
        output_file = open(filename, "w")
        for team in team_data:
            print(
                f"{team[0]} {team[1]}, {team[2]}, {team[3]}, {team[4]}",
                file=output_file,
            )
        output_file.close()
    except Exception as e:
        print(e)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print nothing -- however, it should write the same contents
# as Sample.txt to Test.txt.
teams = [
    ("New Jersey", "Devils", "Newark", "New Jersey", "USA"),
    ("Winnipeg", "Jets", "Winnipeg", "Manitoba", "Canada"),
]
write_nhl_teams("Test.txt", teams)
