active = True
while active:
    get_user_input = input("WElcome to a simple addition CALC\nPress 'q' to exit\nEnter your first_number\n")
    get_user_input2 = input("Enter your second number\n")
    


    def addition(first_num,second_num):
        if first_num == 'q' or second_num == 'q' :
            active = False
            print("application closed!!")
        else:
            try:
                answer = int(first_num) + int(second_num)
                print(f"the sum is : {answer}")
            except ValueError:
                print("Please enter valid values\n")
        print(":><::><::><::><::><::><::><::><::><::><::><::><::><::><:")
    addition(get_user_input,get_user_input2)