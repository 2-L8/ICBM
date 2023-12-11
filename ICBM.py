import math
import random
from math import atan2
import sys

def game_running():
    print(" " * 26 + "ICBM")
    print(" " * 20 + "CREATIVE COMPUTING")
    print(" " * 18 + "MORRISTOWN, NEW JERSEY")
    print("\n" * 3)
    X1 = 0
    Y1 = 0
    X = random.randint(200, 999)
    Y = random.randint(200, 999)
    S = random.randint(50, 69)
    S1 = random.randint(50, 69)
    print("-------MISSILE-----         ", end="")
    print("--------SAM--------         ------")
    print("MILES"," " * 8 + "MILES"," " * 8 + "MILES"," " * 8 + "MILES"," " * 8 + "HEADING")
    print("NORTH"," " * 8 + "EAST"," " * 9 + "NORTH"," " * 8 + "EAST"," " * 9 + "?")
    print("----------------------------------", end="")
    print("---------------------------")
    
    for N in range(1, 51):
        print(Y, X, Y1, X1, end=' ',sep='            ')
        if X == 0:
            print("\nTHE ICBM JUST HIT YOUR LOCATION!!")
            restart()
        T1 = float(input("           ? "))
        T1 = T1/57.296
        H = random.randint(1, 200)
        if H > 4:
            X1 = int(X1 + S1 * math.sin(T1))
            Y1 = int(Y1 + S1 * math.cos(T1))
        if math.sqrt(X**2+Y**2) > S:
            B = math.sqrt(X**2+Y**2)/1000
            T = atan2(Y, X)
            X = int(X - S * math.cos(T) + random.randint(0, 20))
            Y = int(Y - S * math.sin(T) + random.randint(0, 20))
            D = int(math.sqrt((X-X1)**2 + (Y-Y1)**2))
        elif math.sqrt(X**2+Y**2) < S:
            X = 0
            Y = 0
        if D <= 5:
            print("CONGRATULATIONS!  YOUR SAM CAME WITHIN",D,"MILES OF")
            print("THE ICBM AND DESTROYED IT!")
            break
        print("ICBM & SAM NOW", D, "MILES APART")
        
        
        if H == 1:
            print("TOO BAD.  YOUR SAM FELL TO THE GROUND!")
            restart()
        elif H == 2:
            print("YOUR SAM EXPLODED IN MIDAIR!")
            restart()
        elif H == 3:
            print("GOOD LUCK-THE ICBM EXPLODED HARMLESSLY IN MIDAIR!")
            restart()
        elif H == 4:
            print("GOOD LUCK-THE ICBM TURNED OUT TO BE A FRIENDLY AIRCRAFT!")
            restart()
        
def restart():
    user_input = input("DO YOU WANT TO PLAY MORE? (Y OR N)")
    if user_input.upper() == "Y":
        game_running()
    else:
        sys.exit()
        
game_running()