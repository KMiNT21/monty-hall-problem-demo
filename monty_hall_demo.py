import random
import time

#################################
player_allways_change_door = True
#################################

game_number = 0
successful_guessing = 0

while game_number < 10999:

    game_number += 1
    doors = ["car", "goat", "goat"]
    random.shuffle(doors)
    print()
    print()
    print(f"All closed doors: {doors}")

    choices_list = [0, 1, 2]
    player_choice = random.choice(choices_list)
    print(f"Player select door number {player_choice+1}")

    host_choices_list = [0, 1, 2]
    host_choices_list.remove(doors.index('car'))

    if doors[player_choice] == 'car':
        host_open_choice = random.choice(host_choices_list)
    else:
        host_choices_list.remove(player_choice)
        host_open_choice = random.choice(host_choices_list)  # always 1 element left

    print("Host opened one door with goat")
    doors[host_open_choice] = 'GOAT (visible)'
    print(f"Doors: {doors}")


    round2_choices_list = choices_list
    round2_choices_list.remove(host_open_choice)

    if player_allways_change_door:
        print(f"Player decided to change first choice {player_choice+1} to ", end="")
        round2_choices_list.remove(player_choice)
        player_choice = random.choice(round2_choices_list)  # always 1 element left
        print(player_choice+1)

    if doors[player_choice] == 'car':
        successful_guessing += 1

    success_rate = successful_guessing/game_number*100
    print(f'Games: {game_number}, success {successful_guessing} ({success_rate:.2f}%).')

    # time.sleep(1)

