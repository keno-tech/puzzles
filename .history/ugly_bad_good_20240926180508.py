import random

class Shooter:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy
        self.alive = True
    
    def shoot(self, target):
        if random.random() < self.accuracy:
            target.alive = False
            # print(f"{self.name} shoots and kills {target.name}!")
        else:
            pass
            # print(f"{self.name} shoots and misses {target.name}.")

def max_min_accuracy(max_or_min, targets):
    max_accuracy = 0
    min_accuracy = 4
    best = None
    if max_or_min == "max":
        for x in targets:
            if x.accuracy > max_accuracy:
                best = x
                max_accuracy = x.accuracy

    elif max_or_min == "min":
        for x in targets:
            if x.accuracy < min_accuracy:
                best = x
                min_accuracy = x.accuracy
    
    return best
    

def simulate_shootout():
    ugly = Shooter("Ugly", 1/3)
    bad = Shooter("Bad", 2/3)
    good = Shooter("Good", 3/3)
    
    shooters = [ugly, bad, good]
    round = 1
    while sum([s.alive for s in shooters]) > 1:
        for shooter in shooters:
            if shooter.alive:
                targets = [s for s in shooters if s.alive and s != shooter]
                
                if round == 1 and shooter.name == "Ugly":
                    continue
                
                if targets:
                    # choose strategy 
                    target = max_min_accuracy("max", targets)
                    shooter.shoot(target)

        # alive_shooters = [s.name for s in shooters if s.alive]
        # print(f"Remaining alive: {', '.join(alive_shooters)}\n")
        round += 1

    winner = [s.name for s in shooters if s.alive][0]
    # print(f"{winner} is the winner!")
    return winner

N = 10000
def simulate_with_stats():
    wins = {"Ugly": 0, "Bad": 0, "Good": 0}

    for i in range(N):
        winner = simulate_shootout()
        wins[winner] += 1

    return wins

for k,v in simulate_with_stats().items():
    print(f'{k} won {100*(v/N)}% of times')
        
