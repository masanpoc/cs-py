# Let's try out a sort of data analysis-style problem. In
# this problem, you're going to have access to a data set
# covering Georgia Tech's all-time football history. The data
# will be a CSV file, meaning that each line will be a comma-
# separated list of values. Each line will describe one game.
# The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
# If Points For is greater than Points Against, then Georgia
# Tech won the game. If Points For is less than Points Against,
# then Georgia Tech lost the game. If the two are equal, then
# the game was a tie.
#
# You can see a subsection of this dataset in season2016.csv
# in the top left, but the actual dataset you'll be accessing
# here will have 1237 games.
#
# Write a function called all_time_record. all_time_record
# should take as input a string representing an opposing team
# name. It should return a string representing the all-time
# record between Georgia Tech and that opponent, in the form
# Wins-Losses-Ties. For example, Georgia Tech has beaten
# Clemson 51 times, lost 28 times, and tied 2 times. So,
# all_time_record("Clemson") would return the string "51-28-2".
#
# We have gone ahead and started the function and opened the
# file for you. The first line of the file are headers:
# Date,Opponent,Location,Points For,Points Against. After that,
# every line is a game.

import traceback


def all_time_record():
    try:
        record_file = open("season2016.csv", "r")

        total_gained = 0
        total_lost = 0
        num_ties = 0
        record_file.readline()

        # total points for all teams
        total = {}

        # max diff
        max_diff = 0
        max_diff_team = None

        for game in record_file:
            game = game.strip()
            game = game.split(",")

            team_name = game[1]
            location = game[2]
            gained_points = game[3]
            lost_points = game[4]
            game_date = game[0]
            game_date = game_date.split("-")
            year = game_date[0]
            month = game_date[1]

            # if team_name == opponent:
            #     if int(gained_points) == int(lost_points):
            #         num_ties += 1
            #     elif int(gained_points) > int(lost_points):
            #         total_gained += 1
            #     elif int(gained_points) < int(lost_points):
            #         total_lost += 1

            # most points against
            # if int(gained_points) > int(lost_points):
            #     if team_name not in total:
            #         total[team_name] = 0
            #     total[team_name] += int(gained_points)
            # elif int(gained_points) == 0:
            #     if team_name not in total:
            #         total[team_name] = 0

            # no scores from opponent
            # if int(lost_points) == 0:
            #     if team_name not in total:
            #         total[team_name] = 0

            # highest diff
            # if int(gained_points) - int(lost_points) > max_diff:
            #     max_diff_team = team_name
            #     max_diff = int(gained_points) - int(lost_points)

            # counter times played against team and store the sum of diffs
            if team_name not in total:
                total[team_name] = {"count": 0, "diff_sum": 0}

            total[team_name]["count"] += 1
            total[team_name]["diff_sum"] += int(gained_points) - int(lost_points)

        # count>5 - highest diff avg
        max_diff_team5 = None
        max_diff_avg = 0

        for team, val in total.items():
            if val["count"] > 5:
                currentAvg = val["diff_sum"] / val["count"]
                if currentAvg > max_diff_avg:
                    max_diff_avg = currentAvg
                    max_diff_team5 = team

        print(max_diff_team5, "maximum avg diff team", max_diff_avg)

        # highest diff
        print(max_diff_team, max_diff)

        # max_scored = 0
        lost_team = ""
        for team, val in total.items():
            # if val > max_scored:
            #     max_scored = val
            #     lost_team = team
            # no gained
            if val == 0:
                print(team)

        print(lost_team)
        record_file.close()

        return f"{total_gained}-{total_lost}-{num_ties}"

    except Exception as error:
        print(traceback.format_exc())


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
# line.
print(all_time_record())
print(all_time_record())
print(all_time_record())
