import random

class Shooter:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy
        self.alive = True
    
    def shoot(self, target):
        if random.random() < self.accuracy:
            target.alive = False
            print(f"{self.name} shoots and kills {target.name}!")
        else:
            print(f"{self.name} shoots and misses {target.name}.")

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
    

def simulate_shootout(print_out=False):
    ugly = Shooter("Ugly", 1/3)
    bad = Shooter("Bad", 2/3)
    good = Shooter("Good", 3/3)
    
    shooters = [ugly, bad, good]

    while sum([s.alive for s in shooters]) > 1:
        for shooter in shooters:
            if shooter.alive:
                targets = [s for s in shooters if s.alive and s != shooter]
                
                if targets:
                    target = max_min_accuracy
                    
                    # Shooter takes the shot
                    shooter.shoot(target)
        
        # Print alive shooters at the end of each round
        alive_shooters = [s.name for s in shooters if s.alive]
        print(f"Remaining alive: {', '.join(alive_shooters)}\n")
    
    # Determine the winner
    winner = [s.name for s in shooters if s.alive][0]
    print(f"{winner} is the winner!")


# Run the simulation
simulate_shootout()
