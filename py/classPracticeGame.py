#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from random import randint
import time

sense = "That makes no sense.\nTry again!"
wait2 = time.sleep(2)
wait4 = time.sleep(4)
# print "\n" * 100


class Scene(object):
    def enter(self):
        print "This is a class, from which other classes get their " "characteristics\n Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        #        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        #        print "Play's first scene", current_scene

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            #            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)


#            print "map returns new scene", current_scene


class Bar(Scene):
    def enter(self):
        print "You are in a bar and are told a general strike starts in"
        print "10 minutes. You have just paid for a beer. What are you going to"
        print "do, 'wait for change' or 'run' for the bus?"

        action = raw_input("\n>").lower()

        if action == "run":
            print "You just knocked over a few people running"
            print "out the door, but who cares. You made the bus"
            print "\n" * 100
            return "close"

        elif action == "wait for change":
            print "You missed the bus, so you run for the metro"
            print "Just as you get there the train arrives"

            metrodec = raw_input("'Jump the barrier' or 'pay'\n>").lower()

            if metrodec == "jump the barrier":
                print "Good choice"
                print "\n" * 100
                return "close"
            elif metrodec == "pay":
                print """Good citizen. Stupid Person.\nYou obeyed the rules
                but missed the train!"""
                print "\n" * 100
                return "missed"

            else:
                print sense
                print "\n" * 100
                return "bar"

        else:
            print sense
            print "\n" * 100
            return "bar"


class Missed(Scene):
    def enter(self):
        print "You missed the last metro, last bus and have very little money"
        print "What are you going to do?"
        misseddec = raw_input("'ATM' or 'walk'\n>").lower()

        if misseddec == "atm":
            print "\n" * 100
            return "atm"

        elif misseddec == "walk":
            print "\n" * 100
            return "street"

        else:
            print "Makes no sense"
            print "\n" * 100
            return "missed"


class Metro(Scene):
    def enter(self):
        pass


class Bus(Scene):
    def enter(self):
        pass


class Robbed(Scene):
    def enter(self):
        print "Even though it is a nice night"
        print "There is a general strike. Do you even use your brain??"
        print "Every scumbag in the city was out robbing people who " "were as dumb as you"
        print "You return home, robbed and upset!"
        wait4
        return "home"


class Close(Scene):
    def enter(self):
        print "The strike starts and you are 14 blocks from home"
        print "but you have no money. Do you go to an 'ATM' and get a taxi"
        print "or are you going to 'walk'?"

        closedec = raw_input("'atm' or 'walk?'").lower()  # 43.07.42.08

        if closedec == "atm":
            return "atm"

        elif closedec == "walk":
            return "street"
        else:
            print "Makes no sense"
            return "close"


class ATM(Scene):
    def enter(self):
        print "Now you are at the ATM, but what is your pin?"
        print "You can remember the first two and last number"
        print "4, 3, 7 - But what is the 3rd number"
        print "You only have 3 goes?"

        code = "%d%d%d%d" % (4, 3, randint(0, 9), 7)
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 2:
            print "\nWrong pin %r more attempts!" % (2 - guesses)
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "You got cash!"
            time.sleep(2)
            print "\n" * 100
            return "taxi"

        else:
            print "You forgot your pin!!"
            print "This is crap!"
            return "street"


class Taxi(Scene):
    def enter(self):
        print "You have the money and cruise home in a taxi"
        print "Just as you get to your street you see a dodgy"
        print "looking group of guys."
        print "Do you avoid them or say hello?"

        hello = str(raw_input("'hello' or 'avoid'?\n> ").lower())

        if hello == "hello":
            print "They are your neighbours and say hi and one of their"
            print "dogs runs over and you rub it before going in your door"
            return "beer"

        elif hello == "avoid":
            print "you have to jump a wall."
            time.sleep(2)
            print "Bang! Ouch! You just landed really badly"
            print "The guys are approaching!! Oh no"
            time.sleep(2)
            return "hospital"

        else:
            print "Makes no sense"
            return "taxi"


