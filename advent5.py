import re


def main():
    f = open('advent5_input.txt', 'r') #advent5_input
    content = f.read().splitlines()

    seedsinput = [int(x) for x in re.findall(r'\d+',content[0].split(":")[1])] 
    """seeds = []
    for i in range(0,int(len(seedsinput)/2), 1):
        start = seedsinput[2*i]
        rang = seedsinput[2*i+1]
        for j in range(start, start+rang):
            try:
                seeds.append(j)
            except: 
                print(len(seeds))"""

    seed2soil = content[content.index("seed-to-soil map:")+1:content.index("soil-to-fertilizer map:") -1]
    soil2fertilizer = content[content.index("soil-to-fertilizer map:")+1:content.index("fertilizer-to-water map:") -1]
    fertilizer2water = content[content.index("fertilizer-to-water map:")+1:content.index("water-to-light map:") -1]
    water2light = content[content.index("water-to-light map:")+1:content.index("light-to-temperature map:") -1]
    light2temperature = content[content.index("light-to-temperature map:")+1:content.index("temperature-to-humidity map:") -1]
    temperature2humidity = content[content.index("temperature-to-humidity map:")+1:content.index("humidity-to-location map:") -1]
    humidity2location = content[content.index("humidity-to-location map:")+1:]
    print(seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location)

    for map in [seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location]:
        for i in range(0, int(len(seedsinput)/2)):

            for seed in range(seedsinput[i*2], seedsinput[2*i+1]):

                for line in  map:
                    destination_start, source_start, range_length = [int(x) for x in re.findall(r'\d+', line)]
                    #print("dest start", destination_start, 'source start', source_start, 'range len', range_length)

                    shift = seed-source_start
                    #print('seed', seed, 'shift', shift)
                    if(shift >= 0 and shift < range_length):
                        seedsinput[i] = destination_start + shift

        #print(seeds)
    print(min(seedsinput))
    return 0

if __name__ == "__main__":
    main()