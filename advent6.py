import re
import math

def part1():
    for t, d in zip(times, distances):
        #print(t,d)
        delta = t*t - 4 *d
        tmax = (-t-math.sqrt(delta))/(-2)
        tmin = (-t+math.sqrt(delta))/(-2)
        t_t_max = math.floor(tmax)
        t_t_min = math.ceil(tmin)
        #print(delta, tmin, t_t_min, tmax, t_t_max)
        num_sol = t_t_max - t_t_min +1
        
        if(t_t_max == tmax):
            num_sol -= 1
        if t_t_min == tmin:
            num_sol -= 1
        #print(num_sol)
        total *= num_sol

def main():
    f = open('advent6_input.txt', 'r') #advent6_input
    content = f.read().splitlines()

    """times = [int(x) for x in re.findall(r'\d+',content[0].split(":")[1])] 
    distances = [int(x) for x in re.findall(r'\d+',content[1].split(":")[1])] """
    times = int(content[0].split(':')[1].replace(" ", ""))
    distances = int(content[1].split(':')[1].strip().replace(" ", ""))

    total = 1
    print(times, distances)
    t = times
    d = distances
    delta = t*t - 4 *d
    tmax = (-t-math.sqrt(delta))/(-2)
    tmin = (-t+math.sqrt(delta))/(-2)
    t_t_max = math.floor(tmax)
    t_t_min = math.ceil(tmin)
    #print(delta, tmin, t_t_min, tmax, t_t_max)
    num_sol = t_t_max - t_t_min +1
    
    if(t_t_max == tmax):
        num_sol -= 1
    if t_t_min == tmin:
        num_sol -= 1
    #print(num_sol)
    total *= num_sol
    print(total)
    return 0


if __name__ == "__main__":
    main()