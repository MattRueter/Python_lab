fav_colour = input("What is your favourite colour?")
computer_response="I also like the colour "+fav_colour
print(computer_response)

eat_fav_colour = input("Would you ever eat "+fav_colour+" if you could?")
if eat_fav_colour =='yes':
	computer_response = "Me too!"
	print(computer_response)
elif eat_fav_colour == 'no':
	computer_asks_question = input("Oh no.Why not?")
	answer = computer_asks_question
	computer_response ="Really? '"+answer+"' is your reason? Well I have had enough of you."
	print(computer_response)
	print("goodbye.")

