# Narang, Arjun
# Computer Programming p4
# Project 1 - Option 2: Team Batting Average

player1_name = input("Player 1 Name: ")
player1_ab = int(input("Player 1 At-bats: "))
player1_hits = int(input("Player 1 Hits: "))
player2_name = input("Player 2 Name: ")
player2_ab = int(input("Player 2 At-bats: "))
player2_hits = int(input("Player 2 Hits: "))
player3_name = input("Player 3 Name: ")
player3_ab = int(input("Player 3 At-bats: "))
player3_hits = int(input("Player 3 Hits: "))
player4_name = input("Player 4 Name: ")
player4_ab = int(input("Player 4 At-bats: "))
player4_hits = int(input("Player 4 Hits: "))
player5_name = input("Player 5 Name: ")
player5_ab = int(input("Player 5 At-bats: "))
player5_hits = int(input("Player 5 Hits: "))
player1_ave = player1_hits / player1_ab
player2_ave = player2_hits / player2_ab
player3_ave = player3_hits / player3_ab
player4_ave = player4_hits / player4_ab
player5_ave = player5_hits / player5_ab
total_ab = player1_ab + player2_ab + player3_ab + player4_ab + player5_ab
total_hits = player1_hits + player2_hits + player3_hits + player4_hits + player5_hits
cumulative_ave = total_hits / total_ab
print("\nNAME\t\tAB\tHITS\tAVE")
print(f"{player1_name}\t\t{player1_ab}\t{player1_hits}\t{player1_ave}")
print(f"{player2_name}\t\t{player2_ab}\t{player2_hits}\t{player2_ave}")
print(f"{player3_name}\t\t{player3_ab}\t{player3_hits}\t{player3_ave}")
print(f"{player4_name}\t\t{player4_ab}\t{player4_hits}\t{player4_ave}")
print(f"{player5_name}\t{player5_ab}\t{player5_hits}\t{player5_ave}")
print(f"TOTAL\t\t{total_ab}\t{total_hits}\t{cumulative_ave}\n")
team_overall_ave = 0.253
mlb_overall_ave = 0.245
if team_overall_ave > cumulative_ave:
    print("Team's overall average is higher than the 5 players' average.")
else:
    print("Team's overall average is lower than the 5 players' average.")
if mlb_overall_ave > cumulative_ave:
    print("MLB's overall average is higher than the 5 players' average.")
else:
    print("MLB's overall average is lower than the 5 players' average.")