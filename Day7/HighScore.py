import random


def Highscore():

    score = random.randint(1,101) 
    with open("Day7/HighScore.txt") as f:
        Highscore = f.read()
        if (Highscore != ""):
            Highscore = int(Highscore)
        else:
            Highscore = 0

    print(score)
    
    if score > Highscore:
        with open("Day7/HighScore.txt", "w") as f:
            f.write(str(score))


    return score

Highscore()