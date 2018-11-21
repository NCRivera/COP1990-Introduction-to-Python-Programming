players = 5
soccerTeam = {}
menuOp = 'yay'

for player in range(players):
    try:
        jersey = int(input("Enter player %d's jersey number:\n" % (player + 1)))
        rating = int(input("Enter player %d's rating:\n" % (player + 1)))
        soccerTeam[jersey] = rating
        print('')
    except ValueError:
        jersey = int(input("Enter player %d's jersey number:\n" % (player + 1)))
        rating = int(input("Enter player %d's rating:\n" % (player + 1)))
        soccerTeam[jersey] = rating
        print('')

jerseyList = sorted(soccerTeam.keys())

print('ROSTER')
for i in jerseyList:
    print('Jersey number: %d, Rating: %d' % (i, soccerTeam[i]))

while menuOp != 'q':
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    
    menuOp = input('Choose an option:\n')
    
    if menuOp == 'a':
        jersey = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter player's rating:\n"))
        soccerTeam[jersey] = rating

    if menuOp == 'd':
        jersey = int(input("Enter a jersey number:\n"))
        del soccerTeam[jersey]

    if menuOp == 'u':
        jersey = int(input("Enter a jersey number:\n"))
        rating = int(input("Enter a new rating for player:\n"))
        soccerTeam[jersey] = rating

    if menuOp == 'r':
        rating = int(input("Enter player's rating:\n"))
        print("ABOVE", rating)
        for i in jerseyList:
            if soccerTeam[i] > rating:
                print('Jersey number: %d, Rating: %d' % (i, soccerTeam[i]))
            else:
                continue

    if menuOp == 'o':
        jerseyList = sorted(soccerTeam.keys())
        print('ROSTER')
        for i in jerseyList:
            print('Jersey number: %d, Rating: %d' % (i, soccerTeam[i]))

    if menuOp == 'q':
        continue
    
