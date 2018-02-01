import sys import random

ans = True while ans: question = input("Ask the magic 8 ball a question: (Press enter to quit) ")

answers = random.randint(1,8)

if question == "": sys.exit()

elif answers == 1: print ("Answer 1")

elif answers == 2: print ("Answer 2")

elif answers == 3: print ("Answer 3")

elif answers == 4: print ("Answer 4")

elif answers == 5: print ("Answer 5")

elif answers == 6: print ("Answer 6")

elif answers == 7: print ("Answer 7")

elif answers == 8: print ("Answer 8")
