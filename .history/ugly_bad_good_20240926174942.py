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

def simulate_shootout():
    ugly = Shooter("Ugly", 1/3)
    bad = Shooter("Bad", 2/3)
    good = Shooter("Good", 3/3)
    
    shooters = [ugly, bad, good]

    while sum([s.alive for s in shooters]) > 1:
        for shooter in shooters:
            if shooter.alive:
                targets = [s for s in shooters if s.alive and s != shooter]
                
                if targets:
                    # Pick a target randomly
                    target = random.choice(targets)
                    
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
