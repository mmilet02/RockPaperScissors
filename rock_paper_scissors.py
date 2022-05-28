import random

print("Welcom to Rock Paper Scissors game. You are playing against computer. Side which gets 3 points fatser is a winner. Good Luck :)")

the_end = False
points_table = [0, 0]
round = 0
while not(the_end):
    round += 1
    print("ROUND "+ str(round) + ".")
    print("SCORE: Computer [" + str(points_table[0]) + "] : [" + str(points_table[1]) + "] You")
    side2 = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor: ")
    if side2.lower() != "r" and side2.lower() != "p" and side2.lower() != "s":
        print("You did not enter valide choice [" + side2 + "]. Try again")
        continue
    side1 = random.choice(["r", "p", "s"])
    print("Computer chose -> " + side1.upper())
    if side1 == side2:
        print("It is a tie.")
    elif (side1 == "r" and side2 =="s") or (side1 == "p" and side2 == "r") or (side1 == "s" and side2 == "p"):
        points_table[0] += 1
        if points_table[0] == 3:
            print("Computer wins :)")
            the_end = True
    else:
        points_table[1] += 1
        if points_table[1] == 3:
            print("Congratulation You win :)")
            the_end = True

