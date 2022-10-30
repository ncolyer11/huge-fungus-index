from random import randint
import json

# input("Enter hatheight/trunkheight: ")
T = [24,26]
N = 0
trunkHeight = 16
hatHeight = 13  # randint(4, 13)
while trunkHeight < 27:
    trunkHeight = T[N]
    offset = trunkHeight - hatHeight
    # print(hatHeight)
    layer = offset
    # print(layer)
    if 8 < hatHeight <= 13:
        air = [0] * offset
        constantA = [2, 1, 1]
        twos = [2] * (hatHeight - 6)
        three = [3]
        vinesThree = [3, 3, 3]
        vinesTwo = []
    elif 4 < hatHeight <= 8:
        air = [0] * offset
        constantA = [2, 1, 1]
        twos = [2] * (hatHeight - 5)
        three = []
        vinesThree = []
        vinesTwo = [2, 2, 2]
    elif hatHeight == 4:
        air = [0] * offset
        constantA = [1, 1]
        twos = []
        three = []
        vinesThree = []
        vinesTwo = [2, 2, 2]
    else:
        raise TypeError("invalid parameter input")

    radii = air + vinesTwo + vinesThree + three + twos + constantA

    Y = 0
    n = 0
    with open(str(trunkHeight) + 'T' + str(hatHeight) + 'H' + '.txt', 'w') as file:

        while Y <= trunkHeight:
            X = -1 * radii[n]
            while X <= radii[n]:
                Z = -1 * radii[n]
                while Z <= radii[n]:
                    bl2 = X == radii[n] or X == -radii[n]
                    bl3 = Z == radii[n] or Z == -radii[n]
                    bl6 = Y < offset + 3
                    if X == 0 and Z == 0 and Y != trunkHeight:
                        L = 100
                        S = 0
                        W = 0
                        region = 'trunk'
                    elif bl6 and (bl2 or bl3):
                        L = 0
                        S = 0
                        W = 27.1125
                        region = 'vines'
                    elif bl6 and not (bl2 or bl3):
                        L = 0
                        S = 0
                        W = 0
                        region = 'air'
                    elif bl2 and bl3:
                        L = 0
                        S = 1
                        W = 69.3
                        region = 'corners'
                    elif not bl2 and not bl3 and Y != trunkHeight:
                        L = 0
                        S = 10
                        W = 18
                        region = 'internal'
                    else:
                        L = 0
                        S = 0.05
                        W = 97.951
                        region = 'external'
                    file.write(json.dumps([[X, Y, Z], ['stem%: ' + str(L), 'shrooms%: ' + str(S), 'wart%: ' + str(W)], region]))
                    file.write('\n')

                    Z += 1
                X += 1
            Y += 1
            n += 1
        N += 1

print(radii)

