#Defining  the class named player
class player:
    def play(self):
        print("The player is playing cricket")


#deriving the Batsman,Bowler classes from player class
class Batsman(player):
    def play(self):
        print("The batsman is batting")


class Bowler(player):
    def play(self):
        print("The bowler is bowling")

#create instance for Batsman and Bowler class
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()