import random
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result = ''
    for i in range(n):
        result += str(rollDie())
    print(result)


# runSim('11111', 1000)

def fracBoxCars(numTests):
    numBoxCars = 0.0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars / numTests


print('Frequency of double 6 =',
      str(fracBoxCars(100000) * 100) + '%')