from sys import exit # class quitter 

def gold_room(): # defines gold room 
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next) 
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
        
    else:
        dead("You greedy bastard!")
        
def bear_room(why): # defines room with room
    print why
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True: # while loop (infinite)
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def trap_room():
    print "This room is full of traps: spikes and hidden potholes."
    print "There are three buttons."
    print "You have to press the three buttons in a certain way so the door opens"
    print "Which button will you press first?"
    
    door_open = False
    
    next = raw_input("> ")
    
    if next == "2":
        print "What will you press next?"
        next2 = raw_input("> ")
        
        if next2 == "1":
            print "What will you press next?"
            next3 = raw_input("> ")
            if next3 == "3":
                bear_room("Yes the door opened!")     
            else:
                dead("Oh no, you got hit by an arrow!")
        else:
            dead("Oh no, one of the spikes just impaled you!")
    else:
         cthulhu_room("Oh no, you fell through a trap door!")       
            
def cthulhu_room(): 
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at uou and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0) # aborts the game
    
def start(): # sets the beginning of the game
    print "You are in a dark room."
    print "There is a door to your right, infront of you and to your left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room("Hello world!")
    elif next == "right":
        cthulhu_room()
    elif next == "infront":
        trap_room()
    else:
        dead("You stumble around the room until you starve.")
start() # initializes the game
    
