def inputAccount():
    valid_input = False
    while not valid_input:
        account = input("Select which account should be used\n\n1 - tim.wigton@wigtonco.com\n2 - tim@murcadom.com\n\n")
        if int(account) == 1:
            account = "tim.wigton@wigtonco.com"
            valid_input = True
        elif int(account) == 2:
                account = "tim@murcadom.com"
                valid_input = True
        else:
            print("invalid input")
    return account
