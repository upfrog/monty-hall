import random
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='MontyHallSimulator',
        description='Simulates the Monty Hall problem with user-selected parameters')

    parser.add_argument('--num-doors', type=int, default=3)
    parser.add_argument('--num-revealed', type=int, default=1)
    parser.add_argument('--num-iterations', type=int, default=1000)
    parser.add_argument('--num-prizes', type=int, default=1)
    parser.add_argument('--prize-token', type=str, default="C")
    parser.add_argument('--goat-token', type=str, default="G")
    parser.add_argument('--seed', type=int, help="Seed for RNG (optional, provides reporducibility)")
    parser.add_argument('--strategy', choices=["both", "switch", "stick"], default="both")

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    validate_args(args)
    run_simulation(args)    


def run_simulation(args):
    strategy = [True, False] if args.strategy == "both" else [args.strategy=="switch"]
    for switch in strategy:
        win_count = 0
        for iteration in range(args.num_iterations):        
            prob = construct_problem(args.num_doors, args.goat_token, 
                                     args.prize_token, args.num_prizes)
            if play_problem(prob, switch, args.prize_token, args.num_revealed):
                win_count += 1

        report_results(win_count, args.num_iterations, switch)


def validate_args(args):
    if args.num_prizes + args.num_revealed >= args.num_doors:
        raise ValueError("Too many prizes and revealed doors - the player should never be able to choose a door which has already been opened.")
    
    if args.num_doors < 0 or args.num_prizes < 0:
        raise ValueError("The number of doors and prizes must both be non-negative")
    
    if args.goat_token == args.prize_token:
        raise ValueError("Different symbols must be used for the preferred and not-preferred prizes")
        
    if args.num_iterations < 1:
        raise ValueError("Need at least one iteration")

    
def play_problem(problem: list, switch_choice: bool, prize: str, to_reveal=1):
    '''
    Given a set of parameters for interacting with a problem, plays it, and reports
    whether or not the problem was won.
    '''
    problem_indices = range(len(problem))
    first_choice = random.choice(problem_indices)
    revealed = set()

    #valid_reveals = [i for i in problem_indices if i != first_choice and problem[i] != prize]
    #valid_reveals = gen_valid_reveals(problem_indices, first_choice, problem, prize)
    #revealed = set(random.sample(valid_reveals, to_reveal))
    revealed = gen_reveals(problem_indices, first_choice, problem, prize, to_reveal)

    second_choice = first_choice
    if switch_choice:
        '''second_choice = random.choice(
            [i for i in problem_indices if i != first_choice and i not in revealed]
        )'''
        second_choice = gen_second_choice_options(problem_indices, first_choice, revealed)

    return problem[second_choice] == prize

#For benchmarking:
def gen_valid_reveals(problem_indices, first_choice, problem, prize):
    return [i for i in problem_indices if i != first_choice and problem[i] != prize]

def gen_reveals(problem_indices, first_choice, problem, prize, to_reveal):

    valid_reveals = gen_valid_reveals(problem_indices, first_choice, problem, prize)

    num_valid_reveals = len(valid_reveals)
    if to_reveal > num_valid_reveals//2:
        #generate the elements we DONT reveal
        
        exclude_n = len(valid_reveals) - to_reveal
        excluded = set(random.sample(valid_reveals, exclude_n))
        valid_reveals = set(valid_reveals)
        return valid_reveals - excluded
    else:
        #valid_reveals = gen_valid_reveals(problem_indices, first_choice, problem, prize)
        return set(random.sample(valid_reveals, to_reveal))

def gen_second_choice_options(problem_indices, first_choice, revealed):
    return random.choice(
            [i for i in problem_indices if i != first_choice and i not in revealed]
        )


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
    

def report_results(win_count: int, num_iterations: int, switch:bool) -> None:
    win_percentage = 100*(win_count/num_iterations)
    strategy = "switch" if switch else "stick"
    print("====================")
    print(f"Strategy is: {strategy}.")
    #fstring breaks compatibility with python older than 3.6 (I think)
    print(f"won {win_count}/{num_iterations} games, or {win_percentage:.4f}%")
    print("====================")
    

if __name__ == "__main__":
    main()
