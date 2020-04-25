import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    same_color_count = 0
    for trial in range(numTrials):
        balls = [0,0,0,1,1,1]
        random.shuffle(balls)
        sum_balls = sum(balls[:3])
        if sum_balls == 0 or sum_balls == 3:
            same_color_count += 1
    return float(same_color_count)/numTrials