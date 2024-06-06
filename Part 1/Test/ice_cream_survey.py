from survey import Survey
question = "What is your favorito ice cream ?\n"
get_data = Survey(question)
get_data.print_question()
print("If you wanna quit the survey just type 'q' in the response")
while True:
    get_response = input('Ice-cream: ')
    if get_response == 'q' :
        break
    
        
    get_data.store_response(get_response)

get_data.show_result()