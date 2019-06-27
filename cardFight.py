# Card Fight
# Code by cFreeze9

import random
import time

# These are the list of cards used for battling. Anything with a + in front of the number is used for healing.
CARDS = '0 1 2 3 3 4 4 5 5 5 6 6 6 8 8 8 8 10 10 10 10 12 12 12 12 12 15 15 15 15 15 20 20 20 20 20 20 25 25 25 25 25 25 30 30 30 30 30 30 30 40 40 40 40 40 40 40 50 50 50 50 50 50 60 60 60 60 60 60 70 70 70 70 70 75 75 75 75 75 80 80 80 90 90 90 100 100 125 125 150 200 0 0 0 0 0 0 0 0 0 0 +12 +12 +12 +12 +12 +25 +25 +25 +25 +25 +25 +75 +75 +75 +75 +75 +125 +125 +250'.split()

# These functions append to the CARDS list. Anything with an R in front of the number is used for mystery cards.
for i in range(120, 160):
    CARDS.append('R1')
for i in range(160, 180):
    CARDS.append('R2')
for i in range(180, 190):
    CARDS.append('R3')
for i in range(190, 197):
    CARDS.append('R4')
for i in range(197, 200):
    CARDS.append('R5')
CARDS.append('250')

# The fighter class holds the players' name, HP, and attributes.
class Fighter():
    def __init__(self, name, HP):
        # Fighter constructor
        self.name = name
        self.HP = HP

    def displayStats(self):
        # This funtion displays player's name and HP
        print(self.name + ': ' + str(self.HP) + '/250')

    def attack(self, number, mod, mystery):
        # This function modifies the player's HP and displays messages.

        if mod == 'miss':
            print('The card crumbles to millions of pieces and did no damage.')

            if mystery:
                time.sleep(1)
                print('It would have hit for ' + str(number) + ' damage.')
                
            return

        crit = 0 # crit must be initialized here. Otherwise, there will be errors.
        if mod == 'crit':
            crit = number * 0.5
            if crit % 1 == 0.5:
                crit += 0.5 # crit rounds up to ensure whole numbers are being used.
                
            print('A critical hit!')
            time.sleep(1)
            
        if number == 0:
            print('The card didn\'t do anyting. Lame.')
            return

        elif number == 250 and not mystery: # Only works if the 250 doesn't come from a mystery card.
            print('The card NUKES ' + self.name + ' for infinite damage!!!')
            
        else:
            print('The card hits ' + self.name + ' for ' + str(int(number + crit)) + ' damage!')

        # The player's HP is modified here.    
        if number + crit >= self.HP or number == 250 and not mystery:
            self.HP = 0
        else: # int ensures that the values come out cleanly without decimal places.
            self.HP = int(self.HP - number - crit)

    def heal(self, number):
        # This function modifies the player's HP and displays messages.
        if number + self.HP > 250: # Used to set an HP cap by adjusting the number.
            number = 250 - self.HP

        # The player's HP is modified here.
        self.HP += number

        #Displays messages
        print(self.name + ' restored its health by ' + str(number) + ' HP.')
        if number == 0:
            time.sleep(1)
            print(self.name + ' wasted a turn.')

    def godHeal(self, number):
        # Used only if the player's name is God.
        self.HP += number
        print(self.name + ' restored his health by ' + str(number) + ' HP.')

def machineDescription(number):
    # Possible descriptions for all the Anonymous accounts are shown here.
    descriptions = ["He likes to troll people for his own enjoyment.",
                    "He is a big fan of M-Rated video games.",
                    "He wastes so much money gambling.",
                    "He mainly listens to gangsta rap.",
                    "He loves getting into unhealthy arguments on the internet.",
                    "He visits the dark web regularly.",
                    "He was arrested one time for intentionally doing a bad thing.",
                    "He is an atheist who hates religious people.",
                    "He would punch a guy who's into anime.",
                    "She's a maneater!",
                    "He seems evil.",
                    "He is a proponent of hate.",
                    "He loves watching R-Rated movies.",
                    "He is a Neo-Nazi.",
                    "He taunts you with a lot of 4-letter profanities.",
                    "She's a maniac, maniac.",
                    "He listens to a lot of black metal.",
                    "He is a big-time pervert.",
                    "He gave Mars of Destruction a 10 on MyAnimeList.",
                    "He is a porn addict.",
                    "He smokes funny things everyday.",
                    "He is a rapist.",
                    "He cheated on his wife.",
                    "He once stole a gaming console.",
                    "He has hacked numerous online accounts."]
    # The description is based on the remainder of the number of the opponent.
    index = number % len(descriptions)
    # Some numbers display special descriptions.
    if number == 1738:
        return("He is a big fan of Fetty Wap.")
    if number % 1000 == 621:
        return("He is a furry.")
    if number == 1337:
        return("He is fluent in Leetspeak.")
    else:
        return descriptions[index]

