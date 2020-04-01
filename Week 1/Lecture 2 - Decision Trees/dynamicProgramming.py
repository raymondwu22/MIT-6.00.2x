from Food import *

def fastMaxVal(toConsider, avail, memo = {}):
    """ Assumes toConsider a list of items,
                avail a weight, memo supplied by recursive calls
        Returns a tuple of the total value of a solution
        to 0/1 knapsack problem and
        the items of that solution
    """
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = fastMaxVal(toConsider[1:],
                                     avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)

        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

import random
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    foods = buildLargeMenu(numItems, 90, 250)
    testMaxVal(foods, 750, fastMaxVal, False)