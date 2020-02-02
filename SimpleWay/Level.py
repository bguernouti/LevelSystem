import time
from Levels_Setup import Level_List

class Level:

    def __repr__(self):
        return "%s : %s MAX = %s" % (self._Level, self._Score, self._MaxScore)

    def __init__(self):
        self.__List = Level_List._Levels
        self._Level = 1
        self.getLevelScore(self._Level)

    def UpdateLevel(self):

        if self._Score <= self._MaxScore:
            return

        self._Level += 1
        if self._Level > len(self.__List):
            self._Score = self._MaxScore
            return
        
        self.getLevelScore(self._Level)

    def getLevelScore(self,self_level):
        self._MaxScore = self.__List.get(self_level)
        self._Score = 0

    def UpdateScore(self,given_score):
        self._Score += given_score

        if self._Score > self._MaxScore: 
            self.UpdateLevel()

    def setLevel(self,rank):
        self._Level = rank
        self.getLevelScore(self._Level)

MyLevel = Level()
MyLevel.setLevel(9)

GameScoreSetp = 500

while True:
    MyLevel.UpdateScore(GameScoreSetp)
    print(MyLevel)
    time.sleep(1)