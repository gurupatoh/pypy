import os        #used to run system commands that mainly clear the screen
import sys       #Used to terminate the script
import random    #used to generate random key lengths 
class players():

    
    first_menu = "Select which game you want to play:\n(A) Original Mastermind for 2 Players\n(B) Original Mastermind for 1 Player\n(C) Mastermind44 for 4 Players\n*Enter A, B, or C to continue*\n"
    second_menu = "What would you like to do?\n(p)lay the game\n(q)uit\n"
    welcome_message = "Welcome to Mastermind!\nDeveloped by *YOUR NAME SHOULD APPEAR HERE*\nCOMP 1046 Object-Oriented Programming"
    welcome_message_2 = "Welcome to Masermind44! The computer will create the secret code and reveal\nfour of the five positions one-by-one individually to each player. During\nrevealing each position only the requested player should look at the\nscreen. (R)ed, b(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack"


def clear_screen(self):
        """
        This function clears the screen by calling the os.clear for linux and Mac
        and os.cls for windows computers
        """
        try:
            os.system('clear') #for Mac and linux
        except:
            os.system('cls') #for windows computers
class feedback:
    def clear_screen(self):
        """
        This function clears the screen by calling the os.clear for linux and Mac
        and os.cls for windows computers
        """
        try:
            os.system('clear') #for Mac and linux
        except:
            os.system('cls') #for windows computers
    def validate_answer(self, key, answer):
                     
                    feedback = ''
                    for x in range(len(answer)):
                        if key.__contains__(answer[x]): #check if the answer contains any part of the key
                            if key[x] == answer[x]:
                                feedback += 'B' # Append a black pin to the feedback string
                            else:
                                feedback += 'W' #append a white pin toe the feedback string
                    if feedback == '':
                        feedback = "Nothing" # Return nothing if there was no matches
                    return feedback

        
class codeMaker(players):
        def play(self):
             # print(self.welcome_message) #dispay welcome message
             while True: #collect the game type information from the player
                 game = input(self.first_menu).lower()  #convert the input to lowercase
                 if ['a', 'b', 'c'].__contains__(game):
                    self.game = game
                    break
                    feedback.clear_screen(self)

    





class DecodingBoard(players):
      def start(self): #play the selected game
          codeMaker.play(self)
          while True:
                        option2 = input(self.second_menu) #request for input using the formated menu string
                        if option2 == 'q':
                            sys.exit('\nGoodbye! ') #terminates the running script and exits the game
                            break
                        elif option2 == 'p':
                            break
          feedback.clear_screen(self)

class codeBreaker(players):
    def breakcode(self):
        DecodingBoard.start(self)

        #the code below is executed for 2 players or single player mode
        if self.game == 'a' or self.game == 'b':
            if self.game == 'a':    #if the game is for 2 players

                #use list comprehension to get the player names
                players = [input(f"Player {x +1}: What is your name? ") for x in range(2)] #collect player names
                feedback.clear_screen(self)
                print(f"Welcome {players[1]}, you need to create a code that consists of four pegs. Eeach peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack. Specify the code by specifying four characters where each character indicates a colour as above. For example, WWRG represents the code White-White-Red-Green. You need to enter the code twice. No character is shown on the screen so {players[0]} cannot see it. Enter the code now: \n") #get the code from player 2



class keypeg(players):
    def codingpegs(self):
        codeBreaker.breakcode(self)
        code_correct = True
        if code_correct:
         key = input("Enter the code now: ").upper()
         confirm_key = input("Enter the same code again: ").upper()
         if key == confirm_key and len(key) == 4:
              for letter in key:
                  if ['R', 'L' ,'G', 'Y', 'W', 'B'].__contains__(letter) == False:
                      print("This attempt is incorrect. You must provide exactly four characters and they can only be, R, L, G, Y, W or B. ")
                      code_correct = False
                  if code_correct == True: # if the code provided by player is correct
                            feedback.clear_screen(self)
                            print("The code was stored")
                            break
                  else:
                       feedback.clear_screen(self)
                       print("This attempt is incorrect. You must provide exactly four characters and they can only be, R, L, G, Y, W or B. ")
class originalMasterMind(codeMaker):
    def originalGame(self):
        keypeg.codingpegs(self)
        if self.game == 'b':
                         key = ''.join(random.choices(['R', 'L', 'Y', 'W', 'B'], k=4)) #create a random key of length 4
                         attempts = 1 #holds the number of attempts

        if  True:
                    answer = input(f"Attempt #{attempts} \n").upper()
                    response= feedback.validate_answer(self,key,answer)
        if response == 'BBBB': #if response contains black pins only
                    print(f"Congratulations! You broke the code in {attempts} attempts.")
                    self.play() #display the game menu
        else:
                    if attempts == 6:
                        print(f"The code is {key}")
                    else:
                        attempts += 1
                        print(response)
class Mastermind(codeMaker):
    def masterMind44(self):
        codeMaker.play(self)
        #Masermind44 code begins here
        if self.game == 'c':
                key = ''.join(random.choices(['R', 'L', 'Y', 'W', 'B'], k=5)) #random key
                print(key)
                white_space = random.randint(0, 5) #pick a random point within the key that is going to be blank
                key = key[:white_space] + ' ' + key[white_space:] #add a space in a random position within the key
                players = [input(f"Player {x+1}: What is your name ? ") for x in range(4)]
                feedback.clear_screen(self)
                print(self.welcome_message_2)
                chosen_keys = [x for x in key if x.isalpha()] #display secret keys and their positions to the players
                for index in range(len(players)):
                    input(f"Player {players[index]}: When you are ready for one position of the code to be revealed on the screen press <enter>.")
                    print(f"Position: {key.index(chosen_keys[index])} Colour: {chosen_keys[index]}")
                    input("press <enter> to clear the screen")
                    feedback.clear_screen(self)
                attempts = 1 #holds the number of attempts
                game_on = True
                if game_on:
                  for player in players: #players take turns
                    answer = input(f"Each player can now start to guess the code. {player}, Attempt #{attempts}: Enter five colours using (R)ed, b(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack: " + '\n').upper()
                    result = feedback.validate_answer(self,key, answer)
                    print(result)
                    if result.count('B') >= 4: #if the response contains 4 black pins its a win!
                        print(f"Congratulations! You broke the code in {attempts} attempts.")
                        game_on = False
                        self.play() #display game menu
                        break
                    else:
                        print(f"Feedback on {player}, Attempt #{attempts}: {result}") #return feedback to the players
                if attempts == 5:
                    self.clear_screen()
                    print(f"The secret key is {key}")
                else:
                    attempts += 1

# x=codeBreaker()
# x.breakcode()

play=originalMasterMind()
play.originalGame()
# game = Mastermind()
# game.masterMind44()


    







