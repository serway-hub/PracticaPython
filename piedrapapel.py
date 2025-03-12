import random

option = ("piedra","papel","tijera")
computer_win =0
user_win =0

round = 1
while True:
    print("*" * 10)
    print("ROUND", round)
    print("*"*10)

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in option:
        print("la opcion no es valida")
        continue

    computer_option = random.choice(option)

    print("user option =>", user_option)
    print("Computer option =>", computer_option)

    if user_option == computer_option:
        print("¡Empate")
    elif user_option == "piedra":
        if computer_option == "papel":
            print(f"{computer_option} gana a {user_option}")
            print(f"Cumputador gana con {computer_option}")
            computer_win += 1
        else:
            if computer_option=="tijera":
                print(f"{user_option} gana a {computer_option}")
                print(f"Usuario gana con {user_option}")
                user_win += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print(f"{user_option} gana a {computer_option}")
            print(f"Usuario gana con {user_option}")
            user_win += 1
        else:
            if computer_option=="piedra":
                print(f"{computer_option} gana a {user_option}")
                print(f"Computador gana con {computer_option}")
                computer_win += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print(f"{user_option} gana a {computer_option}")
            print(f"Usuario gana con {user_option}")
            user_win += 1
        else:
            if computer_option=="tijera":
                print(f"{computer_option} gana a {user_option}")
                print(f"Computador gana con {computer_option}")
                computer_win += 1
    if computer_win == 2:
        print(f"Total rondas => {round}")
        print(f"numero de victorias del computador {computer_win}")
        print(f"numero de victorias del computador {user_win}")
        print("El ganador es la Computadora")
        
        break
    if user_win == 2:
        print(f"Total rondas => {round}")
        print(f"numero de victorias del computador {computer_win}")
        print(f"numero de victorias del usuario {user_win}")
        print("El ganador es el usuario")
        break

    round +=1
        
