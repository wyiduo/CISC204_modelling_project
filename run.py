from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import random
E = Encoding()
# three arrays to store information
team = []
options = []
optionsArrays = []
# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# different types of champions that exist
types = ["A","B","C","D","E","F","G","H","J"]

# number of champions allowed on the board
num_champion = 9

# number of champions given on the board
num_champion_given = 8

# number of options player can choose from
num_option = 4

# number of a type of champions on board
a1 = BasicPropositions("A_1")
a2 = BasicPropositions("A_2")
a3 = BasicPropositions("A_3")
a4 = BasicPropositions("A_4")
a5 = BasicPropositions("A_5")
a6 = BasicPropositions("A_6")
b1 = BasicPropositions("B_1")
b2 = BasicPropositions("B_2")
b3 = BasicPropositions("B_3")
b4 = BasicPropositions("B_4")
b5 = BasicPropositions("B_5")
b6 = BasicPropositions("B_6")  
c1 = BasicPropositions("C_1")
c2 = BasicPropositions("C_2")
c3 = BasicPropositions("C_3")
c4 = BasicPropositions("C_4")
c5 = BasicPropositions("C_5")
c6 = BasicPropositions("C_6")
d1 = BasicPropositions("D_1")
d2 = BasicPropositions("D_2")
d3 = BasicPropositions("D_3")
d4 = BasicPropositions("D_4")
d5 = BasicPropositions("D_5")
d6 = BasicPropositions("D_6")
e1 = BasicPropositions("E_1")
e2 = BasicPropositions("E_2")
e3 = BasicPropositions("E_3")
e4 = BasicPropositions("E_4")
e5 = BasicPropositions("E_5")
e6 = BasicPropositions("E_6")
f1 = BasicPropositions("F_1")
f2 = BasicPropositions("F_2")
f3 = BasicPropositions("F_3")
f4 = BasicPropositions("F_4")
f5 = BasicPropositions("F_5")
f6 = BasicPropositions("F_6")
g1 = BasicPropositions("G_1")
g2 = BasicPropositions("G_2")
g3 = BasicPropositions("G_3")
g4 = BasicPropositions("G_4")
g5 = BasicPropositions("G_5")
g6 = BasicPropositions("G_6")
h1 = BasicPropositions("H_1")
h2 = BasicPropositions("H_2")
h3 = BasicPropositions("H_3")
h4 = BasicPropositions("H_4")
h5 = BasicPropositions("H_5")
h6 = BasicPropositions("H_6")
j1 = BasicPropositions("J_1")
j2 = BasicPropositions("J_2")
j3 = BasicPropositions("J_3")
j4 = BasicPropositions("J_4")
j5 = BasicPropositions("J_5")
j6 = BasicPropositions("J_6")

#True when there are some of that class of champion on board
#n ranges from 1 to 6
a = BasicPropositions("A_n")
b = BasicPropositions("B_n")
c = BasicPropositions("C_n")
d = BasicPropositions("D_n")
e = BasicPropositions("E_n")
f = BasicPropositions("F_n")
g = BasicPropositions("G_n")
h = BasicPropositions("H_n")
j = BasicPropositions("J_n")

# True when the champion is able to be brought from the choices
a_b = BasicPropositions("A")
b_b = BasicPropositions("B")
c_b = BasicPropositions("C")
d_b = BasicPropositions("D")
e_b = BasicPropositions("E")
f_b = BasicPropositions("F")
g_b = BasicPropositions("G")
h_b = BasicPropositions("H")
j_b = BasicPropositions("J")


# boolean arrays to represent the quantity of each champion in team
# when xQuantity[0] is True, that means it is true that there is at least 0 of that champion team
# when xQuantity[1] is True, it is true that there is at least 1 of that champion in team, etc
aQuantity = [True, False, False, False, False, False, False]
bQuantity = [True, False, False, False, False, False, False]
cQuantity = [True, False, False, False, False, False, False]
dQuantity = [True, False, False, False, False, False, False]
eQuantity = [True, False, False, False, False, False, False]
fQuantity = [True, False, False, False, False, False, False]
gQuantity = [True, False, False, False, False, False, False]
hQuantity = [True, False, False, False, False, False, False]
jQuantity = [True, False, False, False, False, False, False] 


# Randomly generate 8 champions can be done with regular python code, no predicate logic needed
# Only models singleplayer aspect, the player will get 8 champions and there are 4 champions for the player to choose frome
# which champion of the 4 is the best choice?


