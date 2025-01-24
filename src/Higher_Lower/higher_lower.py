from higher_lower_logo import higher_lower, vs
import random
from game_data import data


score = 0;
right = True
visible1 = False
visible2 =False
temp1 = {}
temp2 = {}
first = {}
second = {}


while right:
    print(higher_lower)
    if temp1 == {} and temp2 == {}:
        first = random.choice(data)
        second = random.choice(data)
    if temp1 != {}:
        first = second
        second = temp1
        temp1 = {}
        temp2 = {}
    if temp2 != {}:
        second = temp2
        temp1 = {}
        temp2 = {}
    while first == second:
        second = random.choice(data)
    if visible1:
        print(f"You're right! Current score: {score}")
    if visible2:
        print(f"Sorry, that's wrong! Final score: {score}")
        break
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")

    print(vs)

    print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}. ")
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    if guess == 'a':
        if first['follower_count'] > second['follower_count']:
            visible1 = True
            right = True
            score+=1
            temp2 = random.choice(data)
            temp1 = {}

        else:
            visible1 = False
            visible2 = True
    if guess == 'b':
        if second['follower_count'] > first['follower_count']:
            visible1 = True
            right = True
            score+=1
            temp1 = random.choice(data)
            temp2 = {}

        else:
            visible1 = False
            visible2 = True