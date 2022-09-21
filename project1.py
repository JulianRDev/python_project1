#!/usr/bin/env python3
"""Anime suggestions | Julian Rosa
  Based on up to 5 user inputs, this code will suggest 5 new anime to watch using a while loop and conditionals"""
import random

def main():
    # welcome message to user
    print("Welcome, please enter 5 anime you have already watched and i shall suggest 5 new ones")

    # list to store all the given anime from user
    watched_anime = list()

    # set anime list for anime suggestions to give
    anime_list=['Demon Slayer', 'Naruto', 'Jujutsu Kaisen', 'Seven Deadly Sins', 'One Punch Man']

    #set anime input to empty string 
    anime_input = ""

    # Set counter to 0
    input_count = 0

    # sets up loop condition for 5 inputs and exits onces input count hits 5
    while input_count < 5:

        # increase input counter
        input_count += 1

        #generate random number for index
        random_num = random.randint(0,len(anime_list)-1)

        #input for anime from user
        anime_input=input("please enter a cool anime you have watched: ").title()

        #condition for if user does not enter anything
        if anime_input == "":
            anime_input=input("Well, I can't help you if you don't give me an anime. Please enter an anime: ").title()
        #condition for once counter hits 5, gives last suggestion and exits
        elif input_count == 5:
            print(f"Here's the last one for you : {anime_list[random_num]}!")
            print("That's all i got for you, FOR NOW!")
        # Condition if the input is already in the given anime_list
        elif anime_input in anime_list:
            print("Looks like you've got some good taste, I was going to suggest that!")
            #append input to users watched anime list
            watched_anime.append(anime_input)
            #removes the input from given anime list
            anime_list.remove(anime_input)
            # uses new randomizer due to removal
            random_num = random.randint(0,len(anime_list)-1)
            #variable for anime list element at random index so element can be removed after use
            random_anime = anime_list[random_num]
            print(f"you should check out {random_anime}!")
            anime_list.remove(random_anime)
        #condition if user inputs something they have already input 
        elif anime_input in watched_anime:
            anime_input = input("I know that is a good one but you can't put it in twice, please enter a different one :").title()
            #append input to users watched anime list
            watched_anime.append(anime_input)
            #variable for anime list element at random index so element can be removed after use
            random_anime = anime_list[random_num]
            print(f"Nice! thats a new one to me! Here's a new one for you : {random_anime}!")
            anime_list.remove(random_anime)
        #condition for an input by user that they have not done before and is not in given anime list
        elif anime_input not in watched_anime:
            print("I've never heard of that, Sounds cool! I'll keep that in mind.")
            #append input to users watched anime list
            watched_anime.append(anime_input)
            #variable for anime list element at random index so element can be removed after use
            random_anime = anime_list[random_num]
            print(f"Here's a new one for you : {random_anime}!")
            anime_list.remove(random_anime)
            
        
main()