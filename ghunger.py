
# HG Player
class NfgpPlayer:
    numRounds = None
    prevRoundFood = None
    prevRoundAvgRep = None
    prevRoundNumPlayers = None

    currRoundFood = None
    currRoundAvgRep = None
    currRoundNumPlayers = None    
    def __init__(self):
        pass

    def hunt_choices(self, round_number, current_food, current_reputation, m,
            player_reputations):
        """
        LOGIC:
        A well-balanced algorithm will also consider a few secondary factors when making a choice:
        1) Number of players that died in the previous round
        2) Average reputation of players in current round (including self?)
        3) Change in food supply
        4) Potential food use in current round (Worst case would these choices kill me?)
      
        """
        # Update player "memory"
        self.numRounds = round_number
        self.prevRoundFood = self.currRoundFood
        self.prevRoundAvgRep = self.currRoundAvgRep
        self.prevRoundNumPlayers = self.currRoundNumPlayers
        
        
        self.currRoundFood = current_food
        self.currRoundNumPlayers = len(player_reputations)
        # The expected value that any opponent will Hunt
        self.currRoundAvgRep = (sum(player_reputations) + current_reputation) / (self.currRoundNumPlayers + 1)
        
    # The main routine that plays each individual round.

    # You must create an array of variables 'hunt_decisions' and assign an 'h' for hunt or
    # an 's' for slack (i.e., not hunt) to each member of the array; the order of the hunt
    # decisions in hunt_decisions should correspond to the order of opponents'
    # reputations in player_reputations.

    # Blank variables or errors will be assigned 's'.

    # The variables passed in to hunt_choices for your use are:
    #     round_number: integer, the number round you are in.
    #     current_food: integer, the amount of food you have.
    #     current_reputation: float (python's representation of real numbers), your current reputation.
    #     m: integer, the threshold cooperation/hunting value for this round.
    #     player_reputations: list of floats, the reputations of all the remaining players in the game.
    #                         The ordinal positions of players in this list will be randomized each round.

        huntDecisions = []
        huntConsequences = 0
        for player in player_reputations:
            if player >= self.currRoundAvgRep: # If the player has a higher-than average reputation to hunt, opt to cooperate
                huntDecisions.append('h')
            else: # If not, slack
                huntDecisions.append('s')
                
        # Analyze worst-case food cost of current hunt decisions
        # If it is greater than the current food supply, then slack as much as possible to avoid worst-case death
        while self.findWorstCaseHunt(huntDecisions) >= self.currRoundFood:
            try:
                i = huntDecisions.index('h')
                huntDecisions[i] = 's'
            except ValueError: # All "Hunt" choices are gone
                break
            
        return huntDecisions

    def hunt_outcomes(self, food_earnings):
    # hunt_outcomes is called after all hunts for the round are complete.

    # The variable passed in to hunt_outcomes for your use is:
    #     food_earnings: list of integers, the amount of food earned from the last round's hunts.
    #                    The entries can be negative as it is possible to lose food from a hunt.
    #                    The amount of food you have for the next round will be current_food
    #                    + sum of all entries of food_earnings + award from round_end.
    #                    The list will be in the same order as the decisions you made in that round.

    """
    LOGIC:
    Based on the value of the entry, we can tell whether we were taken advantage of by another player.
    This can inform whether or not to hunt/slack more in the next round.
    
    U/T
    H/H = -6 + 12/2 = 0 (Both cooperated => BC)
    H/S = -6 + 6/2 = -3 (Taken advantage of => TO)
    S/H = -2 + 6/2 =  1 (Took advantage => TA)
    S/S = -2 + 0 =   -2 (No cooperation => NC)
    
    Thoughts:
    NC and BC are fairly neutral, and maybe shouldn't be consideres as much as TA and TO
    Possibly compare the hunt results to hunt consequences calculated earlier
    
    """
        bc = 0
        to = 0
        ta = 0
        nc = 0
        
        for outcome in food_earnings:
            if outcome == 0:
                bc += 1
            if outcome == -3:
                to += 1
            if outcome == 1:
                ta += 1
            if outcome == -2:
                nc += 1 

    def round_end(self, award, m, number_hunters):
    # round_end is called after all hunts for the round are complete.

    # award - the total amount of food you received due to cooperation in the round.
    # Can be zero if the threshold m was not reached.

    # Add any code you wish to modify your variables based on the cooperation that occurred in
    # the last round.

    # The variables passed in to round_end for your use are:
    #     award: integer, total food bonus (can be zero) you received due to players cooperating
    #            during the last round. The amount of food you have for the next round will be
    #            current_food (including food_earnings from hunt_outcomes this round) + award.
    #     number_hunters: integer, number of times players chose to hunt in the last round.


        pass # do nothing
    
    def findWorstCaseHunt(self, hunt_decisions)
        huntConsequences = 0
        for choice in hunt_decisions:
            if choice == 'h': # If the player has a higher-than average reputation to hunt, opt to cooperate
                huntConsequences += 3
            else: # choice == 's'
                huntConsequences += 2
        return huntConsequences
