def solution(moves):
    # store moves in direction dict
    direction = dict()
    # loop over string & collect moves
    for move in moves:
        if move not in direction:
            direction[move] = 1
            continue
        direction[move] += 1

    # check robot has moved all directions
    if len(direction.keys()) != 4:
        return False

    # check final position is (0,0)
    if direction["^"] != direction["v"] or direction[">"] != direction["<"]:
        return False

    # check it is not a square
    if direction["^"] == direction[">"]:
        return False

    return True
