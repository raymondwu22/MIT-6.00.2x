def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # any given item have 3 condition: bag1, bag2, not taken
    # so enumerate 3**N possible combinations
    for i in range(3**N):
        bag_1 = []
        bag_2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                bag_1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag_2.append(items[j])
        yield (bag_1, bag_2)

a = yieldAllCombos([1, 2, 3])
for n in a:
    print(n)