import random

#Stores game markers for X an O's. Default is empty.

markers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
gameOn = True

def print_board():
    print(markers[0], " ¦ ", markers[1], " ¦ ", markers[2])
    print("-------------")
    print(markers[3], " ¦ ", markers[4], " ¦ ", markers[5])
    print("-------------")
    print(markers[6], " ¦ ", markers[7], " ¦ ", markers[8])

def ai_Marker():
    aiMarker = random.randrange(0,8)

    while markers[aiMarker] == "X" or markers[aiMarker] == "O":
        aiMarker = random.randrange(0,8)

    markers[aiMarker] = "O"

while gameOn:
    print_board()
    newPossition= int(input("Place X marker in possition 1-2-3-4-5-6-7-8-9? 0 to exit "))

    if newPossition == 0:
        break

    markers[newPossition-1] = "X"
    ai_Marker()