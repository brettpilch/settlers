# Green Progress Card classes: blah

class RoadBuilding():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Road Building"
        self.description = "Build 2 roads for free anywhere adjacent to your existing structures."
        
    def execute(self, player):
        for i in range(2):
            player.do('r', "settlement")
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class Alchemist():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Alchemist"
        self.description = "Instead of rolling, choose the results of both numbered dice, then roll the event die as normal."
        
    def execute(self, player):
        print player.color, "is playing the Alchemist card."
        red = raw_input(player.color + ", enter a value for the red die (the event number): ")
        while not red.isdigit() or int(red) not in range(1,7):
            if not red: return
            print "Invalid entry. Must be an integer between 1 and 6."
            red = raw_input(player.color + ", enter a value for the red die (the event number): ")
        yellow = raw_input(player.color + ", enter a value for the yellow die: ")
        while not yellow.isdigit() or int(yellow) not in range(1,7):
            if not yellow: return
            print "Invalid entry. Must be an integer between 1 and 6."
            yellow = raw_input(player.color + ", enter a value for the yellow die: ")
        player.progress_cards.remove(self)
        progress[self.color].append(self)
        return red, yellow
            

class Crane():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Crane"
        self.description = "A city upgrade costs one less commodity."
        
    def execute(self, player):
        print player.color, "is attempting to play the crane card."
        outcome = player.do('u', 1)
        if outcome == "success":
            player.progress_cards.remove(self)
            progress[self.color].append(self)

class Engineer():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Engineer"
        self.description = "Build one city wall for free."
        
    def execute(self, player):
        print player.color, "is playing the Engineer card."
        outcome = player.do('w', 'engineer')
        if outcome == "success":
            player.progress_cards.remove(self)
            progress[self.color].append(self)

class Inventor():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Inventor"
        self.description = "Swap any 2 number tokens on the board. The numbers may not be 2, 6, 8, or 12."
        
    def execute(self, player):
        print player.color, "is playing the Inventor card."
        choice1 = raw_input("Enter the number of one of the hexes whose token you wish to swap: (0 - 18) ")
        hex_choice1 = [hexe for hexe in hexes if str(hexe.location) == choice1 and hexe.number in [3,4,5,9,10,11]]
        while len(hex_choice1) != 1:
            if not choice1: return
            print "Invalid entry. Please select a hexagon with a number token that is 3,4,5,9,10, or 11."
            choice1 = raw_input("Enter the number of one of the hexes whose token you wish to swap: (0 - 18) ")
            hex_choice1 = [hexe for hexe in hexes if str(hexe.location) == choice1 and hexe.number in [3,4,5,9,10,11]]
        choice2 = raw_input("Enter the number of the other hex whose token you wish to swap: (0 - 18) ")
        hex_choice2 = [hexe for hexe in hexes if str(hexe.location) == choice2 and hexe.number in [3,4,5,9,10,11] and hexe != hex_choice1[0]]
        while not hex_choice2:
            if not choice2: return
            print "Invalid entry. Please select a different hexagon with a number token that is 3,4,5,9,10, or 11."
            choice2 = raw_input("Enter the number of the other hex whose token you wish to swap: (0 - 18) ")
            hex_choice2 = [hexe for hexe in hexes if str(hexe.location) == choice2 and hexe.number in [3,4,5,9,10,11] and hexe != hex_choice1[0]]
        hex_choice1[0].number, hex_choice2[0].number = hex_choice2[0].number, hex_choice1[0].number
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class PlusTwo():
    def __init__(self, ID, resource):
        self.ID = ID
        self.color = "green"
        self.resource = resource
        if resource == "wheat": self.name = "Irrigation"
        else: self.name = "Mining"
        self.description = "Get 2 " + resource + " for each " + resource + " hex on which you have built a settlement or city."
        
    def execute(self, player):
        print player.color, "is playing the", self.name, "card..."
        added_amount = 2 * player.get_touching_hexes(self.resource)
        print player.color, "gains", added_amount, self.resource
        player.resources[self.resource] += added_resource
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class Medicine():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Medicine"
        self.description = "Build a city with 2 ore and 1 wheat."
        
    def execute(self, player):
        if player.resources["ore"] < 2 or player.resources["wheat"] < 1:
            print "You don't have the resources to play this card."
            return
        outcome = player.do('c', 'medicine')
        if outcome == "success":
            player.progress_cards.remove(self)
            progress[self.color].append(self)

class VictoryPoint():
    def __init__(self, ID, color):
        self.ID = ID
        self.color = color
        if color == "green": self.name = "Printer"
        else: self.name = "Constitution"
        self.description = "you got the " + self.name + "! It is played immediately for 1 free victory point!"
        
    def execute(self, player):
        print player.color + ", " + self.description
        player.victory_points += 1
        player.progress_cards.remove(self)