class Street(Scene):
    def enter(self):
        print "Just as you get to your street you see a dodgy"
        print "looking group of guys."
        print "Do you avoid them or say hello?"

        hello = str(raw_input("'hello' or 'avoid'?\n> ").lower())

        if hello == "hello":
            print "They are your neighbours and salute you,one of their"
            print "dogs even runs over to play with you, you eventually" " go in your door"
            return "beer"

        elif hello == "avoid":
            print "To avoid the group you have to climb a wall, but it's dark!"
            print "Do you go back to the street, or jump off the wall!"

            jump = raw_input("'Jump' or 'Return\n> ")

            if jump == "jump":
                time.sleep(1)
                print "ouch, you just landed really badly!"
                time.sleep(3)
                print "\n" * 100
                return "hospital"

            elif jump == "return":
                print "You are back on your street"
                return "street"

            else:
                print sense
                return "Street"

        else:
            print sense
            return "taxi"


class Hospital(Scene):
    def enter(self):
        print "Well done, you ended up in hospital! One of the dodgy " "looking guys was very nice and brought you in"
        print "Your ankle is broken, and you will be on crutches"
        print "Now you have no money, can't walk and are down to the " "final option"
        print "Call 'mam' or 'dad'?"

        hospital = raw_input("'mam' or 'dad'?").lower()

        if hospital == "mam":
            print "OMG, you poor thing, are you OK?"
            print "We will be there in 20 minutes to collect you"
            time.sleep(3)
            print "\n" * 100
            return "parents"

        elif hospital == "dad":
            print "\n" * 100
            print "Dad > How the hell did you manage that, were you drunk?"
            print "I broke my leg once and still went to work the next day"
            print "and I never took a sick day in my life. I'll be there in " "20 minute."
            print "Did you leave the dog out today?"

            dog = raw_input("'yes' or 'no'?>").lower()

            if dog == "yes":
                print "Well, at least you managed something"
                return "parents"

            elif dog == "no":
                print "What did you get a dog for. You can barely care for yourself!"
                print "Now that poor animal has been locked up all day"
                print "I'll be there in 20 minutes, but we will have to go and get your dog!"
                return "dog"

            else:
                print "makes no sense"
                return "hospital"

        else:
            print "makes no sense"
            return "Hospital"


class Parents(Scene):
    def enter(self):
        print "So, mommy brings you home!"
        print "Nice job!"
        time.sleep(2)
        return "pyjames"


class Pyjames(Scene):
    def enter(self):
        print "You have no clothes left at home...except an old pair of superman pyjames"
        print "You're mother insists you put them on and begins asking you all"
        print "about your personal life. You really didnt want this....but"

        excall = raw_input(
            "You know your ex will save you, but .... do you make the call\n> 'yes' or 'no'"
        ).lower()

        if excall == "yes":
            print "\n " * 100
            print "Your ex is on the way. You are still in the superman pyjames!"
            print "But at this point you don't care!"
            return "home"

        elif excall == "no":
            print "\n" * 100
            print "Staying strong! Good work"
            print "Now you mother is wants to know why you guys broke up"
            return "home"

        else:
            print sense
            return "pyjames"


class Dog(Scene):
    def enter(self):
        print "You get home and your dog has ripped the place apart"
        print "Your 'best friend' has felt obliged to make you realise"
        print "how much of an idiot you have been. Just to hammer the message home"
        return "home"


class Home(Scene):
    quips = [
        "Some of your best work!Maybe don't try leaving the house for a while",
        "You're home, you can cry now!",
        "You are home. Think about the decisions you just made",
        "It'll be hard have another day as bad as that!",
    ]

    def enter(self):
        print Home.quips[randint(0, len(self.quips) - 1)]
        exit(1)


class Beer(Scene):
    quips = [
        "You made it, grab a beer!",
        "Beer, why not make it a whiskey!",
        "You are home. Have a hot chocolate, with some fig rolls",
        "YaY! What a great day! Beer and bed!",
    ]

    def enter(self):
        print Beer.quips[randint(0, len(self.quips) - 1)]
        exit(1)


class Map(object):

    scenes = {
        "bar": Bar(),
        "dog": Dog(),
        "atm": ATM(),
        "beer": Beer(),
        "Metro": Metro(),
        "hospital": Hospital(),
        "parents": Parents(),
        "Bus": Bus(),
        "close": Close(),
        "home": Home(),
        "taxi": Taxi(),
        "missed": Missed(),
        "robbed": Robbed(),
        "street": Street(),
        "pyjames": Pyjames(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    #        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        #        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        #        print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("bar")
a_game = Engine(a_map)
a_game.play()
