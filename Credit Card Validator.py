def validate_card(card_number):
    
    my_list = [str(x) for x in range(622126, 622926)]

    if len(str(card_number)) == 15 and int(str(card_number)[:2]) in [34,37]:

        print('American Express:')

        Luhn = []

        for index in range(len(str(card_number))):
            if index % 2 == 0:
                Luhn.append(int(str(card_number)[index]) * 2)

        sum_luhn = 0

        for num in Luhn:

            sum_luhn += num
        
        if sum_luhn % 10 == 0:

            return True
        
        else:

            return False
        
    elif len(str(card_number)) in list(range(12, 17)) and int(str(card_number)[0]) == 4:

        print("Visa:")

        Luhn = []

        for index in range(len(str(card_number))):
            if index % 2 == 0:
                Luhn.append(int(str(card_number)[index]) * 2)
            else:
                Luhn.append(int(str(card_number)[index]))

        sum_luhn = 0

        for num in Luhn:

            if len(str(num)) == 2:

                num1 = int(str(num)[0])
                num2 = int(str(num)[1])

                sum_luhn += num1 + num2

                continue

            sum_luhn += num

        if sum_luhn % 10 == 0:

            return True
        
        else:

            return False
        
    elif len(str(card_number)) == 16 and str(card_number)[:5] == '6011' or str(card_number)[:7] in my_list or int(str(card_number)[:4]) in [644, 645, 646, 647, 648, 649] or int(str(card_number)[:3]) == 65:
    
        print("Discover:")

        Luhn = []

        for index in range(len(str(card_number))):

            if index % 2 == 0:

                Luhn.append(int(str(card_number)[index]) * 2)

        sum_luhn = 0

        for num in Luhn:

            sum_luhn += num
        
        if sum_luhn % 10 == 0:

            return True
        
        else:

            return False



card_number = int(input("What's your card number: ").replace(" ", ""))

if validate_card(card_number):

    print("This card number is valid!")

else:

    print("This isn't a valid card number.")