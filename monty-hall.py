import random

def main():
    num_iterations = 50000
    goat = "goat"
    prize = "car"
    num_doors = 4
    num_prizes = 2
    num_revealed = 1
    
    #validate data - this feels very clunk, even putting aside the un-written error msgs
    if num_prizes + num_revealed >= num_doors:
        raise ValueError("Too many prizes and revealed doors - the player should never be able to choose a door which has already been opened.")
    
    if num_doors < 0 or num_prizes < 0:
        raise ValueError("The number of doors and prizes must both be non-negative")
    
    if goat == prize:
        raise ValueError("Different symbols must be used for the preferred and not-preferred prizes")
        
    
    if num_iterations < 1:
        raise ValueError("Need at least one iteration")

    for switch in [True, False]:
        win_count = 0
        for iteration in range(num_iterations):        
            prob = construct_problem(num_doors, goat, prize, num_prizes)
            if play_problem(prob, switch, prize, num_revealed):
                win_count += 1

        report_results(win_count, num_iterations, switch)
        
    
def play_problem(problem: list, switch_choice: bool, prize: str, to_reveal=1):
    '''
    Given a set of parameters for interacting with a problem, plays it, and reports
    whether or not the problem was won.
    '''
    problem_indices = range(len(problem))
    first_choice = random.choice(problem_indices)
    revealed = set()


    valid_reveals = [i for i in problem_indices if i != first_choice and problem[i] != prize]
    revealed = set(random.sample(valid_reveals, to_reveal))

    

    second_choice = first_choice
    if switch_choice:
        second_choice = random.choice(
            [i for i in problem_indices if i != first_choice and i not in revealed]
        )

    return problem[second_choice] == prize


def construct_problem(num_doors=3, goat="G", prize="C", num_prizes=1) -> list:
    '''
    Constructs a scenario, consisting of a list, with each index of the list 
    representing a door. The value of each index will either be the "goat" param,
    (representing the prize which is presumed to be inferior), or the prize parameter.
    '''
    doors = [goat] * num_doors #fine because str are immutable
    prize_locs = random.sample(range(len(doors)), num_prizes)

    for loc in prize_locs:
        doors[loc] = prize

    return doors
    

def report_results(win_count: int, num_iterations: int, choice_switched: bool) -> None:
    win_percentage = 100*(win_count/num_iterations)
    print("================")
    print(f"Switch is: {choice_switched}.")
    #fstring breaks compatibility with python older than 3.6 (I think)
    print(f"won {win_count}/{num_iterations} games, or {win_percentage:.4f}%")
    print("================")
    

if __name__ == "__main__":
    main()
