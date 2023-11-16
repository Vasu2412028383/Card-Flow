import requests
def bin_data_check(card_number,bin_checkurl):
    
    response = requests.post(bin_checkurl+str(card_number)).json()
    return response