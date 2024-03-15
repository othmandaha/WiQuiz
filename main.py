from art import logo
from Database import History, Languages, Physics, Politics,\
Technology, Psychology
import random
from os import system
import time


subjects = {1 :History, 2: Languages, 3: Physics, 4: Politics, 5: Psychology, 6: Technology}
def subject_manager():
    """
    Prompts the user to choose from
    the different subjuects and returns the chosen one as a module.
    """
    print("\nPick a subject!\n")
    the_choice= int(input("""
          1 - History\n
          2 - Languages\n
          3 - Physics\n
          4 - Politics\n
          5 - Psychology\n
          6 - Technology\n 
          \tType the corresponding number to chose your subject: """))
    if the_choice in subjects.keys():
        return subjects[the_choice]
    else: 
        print("\nYou've typed somthing wrong!!")
        #* we use recursion to repeat unitl we get a valid answer
        subject_manager()

    
       
def mode_picker():
    """Prmpts the user for the mode.
    Returns:
        int: 1 for simplified.
        int: 2 for classic.
    """
    print("\nChose your Mode from the ones Below\n")
    chosen_mode = input("1 - Simplified\t\t2 - Classic\n\n\ttype [1] or [2]: ")
    if chosen_mode == '1' or chosen_mode == '2':
        return chosen_mode
    else:
        print("\nYou've typed somthing wrong!!")
        #* we use recurssion to repeat until we get 1 or 2
        mode_picker()


def answer_checker(lie, chosen_option):
    """Checks the answer.
    
    Args:
        lie (int): the number of the lie option 1 or 2
        chosen_option (int): the option the user chose
    Returns:
        (int): 1 if the he succeded in detecting the lie
        (int): 0 otherwise
    """
    if chosen_option == lie:
        return 1
    else:
        return 0

     
def gameplay(subject, chosen_mode):
    """
    Executes the gameplay loop for the trivia game.

    Args:
        subject (Subject): The subject containing questions and answers.
        chosen_mode (int): The chosen gameplay mode: 1 for simplified, 2 for classic.

    Returns:
        None

    We clear the screen using system('cls') - works only on windows - Then we print the logo each time 
    the loop iterates. We make a set of random options depending on the mode they might be 3 or 2. One of 
    This options is a lie.
    We save the lie in order to find it's index after we shuffle the options list.
    We compare the lie index to the user's option to calculate the socore, if he's write we add 10 the the score,
    we subtract a heart otherwise.
    The loop won't stop until the user want to return home by typing 'h' or until the user loses all hearts.
    """
    game_over = False
    hearts = 3
    score = 0
    while game_over != True and hearts != 0:
        system('cls')
        print(logo)
        print("\n{} ❤️\t\t Score: {}".format(hearts, score))

        #* this list is made in order to be randomize
        #* for the places of the correct/incorrect answer not to be always the same (1 or 2)

        #simplified
        options = [random.choice(subject.correct),\
                    random.choice(subject.incorrect)]
        #* we save the option that is a lie since the option will be shuffled
        lie = options[1]

        # If Classic mode
        if chosen_mode != 1:
            #* insert at the begening to be able to keep track of the lie
            options.insert(0, random.choice(subject.correct))
            lie = options[2]

        #* We print the number of the option and the random option itself afterward
        random.shuffle(options)
        print("\nOut of these options below choose 'THE LIE'\n")
        for i, option in enumerate(options, start= 1):
            #* We print the number of the option and the random option itself afterward
            print("{}- ".format(i), end='')
            print(option)
            #* detect the index of the lie since it's shuffled
            if lie == option:
                lie_index = i

        #* the hint is for testing purposes 
        print("HINT: lie is {}".format(lie_index)) 

        if chosen_mode == 1:
            #simplified mode prompt
            choice = int(input("\n\tType [1] or [2]: "))
        else:
            #classic mode prompt
            choice = int(input("\n\tType [1], [2] or [3]: "))

        #* We compare the lie index to the choice of the user
        if answer_checker(lie_index, choice) == 1:
            print("\nBravo!! You detected The Lie!!")
            score += 10
        else:
            hearts -= 1
            if hearts == 0:
                print("You've lost!!\nYour score in the subject is {}\n".format(score))
                #* sleep to let the user see the score because the terminal will be cleared
                time.sleep(6)
                return
            else:
                print("\nYou've lost a heart!!")

        answer = input("\tType [n] to continue, Type [h] to return home: ").lower()
        if answer == 'h':
            print("\nYour score in the subject is {}".format(score))
            time.sleep(5)  
            game_over = True
         
        
def start():
    """
    The starting point of the program.
    It connects all functions.
    """
    session_over = False
    while session_over != True:
        system('cls')
        print(logo)
        answer = input("\n\tType [S] to start the game type anything else to exit: ").lower()
        if answer == 's':
            session_over = False
        else:
            session_over = True
            break
        chosen_subject = subject_manager()
        chosen_mode = mode_picker()
        gameplay(chosen_subject, chosen_mode)



if __name__  == "__main__":
    start()