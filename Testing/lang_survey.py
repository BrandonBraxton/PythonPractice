from survey import AnonSurvey

# define question

question = "What language do you speak?"
my_suvery = AnonSurvey(question)

my_suvery.show_question()
print("Enter 'q' to quit. ")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_suvery.store_response(response)

print("\nThank you for participating!")
my_suvery.show_results()

