import random

UGLY = 1/3
BAD = 2/3
GOOD = 3/3

def simulate_once():
    alive_list = [UGLY, BAD, GOOD]
    while alive_list:
