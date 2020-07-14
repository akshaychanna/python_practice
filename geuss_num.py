import pdb
import random
import sys


if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    # pdb.set_trace()
    number = random.randint(start,end)
    print(f"Game to guess number between {start} to {end}")

    guesses = 0
    while True:
        user_num = int(input("please guess a number between : "))
        if number != user_num:
            guesses += 1
            if user_num > number:
                print("wrong... please guess less number")
            else:
                print("wrong... please guess higher number")
        
        else:
            print(f"""Heyy dude congo your guess is right..
            and you took {guesses} guesses...
            """)
            break
