import random


def main():
    the_file = open('capitals.csv', 'r')
    states  = dict()
    for line  in the_file:
        state = line.rstrip("\n").split(',')
        states[state[0]] = state[1]

    the_file.close()

    count_right_answer = 0
    count_wrong_answer = 0

    states_key = list(states.keys())

    for i in range(1000):
        radndom_choice = random.choice(states_key)
        print('Enter the capital of', radndom_choice)
        user_input = input()
        decision_maker = user_input.lower()
        if decision_maker  == 'quit' :
            return print('Thank you for taking CSIS-151 class.')
        elif radndom_choice and states[radndom_choice] == user_input:
            count_right_answer+=1
        else:
            print('Wrong!!! The capital of', radndom_choice, ' is ', states[radndom_choice])
            count_wrong_answer += 1

main()

    #   compare and respond to the user
#   if the user enters "quit', the exit the prohram


