import numpy as np
import sys

connected_to_n = ['L', '|', 'J']
connected_to_s = ['|', '7', 'F']
connected_to_e = ['-', 'L', 'F']
connected_to_w = ['-', 'J', '7']
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))
def read_file():
    with open("test.txt", "r") as f: #advent10_input
        output_list = []
        for rec in f.read().splitlines():
            list = [rec[i:i+1] for i in range(0, len(rec), 1)]
            output_list.append(list)
    return output_list

def part1(table):
    test = np.array(table)
    path_table = np.zeros(test.shape)

    def scan_around(table, x, y, i):
        #print(table.shape, x, y)
        w  = table[x][y-1] if y>0 else '0'
        n  = table[x-1][y] if x>0 else '0'
        s  = table[x+1][y] if x<table.shape[0]-1 else '0'
        e  = table[x][y+1] if y<table.shape[1]-1 else '0'
        next_positions = []
        if(s in connected_to_n and path_table[x+1, y] == 0):
            next_positions.append([x+1, y])
            path_table[x+1, y] = i
        if(e in connected_to_w and path_table[x, y+1] == 0):
            next_positions.append([x, y+1])
            path_table[x, y+1] = i
        if(w in connected_to_e and path_table[x, y-1] ==0):
            next_positions.append([x, y-1])
            path_table[x, y-1] = i
        if(n in connected_to_s and path_table[x-1, y] ==0):
            next_positions.append([x-1, y])
            path_table[x-1, y] = i
        return next_positions
    
    start_pos = np.argwhere(test == 'S')
    next_positions = scan_around(test, start_pos[0][0], start_pos[0][1], 1)
    i = 2
    pipe_unexplored = 1
    while pipe_unexplored:
        new_pos = []
        for pos in next_positions:
            if np.array(pos).size > 0:
                new_pos.extend(scan_around(test, pos[0], pos[1], i))
        if(new_pos == []):
            pipe_unexplored = 0
        next_positions = new_pos
        i += 1
        
    print(test)
    print(path_table)
    print(np.max(path_table))
    return path_table

def is_long_pipe(table, x, y):
        w  = table[x][y-1] if y>0 else 0
        #e  = table[x][y+1] if y<table.shape[1]-1 else '0'
        actuel = table[x][y]
        if abs(actuel-w) == 1:
            return True
        else:
            return False
    


def part2(path_table):
    in_n_out = np.zeros(path_table.shape)
    for i in range(path_table.shape[0]):
        is_between_pipes = False
        ends_of_line = np.argwhere(path_table[i,:] != 0)
        end_of_line = ends_of_line[-1][0] if len(ends_of_line) else -1

        for j in range(path_table.shape[1]):
            if(i == 4):
                print(is_between_pipes)
            if(is_between_pipes and path_table[i,j] == 0 and j<end_of_line):
                in_n_out[i,j] = 1
            if(path_table[i,j] != 0 and not is_long_pipe(path_table, i,j) and j!= 0):
                is_between_pipes = not is_between_pipes
    print(in_n_out)
    print(in_n_out.sum())





def main():
    table = read_file()
    path_table = part1(table)
    part2(path_table)
    return 0




if __name__ == "__main__":
    main()