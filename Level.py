""" Small Factrory Pattern"""

class Level: 

    _Level = int
    _MaxScore = int
    _Score = int

    _MaxRank = 50

    def __init__(self,level,maxscore):

        self._Level = level
        self._MaxScore = maxscore
        self._Score = 0


class LevelCreator: 

    @staticmethod
    def Create(rank,maxscore):
        
        _level = Level

        if (rank < _level._MaxRank):
            _level = Level(rank,maxscore)
        else: 
            _level = False  
        return _level

level = LevelCreator.Create(rank=49,maxscore=1000)

print(vars(level))
#[print(attr) for attr in dir(level) if not attr.startswith("__")]