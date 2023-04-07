# P(B|A) = P(A,B)/P(A)
# P(A,B) Probability of both A and B occuring
# P(B|A) Probability of B given that A has occured

from numpy import random
random.seed(0) # Generates a seed value for random number generator.  Same random numbers every time

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0} # Python dictionaries
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0} # Python dictionaries
totalPurchases = 0
for _ in range(100000): # 100000 random people
    ageDecade = random.choice([20, 30, 40, 50, 60, 70]) # asigns random age decade
    # purchaseProbability = float(ageDecade) / 100.0 # based on age we create a purchase probability
    # What if Age had nothing to do with it
    purchaseProbability = .50 # based on age we create a purchase probability
    totals[ageDecade] += 1 # New random person 
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1 # attributes a person to this purchase
        # determines if they bought something based off their age range
print(totals)
print(purchases)
print(totalPurchases)

# Now we can play with conditional probability
PEF = float(purchases[30]) / float(totals[30]) # The probability of someone in their 30's buying something = percentage of how many 30-year-olds bought something
print('P(purchase | 30s): ' + str(PEF))

# P(F) is just the probability of being 30 in this data set:
PF = float(totals[30]) / 100000.0
print("P(30's): " +  str(PF))

# P(E) is the overall probability of buying something, regardless of your age0
PE = float(totalPurchases) / 100000.0
print("P(Purchase):" + str(PE))

print("P(30's)P(Purchase)" + str(PE * PF))

print("P(30's, Purchase)" + str(float(purchases[30]) / 100000.0))
#  P(E|F) = P(E,F)/P(F)
print((purchases[30] / 100000.0) / PF)