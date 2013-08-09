# Optional format of the constructor for the OOP approach
class Player:
    def __init__(self):
        """
        Optional __init__ method is run once when your Player object is created before the
        game starts

        You can add other internal (instance) variables here at your discretion.

        You don't need to define food or reputation as instance variables, since the host
        will never use them. The host will keep track of your food and reputation for you
        as well, and return it through hunt_choices.
        """
        

    # All the other functions are the same as with the non object oriented setting (but they
    # should be instance methods so don't forget to add 'self' as an extra first argument).

    def hunt_choices(self, round_number, current_food, current_reputation, m, player_reputations):
        hunt_decisions = ['s' for x in player_reputations] # replace logic with your own
        hunt_goal= round(float(m/len(player_reputations)))
        if hunt_goal ==0:
            hunt_goal+=1
        hunts = self.find_equilibrium(hunt_goal, player_reputations)
        for i in hunts:
            hunt_decisions[i]='h'
        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass # do nothing

    def round_end(self, award, m, number_hunters):
        pass # do nothing
    def find_equilibrium(self, need, players_reputations):
        #searches for all players with rep closest to 50% and returns indecies
        hunts = []
        number_of_hunts = len(hunts); 
        maxim = 51; 
        minim = 49; 
        while number_of_hunts<need:
            try_range = range(minim,maxim,1)
            hunts = self.find_in_range(try_range, players_reputations)
            number_of_hunts = len(hunts);
            maxim = maxim+1
            minim= minim-1
        hunts.sort()
        return hunts[:int(need)]


    def find_in_range(self, defined_range, players_reputations):
        #finds indecies of array(players_reputation) that are in the desired_range
        array = [];
        for player in range(len(players_reputations)):
            if players_reputations[player] in defined_range:
                array.append(player)
        return array
