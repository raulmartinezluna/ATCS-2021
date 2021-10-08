#Make a list that includes 3 or 4 games that you like to play.

games = ["Battlefield", "Call of Duty", "Super Mario Bros", "Fortnite"]

#Print a statement that tells the user what games you like.
games_print = ""
for game in games:
    games_print += game + ", "

print("I like to play ", games_print[:-2])

#Ask the user to tell you a game they like, and store the game in a variable such as new_game.

new_game = str(input("What game do you like? "))

#Add the user's game to your list.

games.append(new_game)

#Print a new statement that lists all of the games that we like to play (we means you and your user).
games_print = ""
for game in games:
    games_print += game + ", "
print("We like to play ", games_print[:-2])