f = open('advent2_input.txt', 'r')
content = f.read().splitlines()
#print(content)

test = content[:5]
"""f = open('test.txt', 'r')
test = f.read().splitlines()
print(test)"""
bag_r = 12
bag_g = 13
bag_b = 14
sum = 0
sum_powers = 0

for i in range(len(content)):
    possible = 1
    min_r = 0
    min_b = 0
    min_g = 0

    game = content[i].split(":")[1]
    #print(game)
    sets = game.split(";")
    #print(sets)
    for set in sets:
        colors = set.split(",")
        for color in colors:
            if (color.__contains__("blue")):
                digi = [int(s) for s in color.split() if s.isdigit()][0]
                if(digi>min_b):
                    min_b = digi
                if(digi>bag_b):
                    possible = 0
            if (color.__contains__("red")):
                digi = [int(s) for s in color.split() if s.isdigit()][0]
                if(digi>min_r):
                    min_r = digi
                if(digi>bag_r):
                    possible = 0
            if (color.__contains__("green")):
                digi = [int(s) for s in color.split() if s.isdigit()][0]
                if(digi>min_g):
                    min_g = digi
                if(digi>bag_g):
                    possible = 0
    power = min_r * min_g * min_b
    sum_powers += power
    if(possible == 1):
        #print("game", i+1, "possible")
        sum += i+1
print("sum of powers", sum_powers)
print("sum:", sum)

              
                
            