def coinFlip():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return True
    else:
        return False 

def getCard(selection):
    # Obtains a random card from the card selection.
    cardIndex = random.randint(0, len(selection) - 1)
    return selection[cardIndex]

def processValue(rCard):
    # Used to generate the value of the mystery card.
    possibleValues = []
    for i in range (0, 10):
        possibleValues.append(random.randint(0, 250))
    possibleValues.sort()
    # The value depends on what string is passed. The higher the value, the stronger the card potentially is.
    if rCard == 'R1':
        return possibleValues[0]
    elif rCard == 'R2':
        return possibleValues[1]
    elif rCard == 'R3':
        return possibleValues[2]
    elif rCard == 'R4':
        return possibleValues[3]
    elif rCard == 'R5':
        return possibleValues[4]                          
    return None

def chance():
    # Used to return 'miss' or 'crit', which each have a 5% chance of occurring.
    luck = random.randint(0, 19)
    if luck == 0:
        return 'miss'
    elif luck == 19:
        return 'crit'
    return

def victoryMessage(name, othername):
    # Displays a random message when the player defeats the computer.
    messages = [name + ' has won the game!',
                name + ' stands victorious!',
                name + ' does a victory dance!',
                name + ' looks at ' + othername + '\'s lying body with a sense of satisfaction.',
                name + ' pwned ' + othername + '!',
                name + ' rekt ' + othername + '!',
                'Congratulations, ' + name + '!',
                name + ' pulled off an impressive victory!',
                'Epic win for ' + name + '!',
                name + ' is the winner!',
                'Justice is served to ' + othername + '!',
                othername + ' is sent to the purgatory.',
                othername + ' descends to hell.',
                name + ' laughs at the defeat of ' + othername + '!',
                name + ' sings a victory song!']
    message = random.randint(0, len(messages) - 1)
    if name == 'Teardrop':
        message = random.randint(0, len(messages) - 3)
    return messages[message]

def quitMessage(name):
    # Displays a random message when the player quits.
    messages = [name + ' ragequits.',
                name + ' gave up.',
                name + ' got away safely.',
                name + ' is not gonna take it anymore.',
                name + ' can\'t handle the pressure.',
                name + ' didn\'t win, because winners never quit.',
                name + ' was too afraid to continue.',
                name + ' left the battlefield.',
                name + ' has decided to quit.',
                name + ' is too tired to fight.',
                name + ' is sick and tired of getting hit by cards.',
                name + ' just won\'t keep fighting.',
                name + ' lost the opportunity to win.',
                name + ' made a good decision by not risking death.',
                name + ' ran away.']
    message = random.randint(0, len(messages) - 1)
    return messages[message]

def deathMessage(name, othername):
    # Displays a random message when the player loses.
    messages = [name + ' died.',
                othername + ' killed ' + name + '!',
                'Press F to pay respects to ' + name + '.',
                name + ' lies down breathlessly.',
                name + '\'s body begins to decompose after a while.',
                name + ' gave up the ghost.',
                name + ' went to the afterlife.',
                name + ' was rushed to the hospital.',
                name + ' passed away.',
                name + ' bit the dust.',
                name + ' ascended to heaven.',
                name + ' vaporized.',
                name + ' fainted.',
                othername + ' will not be attending ' + name + '\'s funeral.',
                name + ' flatlined.']
    message = random.randint(0, len(messages) - 1)
    return messages[message]

print('Welcome to Card Fight!')
firstTime = True
changeName = False

