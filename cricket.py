import random

def cricket_game():
    # initialize the score and number of wickets
    score = 0
    wickets = 0

    # define the maximum runs that a player can score in a single ball
    max_runs = 6

    # define the total number of overs in the game
    total_overs = 2

    # define the number of balls in an over
    balls_per_over = 6

    # define the total number of balls in the game
    total_balls = total_overs * balls_per_over

    # define a list of possible runs that a player can score
    runs = [0, 1, 2, 3, 4, 5, 6, 'W']

    # loop through each ball in the game
    for ball in range(1, total_balls+1):
        # generate a random score for the ball
        ball_score = random.choice(runs)

        # update the score and wickets based on the ball score
        if ball_score == 'W':
            wickets += 1
            print(f'Ball {ball}: OUT!')
        else:
            score += ball_score
            print(f'Ball {ball}: {ball_score}')

        # check if the game is over
        if wickets == 10 or ball == total_balls:
            break

        # print the current score and wickets after each ball
        print(f'Current score: {score}/{wickets}')

    # print the final score and number of wickets
    print(f'Total score: {score}/{wickets}')

    # check if the game was won or lost
    if score > 0:
        print('You won the game!')
    else:
        print('You lost the game!')

# run the cricket game
cricket_game()
