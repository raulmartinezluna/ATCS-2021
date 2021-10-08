#Modify Game Preferences so your user can add as many games as they like.

games = ["Battlefield", "Call of Duty", "Super Mario Bros", "Fortnite"]


games_print = ""
for game in games:
    games_print += game + ", "

print("I like to play ", games_print[:-2])

not_done = True
while not_done:
    new_game = str(input("What game do you like? "))
    games.append(new_game)
    not_done = bool(input("Do wish to continue? To continue write anything and to stop don't write anything."))

games_print = ""
for game in games:
    games_print += game + ", "
print("We like to play ", games_print[:-2])