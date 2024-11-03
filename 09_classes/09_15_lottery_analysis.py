# 9-10. Lottery Analysis
# Make a loop to see how hard it might be to win the kind of lottery I just modeled.
import random

def generate_lottery_ticket():
    # Assuming a lottery ticket has 4 numbers from 1 to 49, adjust as needed
    return tuple(sorted(random.sample(range(1, 50), 4)))

def lottery_simulation(my_ticket):
    attempts = 0
    won = False
    while not won:
        attempts += 1
        new_ticket = generate_lottery_ticket()
        if new_ticket == my_ticket:
            won = True
            return attempts

# Make a list or tuple called my_ticket.
my_ticket = (3, 12, 18, 22)

# Run the lottery simulation
attempts_to_win = lottery_simulation(my_ticket)
print(f"I won the lottery!\nAttempts: {attempts_to_win}")