# return a champion class according to a given number
def assign_letter_number(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "B"
    elif num == 2:
        return "C"
    elif num == 3:
        return "D"
    elif num == 4:
        return "E"
    elif num == 5:
        return "F"
    elif num == 6:
        return "G"
    elif num == 7:
        return "H"
    elif num == 8:
        return "J"

# update the truth values in all the propositions arrays 
# arr = [False, False, False, False, False, False, False, False]

def update_proposition(arr):
    for i in range(7):
        if arr[i] == False:
            arr[i] = True
            return

# set up the game
def set_game():


  # assign 8 random champions to be already in the player's comp
    for i in range(8):
        number = random.randint(0, 8)
        team.append(assign_letter_number(number))

  # update the truth values in all the propositions arrays
    for i in range(8):
        if team[i] == "A":
            update_proposition(aQuantity)
        elif team[i] == "B":
            update_proposition(bQuantity)
        elif team[i] == "C":
            update_proposition(cQuantity)
        elif team[i] == "D":
            update_proposition(dQuantity)
        elif team[i] == "E":
            update_proposition(eQuantity)
        elif team[i] == "F":
            update_proposition(fQuantity)
        elif team[i] == "G":
            update_proposition(gQuantity)
        elif team[i] == "H":
            update_proposition(hQuantity)
        else:
            update_proposition(jQuantity)

    # find 4 random champions to be the options the player can choose from
    for i in range(4):
        number = random.randint(0, 8)
        options.append(assign_letter_number(number))

  # Check which champions are in options, and add the champ and its respective list to
  # optionsArray.
  # Ensures that the champions are placed in order from highest to lowest value
    if "A" in options:
        optionsArrays.append(["A", aQuantity])
    if "B" in options:
        optionsArrays.append(["B", bQuantity])
    if "C" in options:
        optionsArrays.append(["C", cQuantity])
    if "D" in options:
        optionsArrays.append(["D", dQuantity])
    if "E" in options:
        optionsArrays.append(["E", eQuantity])
    if "F" in options:
        optionsArrays.append(["F", fQuantity])
    if "G" in options:
        optionsArrays.append(["G", gQuantity])
    if "H" in options:
        optionsArrays.append(["H", hQuantity])
    if "J" in options:
        optionsArrays.append(["J", jQuantity])

# if a champion is in optionsArrays, that means at least one of that champion is available.
# look for groups of 5, 3, or 1 (in which case adding 1 would make groups of 6, 4, or 2
# respectively, which is what we want)
# checks in order of highest to lowest champion since optionsArray is already in that order
# Returns True if successful (a group has been found and added to), False otherwise
def find_highest_even_group():
    for i in range(5, 0, -2):
        for j in range(len(optionsArrays)):
            if optionsArrays[j][1][i]:
                optionsArrays[j][1][i + 1] = True
                team.append(optionsArrays[j][0])
                return True
    return False

# since the available champions are listed in order from highest to lowest, add the next highest
# single by adding the first available champion.
# Returns True if successful (the highest single has been added to the team), False otherwise
def find_highest_single():
    for i in range(7):
        highest = optionsArrays[0][1]
        if not highest[i]:
            highest[i] = True
            team.append(optionsArrays[0][0])
            return True
    return False


# still need to add more constraints
def optimal_team_comp():
    set_game()

    #specific class that can't be chosen from the option if 2 specific classes exist on board 
    E.add_constraint(a & b >> ~c_b)
    E.add_constraint(a & c >> ~b_b)
    E.add_constraint(b & c >> ~a_b)
    E.add_constraint(d & e >> ~f_b)
    E.add_constraint(d & f >> ~e_b)
    E.add_constraint(e & f >> ~d_b)
    E.add_constraint(g & h >> ~j_b)
    E.add_constraint(g & j >> ~h_b)
    E.add_constraint(h & j >> ~g_b)

    #prioritizing 6,4,2 than hierachy of class
    E.add_constraint(a3 & b5, a_b & b_b >> b_b)
    E.add_constraint(c2 & d1, c_b & d_b >> d_d)

 
    # can't have more than 6 of the same type of champion on board
    E.add_constraint(a6 >> ~a_b)
    E.add_constraint(b6 >> ~b_b)
    E.add_constraint(c6 >> ~c_b)
    E.add_constraint(d6 >> ~d_b)
    E.add_constraint(e6 >> ~e_b)
    E.add_constraint(f6 >> ~f_b)
    E.add_constraint(g6 >> ~g_b)
    E.add_constraint(h6 >> ~h_b)
    E.add_constraint(j6 >> ~j_b)

  
    #hierachy A to J
    E.add_constraint(a_b & b_b & c_b & d_b >> a_b)
    E.add_constraint(a_b & c_b & d_b & e_b >> a_b)
    E.add_constraint(a_b & d_b & e_b & f_b >> a_b)
    E.add_constraint(a_b & e_b & f_b & g_b >> a_b)
    E.add_constraint(a_b & f_b & g_b & h_b >> a_b)
    E.add_constraint(a_b & g_b & h_b & j_b >> a_b)
    E.add_constraint(a_b & h_b & j_b >> a_b)
    E.add_constraint(a_b & j_b >> a_b)
    E.add_constraint(b_b & c_b & d_b & e_b >> b_b)
    E.add_constraint(b_b & d_b & e_b & f_b >> b_b)
    E.add_constraint(b_b & e_b & f_b & g_b >> b_b)
    E.add_constraint(b_b & f_b & g_b & h_b >> a_b)
    E.add_constraint(b_b & g_b & h_b & j_b >> a_b)
    E.add_constraint(b_b & h_b & j_b >> b_b)
    E.add_constraint(b_b & j_b >> b_b)
    E.add_constraint(c_b & d_b & e_b & f_b >> c_b)
    E.add_constraint(c_b & e_b & f_b & g_b >> c_b)
    E.add_constraint(c_b & f_b & g_b & h_b >> a_b)
    E.add_constraint(c_b & g_b & h_b & j_b >> a_b)
    E.add_constraint(c_b & h_b & j_b >> c_b)
    E.add_constraint(c_b & c_b >> a_b)
    E.add_constraint(d_b & e_b & f_b & g_b >> d_b)
    E.add_constraint(d_b & h_b & j_b >> d_b)
    E.add_constraint(d_b & j_b >> d_b)
    E.add_constraint(e_b & h_b & j_b >> d_b)
    E.add_constraint(e_b & j_b >> d_b)


    return E

# template provided by prof
if __name__ == "__main__":
    # finds the optimal team comp for the given board
    T = optimal_team_comp()
    T = T.compile()
    solution = T.solve()
    # out puts the results
    print("Your team: " + team)
    print("Your options: " + options)
    print("Best choice: " + solution)