while True:
    if not firstTime:
        print('Would you like to change your character\'s name? (Yes/No)')
        change = input()
        if change.lower() == 'yes':
            changeName = True
        elif change.lower() == 'no':
            changeName = False
        hero.HP = 250
    if firstTime or changeName:
        print('What is the name of your fighter?')
        hero = Fighter(input(), 250)
    print(hero.name + ', prepare to meet your opponent.')
    time.sleep(2)

    # Generates a random name for the computer to have.
    computerName = random.randint(0, 9999)
    if computerName < 10:
        computerName = '000' + str(computerName)
    elif computerName < 100:
        computerName = '00' + str(computerName)
    elif computerName < 1000:
        computerName = '0' + str(computerName)
    machine = Fighter('Anonymous' + str(computerName), 250)
    print('Your opponent is ' + machine.name + '.')
    time.sleep(1)
    print(machineDescription(int(computerName)))
    time.sleep(1)
    print('Press enter to continue.')
    input()

    if firstTime == True:
        print('Would you like a tutorial? (Yes/No)')
        if input().lower().startswith('y'):
            print('You both start out with 250HP. (Press enter to continue.)')
            input()
            print('You will attack using some specialized cards that deal damage to your opponent.')
            input()
            print('Sometimes, a 0 card may appear, which does nothing.')
            input()
            print('Sometimes, a healing card may appear, which heals yourself.')
            input()
            print('Sometimes, a mystery card may appear, which deals a random amount of damage.')
            input()
            print('The higher the class of the mystery card, the more likely the card will deal more damage.')
            input()
            print('Rarely, a critical hit may land, dealing more damage.')
            input()
            print('Rarely, the card may crumble, which won\'t cause any damage.')
            input()
            print('You may quit the battle anytime by typing "quit".')
            input()
            print('If you lose all your HP, you lose the battle, and the opponent wins.')
            input()
            print('This concludes this tutorial. Please press enter.')
            input()
    time.sleep(2)

    firstTime = False
    
    if hero.name == 'Chuck Norris' or hero.name == 'God':
        hero.HP = 9999
        
    turnCounter = 0
    if(coinFlip()):
        print(hero.name + ' goes first.')
        herosTurn = True
    else:
        print(machine.name + ' goes first.')
        herosTurn = False

    gameIsPlaying = True
    time.sleep(1)
    print('\nTURNS: ' + str(turnCounter))
    hero.displayStats()
    machine.displayStats()

    while gameIsPlaying:

        if herosTurn:
            print('\nWhat will ' + hero.name + ' do? \nOptions: Fight | Quit')
            if (turnCounter == 2 or turnCounter == 3):
                print('Hint: You could just hit Enter to fight.')

            if not input().lower() == 'quit':
                turnCounter += 1
                print('TURNS: ' + str(turnCounter))
                card = getCard(CARDS)
                if hero.name == "Chuck Norris":
                    card = '250'

                if card.startswith('+'):
                    print(hero.name + ' pulls out a heal card that says ' + card + '.')
                    value = card[1:]
                    time.sleep(2)
                    if hero.name == 'God':
                        hero.godHeal(int(value))
                    else:
                        hero.heal(int(value))

                else:
                    mod = chance()
                    mystery = False

                    if card.startswith('R'):
                        print(hero.name + ' pulls out a Class ' + card[1:] + ' mystery card.')
                        mystery = True

                        damage = processValue(card)
                        time.sleep(2)
                        machine.attack(damage, mod, mystery)

                    else:
                        if card == '250':
                            print(hero.name + ' pulls out an INFINITY card!!!')
                        elif card.startswith('8'):
                            print(hero.name + ' pulls out an ' + card + ' card.')
                        else:
                            print(hero.name + ' pulls out a ' + card + ' card.')

                        damage = int(card)
                        time.sleep(2)
                        machine.attack(damage, mod, mystery)

                    if machine.HP == 0:
                        gameIsPlaying = False

                herosTurn = False

            else:
                print(quitMessage(hero.name))
                if turnCounter < 2:
                    print('Why give up so soon?')
                elif hero.HP == 250:
                    print('Oh, and ' + hero.name + ' came out completely unscathed.')         
                gameIsPlaying = False
                break

        else:
            print('\nIt\'s ' + machine.name + '\'s turn. Press enter to continue.')
            input()

            turnCounter += 1
            print('TURNS: ' + str(turnCounter))
            card = getCard(CARDS)

            if card.startswith('+'):
                print(machine.name + ' pulls out a heal card that says ' + card + '.')
                value = card[1:]
                time.sleep(2)
                machine.heal(int(value))

            else:
                mod = chance()
                mystery = False

                if card.startswith('R'):
                    print(machine.name + ' pulls out a Class ' + card[1:]  +' mystery card.')
                    mystery = True

                    damage = processValue(card)
                    time.sleep(2)
                    hero.attack(damage, mod, mystery)

                else:
                    if card == '250':
                        print(machine.name + ' pulls out an INFINITY card!!!')
                    elif card.startswith('8'):
                        print(machine.name + ' pulls out an ' + card + ' card.')
                    else:
                        print(machine.name + ' pulls out a ' + card + ' card.')

                    damage = int(card)
                    time.sleep(2)
                    if hero.name == 'God' and card == '250':
                        print('God is immune to INFINITY cards.')
                    else:
                        hero.attack(damage, mod, mystery)

                if hero.HP == 0:
                    gameIsPlaying = False

            herosTurn = True

        
        time.sleep(2)
        print()
        hero.displayStats()
        machine.displayStats()

        if turnCounter == 50 and gameIsPlaying:
            gameIsPlaying = False
            print('\n50 turns is too long for this battle, so it ends right now.')

    if hero.HP == 0:
        print(deathMessage(hero.name, machine.name))
    elif machine.HP == 0:
        print(victoryMessage(hero.name, machine.name))
    time.sleep(2)

    print('Would you like to play again? (Yes/No)')
    if input().lower().startswith('n'):
        break
