import  random 

top_range = input("type a  number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('plz type a number larger than 0 next time !')
        quit()
else:
    print('please type a number next time')
    quit()
random_no = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('plz enter a number ')
        continue

    if user_guess == random_no:
        print('you got it')
        break
    elif user_guess > random_no:
        print("you were above the number")
    else:
        print("you are below the number ")

print("you got number In " + str(guesses) + " of gusses")