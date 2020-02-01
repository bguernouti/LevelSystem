import time
from Level_List import Level_List as lvls

""" Small Factrory Method Pattern"""
class Level:

    __Levels = lvls.ListOfLevels
    _Level = int
    _MaxScore = int
    _Score = int

    _MaxRank = 50

    def __init__(self,level,maxscore):

        self._Level = level
        self._MaxScore = maxscore
        self._Score = 0
        
    def getLevels(self):
        return self.__Levels

class LevelCreator:

    @staticmethod
    def Create(rank,maxscore):

        _level = Level

        if (rank <= _level._MaxRank):
            _level = Level(rank,maxscore)
        else: 
            _level = False

        return _level

"""level = LevelCreator.Create(rank=49,maxscore=1000)

while level._Score < level._MaxScore:
    level._Score += 100
    print(level._Score)
    time.sleep(1)

if level._Score >= level._MaxScore: 
    
    level = LevelCreator.Create(rank=level._Level +1,maxscore=2000)
    print(vars(level))"""