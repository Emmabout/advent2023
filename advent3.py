import re
import numpy as np


def sol():
    def scanNumber(i,j):
        if i>len(board) or j >len(board[0]) or i < 0 or j < 0 or (i,j) in seenAlready: return 0
        if not board[i][j].isnumeric(): return 0
        digits = board[i][j]
        seenAlready.append((i,j))
        # scan left
        lj = j - 1
        while lj >= 0:
            if not board[i][lj].isnumeric(): break
            digits = board[i][lj] + digits
            seenAlready.append((i,lj))
            lj -= 1
        # scan right
        rj = j + 1
        while rj < len(board[0]):
            if not board[i][rj].isnumeric(): break
            digits = digits + board[i][rj]
            seenAlready.append((i,rj))
            rj += 1
        #print(digits)

        return int(digits)
        

    def getAdjacentNumbers(i,j):
        nw = scanNumber(i-1,j-1)
        n = scanNumber(i-1,j)
        ne = scanNumber(i-1,j+1)
        w = scanNumber(i,j-1)
        e = scanNumber(i,j+1)
        sw = scanNumber(i+1,j-1)
        s = scanNumber(i+1, j)
        se = scanNumber(i+1, j+1)
        return nw+n+ne+w+e+sw+s+se
    board = []
    seenAlready = []
    total = 0
    with open("advent3_input.txt", 'r') as f: board = [[c for c in line.rstrip()] for line in f]
    for i, line in enumerate(board):
        for j,c in enumerate(line):
            if not c.isnumeric() and c!='.':
                # symbol hit
                total += getAdjacentNumbers(i,j)
    print(total)
    return seenAlready

def has_neighbour_in_line(number, line):
    idx = line.index(str(number))
    has_neighbour = 0
    if(idx > 0):
        if(line[idx-1] != '.' and not line[idx-1].isdigit()):
            has_neighbour = 1
    if(idx + len(str(number))<=len(line)-1):
        if(line[idx+len(str(number))] != '.' and not line[idx+len(str(number))].isdigit()):
            has_neighbour = 1
    return has_neighbour

def has_neighbour_in_adjacent_line(number, line, adjline):
    idx = line.rfind(str(number))
    has_neighbour = 0
    min_idx = max(0,idx - 1)
    max_idx = min(idx+len(str(number)), len(line)-1)
    for i in range(min_idx, max_idx+1):
        if(adjline[i] != '.' and not adjline[i].isdigit()):
            has_neighbour = 1
    return has_neighbour

def setdiff2d_list(arr1, arr2):
    delta = set(map(tuple, arr2))
    return np.array([x for x in arr1 if tuple(x) not in delta])

def part1(test):
    liste = []
    mySeen = []
    sum = 0
    for i, line in enumerate(test):
        #print(line)
        digits = re.findall(r'\d+', line)#[int(s) for s in line.split('.') if s.isdigit()]
        for digit in digits:
            for j in range(len(str(digit))):
                mySeen.append((i,line.index(str(digit))+j))
            has_neighbour = 0
            if(i == 0):
                has_neighbour = has_neighbour_in_line(digit, line) or has_neighbour_in_adjacent_line(digit, line, test[i+1])
            elif i== len(test) -1:
                has_neighbour = has_neighbour_in_line(digit, line) or has_neighbour_in_adjacent_line(digit, line, test[i-1])
            else:
                has_neighbour = has_neighbour_in_line(digit, line) or has_neighbour_in_adjacent_line(digit, line, test[i+1]) or has_neighbour_in_adjacent_line(digit, line, test[i-1])
            if(has_neighbour):
                liste.append(digit)
                sum += int(digit)
                print(i,digit)



def scan_around(content, line, col):
    def find_number(content, i, j):
        if i<0 or j<0 or i>len(content)-1 or j>len(content[0])-1: return 0
        var = content[i][j]
        number = ''
        if var.isdigit():
            #scan left
            col_nb=j
            while col_nb >= 0 and content[i][col_nb].isdigit():
                char = content[i][col_nb]
                number = char + number
                col_nb -= 1
            # scan right
            col_nb = j+1
            while col_nb < len(content[0]) and content[i][col_nb].isdigit():
                char = content[i][col_nb]
                number = number + char
                col_nb += 1
        print("number", number)
        return int(number) if number !='' else 0

    print('-----')
    tl = find_number(content, line-1, col-1)
    t  = find_number(content, line-1, col)
    tr = find_number(content, line-1, col+1)
    ml = find_number(content, line, col-1)
    mr = find_number(content, line, col+1)
    bl = find_number(content, line+1, col-1)
    b  = find_number(content, line+1, col)
    br = find_number(content, line+1, col+1)
    unique_nb = np.unique([tl, t, tr, ml, mr, bl, b, br])
    unique_nb = [i for i in unique_nb if i != 0]
    print(unique_nb)
    if(len(unique_nb) == 2):
        return unique_nb[0] * unique_nb[1]
    else:
        return 0


def main():
    """ Main program """
    f = open('advent3_input.txt', 'r') #advent3_input
    content = f.read().splitlines()
    #print(content)

    test = content
    sum = 0
    for i,line in enumerate(test):
        
        asteriscs = [i for i, char in enumerate(line) if char == '*']
        for ast in asteriscs:
            sum += scan_around(content, i, ast)
        

    print(sum)

    
    return 0


if __name__ == "__main__":
    main()