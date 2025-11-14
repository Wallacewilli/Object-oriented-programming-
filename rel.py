class r:
    def __init__(self,partner):
        self.partner = partner
        self._trust = 50
        self._mood="happy"
        self._vibe=100
    def build_trust(self,amount):
        if amount < 0:
            raise ValueError("run away")
        self.__trust =+ amount
    def break_tust(self,amount):
        if amount <= 0:
            raise ValueError("i dont want ")
        self._trust -= amount
    def talk(self,duration):
        if duration <= 0:
            raise ValueError ("dont wast time ")
        self._vibe +=duration
        self._trust +=5
        self.mood="good"
netflix=r("chill")
netflix.build_trust(20)




    
        