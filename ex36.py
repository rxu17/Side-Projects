# Rixing's Game: From Jedi Padawan to Jedi Knight???
from sys import exit 
import random 
from random import randint

storm = False
vader = False
win = False
HP, ATK, DEF = 0, 0, 0
#s_HP, s_ATK, s_DEF = 0, 0, 0
#p_stat = [randint(self, 1, 100), randint(self, 1, 100), randint(self, 1, 100)]
#s_stat = [randint(self, 1, 50), randint(self, 1, 50), randint(self, 1, 50)]
#v_stat = [randint(self, 1, 1000), randint(self, 30, 100), randint(self, 30, 100)]

HP = randint(1, 100)
ATK = randint(1, 100)
DEF = randint(1, 100)

s_HP = randint(1, 100)
s_ATK = randint(1, 20)
s_DEF = randint(1, 30)
    
def setup(HP, ATK, DEF): # sets player's stats
    HP = randint(1, 100)
    ATK = randint(1, 100)
    DEF = randint(1, 100)

def s_setup(s_HP, s_ATK, s_DEF): # sets stormtrooper stats
    s_HP = randint(1, 100)
    s_ATK = randint(1, 20)
    s_DEF = randint(1, 30)

def v_setup():
    v_stat = [randint(1, 1000), randint(30, 100), randint(30, 100)]
    
def attack():
    if ATK > s_DEF:
        s_HP -= ATK
        win()
        
def defend():
    if s_ATK > DEF:
        HP -= s_ATK
        win()
        
def win():
    if s_HP or v_HP <= 0:
        print "You won!"
        win = True
    elif HP <= 0:
        print "You lost!"
        dead()
        
def start():

    #setup(HP, ATK, DEF)
    print "Choose your character: Female or Male"
    gender = raw_input("> ")
    print "Enter a name for your character:"
    name = raw_input("> ")
    print "Welcome %s , you are a Jedi Padawan and your master has been captured. You must rescue her!" % name
    print "Your HP is %d, your ATK is %d, and your DEF is %d" % (HP, ATK, DEF)
    print "You have snuck into the secret Resistance facility on Jakar where they are keeping your Master through the garbage chute."
    print "You see a door to your left and to your right. Which one do you go through?"
    door = raw_input("> ")
    
    if door == "right":
        vader_room()
    elif door == "left":
        storm_room()
    else:
        dead("You took too long! The stormtroopers have found you!")
        
def storm_room():
    #s_setup(s_HP, s_ATK, s_DEF)
    storm = True
    print "You come face to face with one of those stormtroopers."
    print "You know about their infamous aim, but you shouldn't underestimate them."
    print "attack or defend?"
    move = raw_input("> ")
    
    while (win == False):
        if move == "attack":
            attack()
        if move == "defend":
            defend()
            
    print "You crushed that stormtrooper like a fly! Now you have a door to your right and to your left."
    door = raw_input("> ")
    
    if door == "right":
        vader_room()
    elif door == "left":
        puzzle_room()
    else:
        dead("You took too long! The stormtroopers have found you!")
        
def vader_room():
    vader = True
    print "You come face to face with Darth Vader."
    print "He is the ultimate Sith lord. Be ware. "
    print "attack or defend?"
    move = raw_input("> ")
    
    while (win == False):
        if move == "attack":
            attack()
        if move == "defend":
            defend()
            
    print "You defeated Darth Vader! How in the world...?! Now you have a door to your right and your left"
    door = raw_input("> ")
    
    if door == "right":
        storm_room()
    elif door == "left":
        puzzle_room()
    else:
        dead("You took too long! The stormtroopers have found you!")
    
def dead(why):
    print why
    print "You died. Try again?"
    ans = raw_input("> ")
    if ans == "yes":
        start()
    else: 
        exit(0)

def puzzle_room():
    puzzle = """ 
    You must solve three puzzles: \n \n
    1. Luke has a mass of 68kg. His lasso rope has a breaking tension of 500N. 
    If he swings on his lasso rope at a constant velocity of 20 m/s, will the rope break? 
    What will his velocity have to be inorder for the rope not to break? \n \n
    2. Darth Vader's voice has a frequency of 350 Hz when heard from afar. What will his 
    new frequency be when he starts running towards you at 300 m/s? \n \n    
    3. Stormtroopers have on average, a 20% probability of hitting their target. What will 
    be the expected number of hits for a stormtrooper who has fired 100 shots? 
    """
    print "-"*25
    print puzzle
    print "-"*25
    print "Puzzle one answer:"
    ans = raw_input("> ")
    print "Puzzle two answer:"
    ans2 = raw_input("> ")
    print "Puzzle three answer:"
    ans3 = raw_input("> ")
    
    if ans == "30" and ans2 == "30" and ans3 == "40":
        print "Congrats! You pass! You have unlocked the door to the chamber where your master is held captive."
        master_room()
    else:
        dead("Oh no! You failed.")
def master_room():
    print "You find your master in a cyrostasis chamber. He is currently immobile. What do you do next?"
    ans = raw_input("> ")
    
start()

