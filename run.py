
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
# Encoding that will store all of your constraints
E = Encoding()

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
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
a = BasicPropositions("a")
b = BasicPropositions("b")   
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()





##### WHAT WE ARE WORKING ON (STILL NEED TO BE IMPLEMENTED TO THE ACTUAL CODE ABOVE)#######

# Randomly generate 8 champions can be done with regular python code, no predicate logic needed
# Only models singleplayer aspect, the player will get 8 champions and there are 4 champions for the player to choose frome
# which champion of the 4 is the best choice?


# no constraints added yet
team = ["A", "A", "A", "B", "B", "B", "C", "D"] # 8 random champs for player’s team
options = ["A", "B", "C", "F"] # 4 random options for player to choose from
optionsArrays = []

# boolean arrays to represent the quantity of each champion in team
# when xQuantity[0] is True, that means it is true that there is at least 0 of that champion team
# when xQuantity[1] is True, it is true that there is at least 1 of that champion in team, etc
aQuantity = [True, True, True, True , False, False, False]
bQuantity = [True, True, True, True, False, False, False]
cQuantity = [True, True, False, False, False, False, False]
dQuantity = [True, True, False, False, False, False, False]
eQuantity = [True, False, False, False, False, False, False]
fQuantity = [True, False, False, False, False, False, False]
gQuantity = [True, False, False, False, False, False, False]
hQuantity = [True, False, False, False, False, False, False]
jQuantity = [True, False, False, False, False, False, False]	

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
	options.Arrays.append(["D", dQuantity])
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
# respectively)
# checks in order of highest to lowest champion since optionsArray is already in that order
for i in range(5, 0, -2):
    for j in range(len(optionsArrays)):
	    if optionsArrays[j][1][i]:
		    optionsArrays[j][1][i + 1] = True
		    break

# since the available champions are listed in order from highest to lowest, add the next highest
# single by adding the first available champion
for i in range(7):
    if not optionsArrays[0][1][i]:
	    optionsArrays[0][1][i] = True
	    break