class Smith():
    def __init__(self, ID):
        self.ID = ID
        self.color = "green"
        self.name = "Smith"
        self.description = "Upgrade 2 of your knights for free. Rules about mighty knights still apply."
        
    def execute(self, player):
        print player.color, "is playing the Smith card."
        choices = [k[0] for k in player.knights_built if k[1] < 1 or (k[1] < 2 and player.technology["coin"] > 3)]
        choice1 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
        while not choice1.isdigit() or int(choice1) not in choices:
            if not choice1: return
            print "Invalid entry. Please choose from the options given."
            choice1 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
        outcome1 = player.upgrade_knight(int(choice1), "smith")
        if outcome1 != "success": return
        choices.remove(int(choice1))
        if not choices: print "You do not have any more upgradeable knights."
        else:
            choice2 = raw_input("Select another knight you wish to upgrade: " + str(choices) + " ")
            while not choice2.isdigit() or int(choice2) not in choices:
                if not choice2:
                    print "You have chosen not to upgrade the second knight."
                    break
                print "Invalid entry. Please choose from the options given."
                choice2 = raw_input("Select a knight you wish to upgrade: " + str(choices) + " ")
            if choice2: player.upgrade_knight(int(choice2), "smith")
        player.progress_cards.remove(self)
        progress[self.color].append(self)
        
    
# Blue Progress Card classes:

class Bishop():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Bishop"
        self.color = "blue"
        self.description = "Move the robber to any hex. Steal a card from each player occupying that hex."
        
    def execute(self, player):
        print player.color, "is playing the Bishop card."
        move_robber(player, "bishop")
        player.progress_cards.remove(self)
        progress[self.color].append(self)

class Deserter():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Deserter"
        self.color = "blue"
        self.description = "Choose an opponent. That player must remove one of his knights. You may then place a knight of equal strength."
        
    def execute(self, player):
        pass

class Diplomat():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Diplomat"
        self.color = "blue"
        self.description = "You may remove an open road. If it is your own road, you may place it somewhere else connected to you."
        
    def execute(self, player):
        pass

class Intrigue():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Intrigue"
        self.color = "blue"
        self.description = "You may displace an opponent's knight if it is touching your road."
        
    def execute(self, player):
        pass

class Saboteur():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Saboteur"
        self.color = "blue"
        self.description = "Each player who has as many or more victory points that you must discard half his had."
        
    def execute(self, player):
        pass

class Spy():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Spy"
        self.color = "blue"
        self.description = "Examine an opponent's hand of progress cards. You may choose one and add it to your hand."
        
    def execute(self, player):
        pass

class Warlord():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Warlord"
        self.color = "blue"
        self.description = "Activate all of your knights for free."
        
    def execute(self, player):
        print "Activating all of " + player.color + "'s knights."
        for knight in player.knights_built:
            knight[2] = 1
            knight[3] = 1

class Wedding():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Wedding"
        self.color = "blue"
        self.description = "Each player who has more victory points than you must give you two cards of his choice."
    def execute(self, player):
        pass

# Yellow Progress Card classes:

class CommercialHarbor():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Commercial Harbor"
        self.color = "yellow"
        self.description = "You may offer each player one resource in exchange for one commodity from his hand if he has any."
        
    def execute(self, player):
        pass

class MasterMerchant():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Master Merchant"
        self.color = "yellow"
        self.description = "Choose a player who has more victory points than you. You may examine his hand of resources and commodities and take 2."
        
    def execute(self, player):
        pass

class Merchant():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Merchant"
        self.color = "yellow"
        self.description = """Place the merchant on a hex adjacent to one of your settlements or cities.
You may trade that resource at the 2:1 rate for as long as you have the merchant. It is worth 1 victory point."""
        
    def execute(self, player):
        pass

class MerchantFleet():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Merchant Fleet"
        self.color = "yellow"
        self.description = "Choose any resource or commodity, which you may trade at the 2:1 rate for the rest of this turn."
        
    def execute(self, player):
        pass

class ResourceMonopoly():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Resource Monopoly"
        self.color = "yellow"
        self.description = "Choose a resource. Each player must give you 2 of that resource if they have any."
        
    def execute(self, player):
        pass

class TradeMonopoly():
    def __init__(self, ID):
        self.ID = ID
        self.name = "Trade Monopoly"
        self.color = "yellow"
        self.description = "Choose a commodity. Each player must give you 1 of that commodity if they have it."
        
    def execute(self, player):
        pass
        
