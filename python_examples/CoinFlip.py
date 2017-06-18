#!/usr/bin/python3
from random import randrange as rand

outcome = "Heads" if(rand(0, 2) is 1) else "Tails"
print("It landed on: " + str(outcome))
