import re
import pandas as pd

def main():
    f = open('advent4_input.txt', 'r') #advent4_input
    content = f.read().splitlines()

    #sum = 0
    df = pd.DataFrame(columns=['card nb','amount', 'winning numbers', 'my numbers'])
    df['card nb'] = range(len(content))
    df['amount'] = 1
    
    for i,line in enumerate(content):
        #card_score = 0
        game = line.split(':')[1]
        winning_numbers, my_numbers = game.split('|')
        winning_numbers = re.findall(r'\d+', winning_numbers)
        my_numbers = re.findall(r'\d+', my_numbers)
        df.at[i, 'winning numbers']=winning_numbers
        df.at[i, 'my numbers']=my_numbers
        for k in range(df.loc[i,'amount']):
            matching_numbers = 0
            for num in my_numbers:
                for win in winning_numbers:
                    if num ==  win:
                        matching_numbers += 1
                        #card_score = 1 if card_score == 0 else card_score * 2
            #sum += card_score
            #print(winning_numbers, my_numbers)
            for j in range(matching_numbers):
                df.loc[i+j+1, 'amount'] += 1

    #print(sum)
    
    print(df)
    print(df['amount'].sum())
    return 0

if __name__ == "__main__":
    main()