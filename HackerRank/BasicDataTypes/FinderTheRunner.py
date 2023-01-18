from math import inf


def solve(scores):
    winner = -inf
    runner_up = -inf
    for i in scores:
        if i > winner:
            winner, runner_up = i, winner
        elif winner > i > runner_up:
            runner_up = i
    return runner_up


scores = [5, 8, 2, 6, 8, 5, 8, 7]
print("Runner-up score is:", solve(scores))

# Create a Score List
score_lis = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 9, 10, 10, 10, 10]

# Print the List
print('Current Scores: ', score_lis)

# Get Max Number from the list
max_num = max(score_lis)

# Count the Max Number
max_num_count = score_lis.count(max_num)

# Apply for loo p and remove Max Number from the list
for i in range(0, max_num_count):
    score_lis.remove(max_num)

# Now Max Number becomes the Runner-Up Score
runner_up = max(score_lis)

# Print it
print('Runner Up Score is: ', runner_up)
