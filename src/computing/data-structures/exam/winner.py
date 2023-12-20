# In the racing video game Mario Kart, up to 12 players
# can race against each other. At the end of each race,
# players receive points based on where they finished in
# the race. At the end of some number of races, the player
# with the most points wins.
#
# In this problem, let's assume only 4 players are playing,
# and that they are going to complete 4 races. In each race,
# whoever finishes first gets 5 points; second place gets
# 3 points; third place gets 2 points; and fourth place gets
# 1 point.
#
# Write a function called find_winner. find_winner will
# take as input a list of four 4-tuples. Each 4-tuple
# represents the finishing order for a particular race.
# Player 1's finishing place is in index 0; Player 2 in
# index 1; Player 3 in index 2; and Player 4 in index 3.
#
# For example: (3, 4, 2, 1) would indicate that Player 1
# came in 3rd, Player 2 came in 4th, Player 3 came in 2nd,
# and Player 4 came in 1st.
#
# find_winner should return the winner of the four-race
# series with the string "Player X wins!", where X is
# replaced by the winning player's number. If two or more
# players tie for first, find_winner should just return
# the string "It's a tie!"
#
# For example:
#
# race_list = [(4, 3, 2, 1), (3, 2, 4, 1),
#              (4, 1, 3, 2), (2, 4, 3, 1)]
# find_winner(race_list) -> "Player 4 wins!"
#
# In the example above, Player 4 would have 18 points:
# 5 points for each first-place finish, 3 points for
# the second-place finish. Player 3 would have 8 points;
# Player 2 would have 11 points; and Player 1 would have
# 7 points. Therefore, Player 4 would win.


# Write your function here!
def find_winner(race_data):
    player_data = {1: 0, 2: 0, 3: 0, 4: 0}
    for round_data in race_data:
        for i in range(len(round_data)):
            if round_data[i] == 1:
                player_data[i + 1] += 5
            else:
                player_data[i + 1] += 5 - round_data[i]
    winner = None
    max_points = 0

    for player, player_points in player_data.items():
        if player_points > max_points:
            winner = player
            max_points = player_points
        elif player_points == max_points:
            winner = False

    if not winner:
        return "It's a tie!"
    return f"Player {winner} wins!"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# Player 4 wins!
# It's a tie!
# Player 1 wins!
race_list_1 = [(4, 3, 2, 1), (3, 2, 4, 1), (4, 1, 3, 2), (2, 4, 1, 1)]
print(find_winner(race_list_1))

race_list_2 = [(3, 4, 2, 1), (1, 4, 2, 3), (4, 2, 3, 1), (2, 3, 1, 4)]
print(find_winner(race_list_2))

race_list_3 = [(3, 1, 2, 4), (1, 3, 4, 2), (1, 3, 2, 4), (1, 3, 4, 2)]
print(find_winner(race_list_3))
