import numpy as np
from collections import Counter
import pandas as pd

dic_points1 = {'A':14, 'K':13, 'Q':12, 'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
dic_points2 = {'A':14, 'K':13, 'Q':12, 'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2, 'J':1}
reverse_dic = { v:k for k,v in dic_points2.items()}

def readFile():
    f = open('advent7_input.txt', 'r') #advent7_input
    content = f.read().splitlines()
    return content

def getType(two, three, four, five):
    if(five):
        return "five"
    if(four):
        return "four"
    if(three == 1 and two == 0):
        return "three"
    if(three == 1 and two == 1):
        return "full"
    if(two == 2):
        return "two pair"
    if(two == 1):
        return "one pair"
    return "high card"

def adaptWithJokers(hand):
    if any("J" in s for s in hand): 
        list_of_values = [dic_points2.get(item,item)  for item in hand]
        # Get unique values and counts
        unique_values, counts = np.unique(list_of_values, return_counts=True)

        # Sort counts and get corresponding indices
        sorted_indices = np.argsort(counts)

        # Sort unique values based on counts
        sorted_unique_values = unique_values[sorted_indices]
        sorted_counts = counts[sorted_indices]
        if(len(sorted_counts) == 1):
            m = sorted_counts[-1]
        else:
            m = sorted_counts[-1] if sorted_unique_values[-1] != 1 else sorted_counts[-2]
        #print(sorted_counts, sorted_unique_values, m)
        all_max_oc = [i for i, j in enumerate(sorted_counts) if j == m]
        temp = 0
        for oc in all_max_oc:
            if sorted_unique_values[oc] > temp:
                best_card = sorted_unique_values[oc]
        new_hand = [best_card if item == 1 else item for item in list_of_values]
        #print(hand, new_hand, best_card)
        return new_hand
    return hand
        

def analyzeHand(hand):
    #print(hand)
    #print(Counter(hand).keys(), Counter(hand).values())
    #print(Counter(Counter(hand).values()).keys())
    two= three= four= five = 0
    new_hand = adaptWithJokers(hand)
    for val in Counter(new_hand).values():
        match val:
            case 2:
                two += 1
            case 3: 
                three += 1
            case 4:
                four += 1
            case 5:
                five += 1
    type = getType(two, three, four, five)
    return type
                

def main():
    content = readFile()
    df = pd.DataFrame(columns=['hand','type', 'rank', 'bid'])

    for line in content:
        hand, bid = line.split(" ")
        type =  analyzeHand(list(hand))
        #print(type, hand)
        df = pd.concat([df, pd.DataFrame([{'hand':hand, 'type':type, 'rank': -1, 'bid':int(bid), 'firstCard':hand[0], 'secondCard':hand[1], 'thirdCard':hand[2], 'fourthCard':hand[3], 'fifthCard':hand[4]}])], ignore_index=True)
        
        #df.append({'hand':hand, 'type': analyzeHand(list(hand)), 'rank': -1, 'bid':bid}, ignore_index = True)
        #analyzeHand(list(hand))
    rank = 1
    finaldf = pd.DataFrame()
    totalwinnings = 0
    for type in ['high card', 'one pair', 'two pair', 'three', 'full', 'four', 'five']:
        subdf = df.loc[df['type'] == type].copy()
        subdf=subdf.replace({'firstCard':dic_points2, 'secondCard':dic_points2, 'thirdCard':dic_points2, 'fourthCard':dic_points2, 'fifthCard':dic_points2})
        subdf = subdf.sort_values(['firstCard', 'secondCard', 'thirdCard', 'fourthCard', 'fifthCard'], ascending=[True, True, True, True, True])
        subdf['rank'] = range(rank,len(subdf) + rank )
        subdf['score'] = subdf['rank'] * subdf['bid']
        rank += len(subdf)
        totalwinnings += subdf['score'].sum()
        #finaldf = pd.concat([finaldf, subdf])
        print(subdf)
    print(totalwinnings)
    return 0

if __name__ == "__main__":
    main()