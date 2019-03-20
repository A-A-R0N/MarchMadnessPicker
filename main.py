>>> import random
>>> def odds(big, small):
...     roll = random.uniform(0,1)
...     impliedodds = big/(big + small)
...     if (roll > impliedodds):
...             print("Upset! Rolled %.2f vs %.2f" % (roll, impliedodds))
...     else:
...             print("Go with the favoriate. Rolled %.2f vs %.2f" % (roll, impliedodds))
