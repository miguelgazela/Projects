# Change Return Program
# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters,
# dimes, nickels, pennies needed for the change.

coins = (0.25, 0.10, 0.05, 0.01)


def select_change(change):
    res = []
    for v in coins:
        res.append(int(round(change, 2) / v))
        change -= v * res[-1]
    return res


if __name__ == "__main__":
    try:
        cost = float(raw_input("Cost: "))
        amount = float(raw_input("Amount given: "))

        if amount < cost:
            print "Not enough money."
        elif amount == cost:
            print "Exact money, no change required."
        else:
            res = select_change(amount-cost)
            print "The change consists of %d quarters, %d dimes, %d nickels and %d pennies" % (res[0], res[1], res[2], res[3])


    except:
        print "Invalid input"
