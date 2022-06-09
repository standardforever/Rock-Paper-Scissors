#!/usr/bin/python3

import random


def tie(player, cpu):
    dic = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}
    for key in dic:
        if key == player:
            print("Player({}) : CPU({})".format(dic[key],dic[key]))
            print("Tie")
            print(" ")

def winner(player, cpu):
    dic = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}

    if player == "R" and cpu == "S":
        print("Player({}) : CPU({})".format(dic["R"], dic["S"]))
        print("Player is the Winner")

    elif player == "S" and cpu == "R":
        print("Player({}) : CPU({})".format(dic["S"], dic["R"]))
        print("CPU is the Winner")
    
    elif player == "P" and cpu == "R":
        print("Player({}) : CPU({})".format(dic["P"], dic["R"]))
        print("Player is the Winner")

    elif player == "R" and cpu == "P":
        print("Player({}) : CPU({})".format(dic["R"], dic["P"]))
        print("CPU is the Winner")

    elif player == "S" and cpu == "P":
        print("Player({}) : CPU({})".format(dic["S"], dic["P"]))
        print("Player is the Winner")

    elif player == "P" and cpu == "S":
        print("Player({}) : CPU({})".format(dic["P"], dic["S"]))
        print("CPU is the Winner")



list = ["R", "P", "S"]
while 1:
    print("Pick an opiton between")
    print("'R', 'P', or 'S'.")
    print("------------------")
    choice = input("Enter your choice: ")

    count = 0
    for i in list:
        if i == choice:
            count += 1

    if count != 1:
        print("Wrong input Please try again")
        print(" ")
    else:
        CPU = random.choice(list)
        if choice == CPU:
            tie(choice, CPU)
            continue
        else:
            winner(choice, CPU)
            break

