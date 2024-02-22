

def minimum_number_of_players(n,k):    
    count = 0
    for i in n:
        if int(i) > k:
            count += 1
    return count


no_of_test_cases = int(input())
if no_of_test_cases >= 1 and no_of_test_cases <=105:
    for i in range(no_of_test_cases):
        no_of_players, height = input().split(" ")
        if int(no_of_players) >=1 and int(no_of_players) <= 105 and int(k)>=1 and int(k)<=105:
            players =input().split(" ")
            if len(players) != int(no_of_players):
                print("Number of players should match with the provided input")
            else:
                output = minimum_number_of_players(players,int(height))
                print(output)
             
        