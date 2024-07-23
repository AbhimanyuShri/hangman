import turtle

word=['s','a','l','t','w','a','t','e','r']
newword=[]
wrong_guesses = 0

def draw_hangman(stage):
    turtle.clearscreen()
    turtle.speed(0)

    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(5)

    # Draw the base
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    t.forward(200)
    t.backward(100)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)

    if stage > 0:  # Head
        t.penup()
        t.goto(75, 70)
        t.pendown()
        t.circle(25)

    if stage > 1:  # Body
        t.penup()
        t.goto(100, 45)
        t.pendown()
        t.forward(80)

    if stage > 2:  # Left arm
        t.penup()
        t.goto(100, 45)
        t.pendown()
        t.right(45)
        t.forward(50)
        t.backward(50)

    if stage > 3:  # Right arm
        t.right(-90)
        t.forward(50)
        t.backward(50)
        t.left(45)

    if stage > 4:  # Left leg
        t.penup()
        t.goto(100,-35)
        t.pendown()
        t.left(225)
        t.forward(50)
        t.backward(50)
        t.right(45)
        
    if stage > 5:  # Right leg
        t.right(-135)
        t.forward(50)

    turtle.done()




def play_game():
    global wrong_guesses

    print("Welcome to the classic game of hangman!\nIn this game, you will choose letters which you think are in the secret word and if you guess correctly, you win, or else hangman loses a body part.")
    draw_hangman(6)
    
    while wrong_guesses < 6:
        user1 = input("Choose a letter: ").lower()
        if user1.isalpha() and len(user1) == 1:
            if user1 in word:
                if user1 not in newword:
                    print("That's a correct letter!")
                    newword.append(user1)
                else:
                    print("You already guessed that letter.")
                print("Current word:", ''.join([letter if letter in newword else '_' for letter in word]))
                if set(newword) >= set(word):
                    print("Congratulations, you guessed the word!")
                    break
            else:
                print("Unfortunately, that's not a letter in the word.")
                wrong_guesses += 1
                draw_hangman(wrong_guesses)
        else:
            print("Invalid input. Please enter a single letter.")

    if wrong_guesses == 6:
        print("Game over! The word was:", ''.join(word))

play_game()
screen.mainloop()






    
