
def read_file():
    f = open('advent8_input.txt', 'r') #advent8_input
    content = f.read().splitlines()
    instructions = content[0]
    nodes = []
    left = []
    right = []
    starting_nodes=[]
    for line in content[2:]:
        node, destinations = line.split('=')
        nodes.append(node.strip())
        lefti, righti = destinations[2:-1].split(',')
        left.append(lefti.strip())
        right.append(righti.strip())
        if(node.strip().endswith('A')):
            starting_nodes.append(node.strip())
    return instructions, nodes, left, right, starting_nodes

def follow_instructions(instructions, nodes, left, right):
    curr_idx = nodes.index('AAA')
    end_idx = nodes.index('ZZZ')
    steps = 0
    z_not_reached = 1
    while z_not_reached:
        for instr in [*instructions]:
            if instr == 'L':
                next_node = left[curr_idx]
            elif instr == 'R':
                next_node = right[curr_idx]
            curr_idx = nodes.index(next_node)
            steps += 1
        if(next_node == 'ZZZ'):
            z_not_reached = 0
    print(steps)
        
def follow_part2(instructions, nodes, left, right, starting_nodes):
    curr_nodes = starting_nodes
    not_all_z = 1
    steps = 0
    while not_all_z:
        for instr in [*instructions]:
            if instr == 'L':
                for i,node in enumerate(curr_nodes):
                    idx = nodes.index(node)
                    next_node = left[idx]
                    curr_nodes[i] = next_node

            elif instr == 'R':
                for i,node in enumerate(curr_nodes):
                    idx = nodes.index(node)
                    next_node = right[idx]
                    curr_nodes[i] = next_node
            #print(curr_nodes)
            steps += 1
        not_all_z = 0
        for node in curr_nodes:
            if not node.endswith('Z'):
                not_all_z = 1

    print(steps)

def main():
    instructions, nodes, left, right, starting_nodes = read_file()
    #follow_instructions(instructions, nodes, left, right)
    follow_part2(instructions, nodes, left, right, starting_nodes)
    return 0


if __name__ == "__main__":
    main()