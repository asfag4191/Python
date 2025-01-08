import random

#Define the pokemon options, using dictionary, where the names are the key and the attributes is the nested dictionaries
pokemon_choices={
    "pikachu": {"health": 100, "attack": 20},
    "charmander": {"health": 120, "attack": 15},
    "bulbasaur": {"health": 110, "attack": 18},
    "squirtle": {"health": 130, "attack": 12},
}

user_pokemon = str(input('Choose your Pokémon (Pikachu, Charmander, Bulbasaur, Squirtle): ').lower())


if user_pokemon in pokemon_choices: 
    user_stats=pokemon_choices[user_pokemon] #looks up the value (stats dictionary) for the key user_pokemon. Stores the stats.
    print(f'You choose {user_pokemon} with {user_stats}')
else:
    print('Invalid choice! Try again.')


#Make sure they can't use the same pokemons, that the computer choose another pokemon than the user
while True:
    computer_pokemon=random.choice(list(pokemon_choices.items())) #Use items() to retrieve both the key and values
    computer_name,computer_stats=computer_pokemon
    # Ensure computer doesn't pick the user's Pokémon
    if computer_name != user_pokemon:
        break

print(f"The computer chose {computer_name} with stats: {computer_stats}")


#Fight

user_health=user_stats['health'] #retrieves the values of the pokemons. 
computer_health=computer_stats['health']

user_attack=user_stats['attack'] #retrives the attacks values of the pokemons. 
computer_attack=computer_stats['attack']

print('----Fight starts----')

#keeps going until one of them has less or the same as 0 points, then we have a winne. 
while user_health>0 and computer_health>0: 
    user_block=random.randint(0,10)
    computer_block=random.randint(0,10)

    if user_block in(0,5,8,10): #User does not block
        user_health-=computer_attack
        if user_health<=0:
            print("You loose! Computer wins!")
            break
        print(f'{user_pokemon} has got beaten with {computer_attack}, has now {user_health} points left')
    else:
        print(f'{user_pokemon} has blocked!')

    if computer_block in (0,3,4,9): #Computer does not block
        computer_health-=user_attack
        if computer_health<=0:
            print("You win! Computer loose!")
            break
        print((f'{computer_name} has got beaten with {user_attack}, has now {computer_health} points left\n'))
    else:
        print(f'{computer_name} has blocked!\n')








