import random


name = "Matt"
if name == "":
	name = "Someone"

question = "Will it be nice out tomorrow?"
number = random.randint(1,5)
answer = ""

if question == "":
	answer ="You must ask a question"
elif number == 1:
	answer ="Most definitely!"
elif number == 2:
	answer = "Of course!"
elif number == 3:
	answer = "Not too certain of anything just now."
elif number == 4:
	answer = "No."
elif number == 5:
	answer = "Not exactly,well... no."
	
print(name + " asks: "+ question)
print("Magic Eight Ball says: " + answer)
