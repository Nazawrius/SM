from random import randint

def guess_the_number():
    N = int(input("Enter the upper limit for number: "))
    n = randint(1, N)
    
    while (x := int(input("Enter your guess: "))) != n:
        if x > n:
            print("Smaller")
        else:
            print("Bigger")
    
    print("You guessed it!")

def rock_paper_scissors():
    moves = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    moves_reverse = {num:move for (move, num) in moves.items()}
    
    while (move := input("Enter your move: ")) != "exit":
        if move not in moves:
            print("Your move is incorrect!")
            continue
            
        human = moves[move]
        comp = randint(1, 3)
        print(f"Computer move was {moves_reverse[comp]},", end=" ")
        if human == comp:
            print("it's a draw!")
        elif human > comp or (human == 1 and comp == 3):
            print("you won!")
        else:
            print("you lost!")