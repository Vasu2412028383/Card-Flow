def generate_valid_cc(bin_number):
    if bin_number == None:
        bin_number = 380000
    generated_num = random.randint(1e9, (1e10)-1)
    card_number = str(bin_number)+str(generated_num)
    valid_card_number = is_valid_credit_card(int(card_number))
    if valid_card_number == True:
        return card_number
    else:
        return False