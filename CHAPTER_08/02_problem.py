import random

def game():
    print("You're playing the game: ")
    score = random.randint(1,99)

    with open("hi_score.txt" , "r")as f:
        hi_score = f.read()
        if (hi_score != ""):
            hi_score  = int(hi_score)
        else:
            hi_score = 0
        print(f"Your score {score}")  
        if (score > hi_score): 
            # Write this hi_score to file
         with open("hi_score.txt","w") as f:
             f.write(str(score))

             return score
game()