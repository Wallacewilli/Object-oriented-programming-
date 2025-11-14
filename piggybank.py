coins = 100 
coins=100+500
print("i have",coins)

coin=-999
class piggybank:
    def __init__(self,coins):# safe doors(make it private use _ )see balancer use  getter() add is 
        #udates values use setter

        self._coins=coins
        self.put_in(coins)
    def put_in(self,amount ):
        if amount <=0:
            raise ValueError("add real money")
        self._coins += amount
        #method to take out 
        def take_out(self,amount):
            if amount<=0:
                raise ValueError("time wasting")
            if amount>self.coins:
                raise ValueError("money is coming")
            self._coins -=amount
        #how much to remove
        def how_much(self):
            return self._coins 

        
        
Goku=piggybank(100000)
Goku._coins=-100000
print("goku box has ",Goku.how_much(),)




        