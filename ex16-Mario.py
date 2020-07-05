class Mario:
    lifecount = 3

    def __init__(self, character, score, timeelapsed, coins):
        self.character = character
        self.score = score
        self.timeelapsed = timeelapsed
        self.coins = coins

    def ifCrashed(self):
        self.__class__.lifecount -= 1

    def isLifeLeft(self):
        if self.__class__.lifecount <= 0:
            print("Game Over")

    def getCoins(self):
        self.coins += 1

    def showScore(self):
        print("Score : ", self.score)

    def showCharacter(self):
        print("Character : ", self.character)

    def timePlayed(self):
        print("Time Elapsed ", self.timeelapsed)


m1 = Mario("Morton", 155, "150s", 1500)
m1.showCharacter()
m1.showScore()
print(m1.lifecount)
m1.ifCrashed()
print(m1.lifecount)
