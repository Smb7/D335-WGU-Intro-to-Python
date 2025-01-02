
usrinput = "bloodbourne"

games_list = []

games_list.append(usrinput)

list_of_games = 'God of War', 'Helldivers 2', 'Gotham Knights', 'Horizon Zero Dawn', 'Horizon Forbidden West', 'Elden Ring', 'Cyberpunk'

for game in list_of_games:
    games_list.append(game)

# first way to find an index and value
for index, game in enumerate(games_list):
    userinput = 'Gotham Knights'
    if userinput == game:
        print(f"{index}, {game}")
        inputuser = 'yes'
        if inputuser == 'yes':
            print(index)
            games_list.pop(index)
            print(games_list)

# another way to get index and value
for index in range(len(list_of_games)):
    value = list_of_games[index] 
    print(index, value)
