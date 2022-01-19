class game():
    def __init__(self, starting_chips, denomination, shooter):
        self.players = []
        for i in range(4):
            self.players.append(Player(starting_chips))
        self.denomination = denomination
        self.shooter = shooter
        # how big you're playing in dollars. for example, if you're playing 10c/20c, denomination is 0.1(smallest denom)
        # currently does not support 3/6h.

    def calculate(self, tai, winner, shooter): #winner and shooter as in player number
        if (winner > 4 or winner <1) or (shooter > 4 or shooter < 1):
            raise PlayerError("No such player")
        l = [0,1,2,3]
        winner -= 1
        shooter -= 1
        l.remove(winner)
        l.remove(shooter)
        if self.shooter: #if we're playing shooter
            price = self.denomination * 4 * (2 ** (tai-1)) #price to pay
            self.players[winner].add(price)
            self.players[shooter].subtract(price)
        else:
            price1 = self.denomination * (2 ** (tai-1)) #non shooter pay, if not playing shooter
            price2 = self.denomination * 2 * (2 ** (tai-1)) #shooter's pay if playing shooter
            self.players[winner].add(2 * price2 + price1)
            self.players[shooter].subtract(price2)
            for i in l:
                self.players[i].chips.subtract(price1)
    
    def checkbalance(self):
        for i in self.players:
            print(f"Player {self.players.index(i)+1} Balance: {i.balance()}")
        return "Game continues."

class Player():
    def __init__(self, chips):
        if type(chips) != int:
            raise TypeError("Not Integer")
        self.chips = chips

    def subtract(self, amt):
        self.chips -= amt

    def add(self, amt):
        self.chips +=  amt

    def balance(self):
        return self.chips

class PlayerError():
    def __init__(self):
        pass

#Testing
_20_40 = game(200, 0.2, True)
_20_40.calculate(5, 1, 4)
print(_20_40.checkbalance())