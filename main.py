from pyrogram import Client,filters
import random
from datetime import datetime, timedelta
import requests
from core.bincheck import bin_data_check
from configs.tokens import api_hash,api_id,bot_token,bin_checkurl
from core.isvalid import is_valid_credit_card
from core.expirydate import generate_date
from core.cvv import generatecvv
from core.validcc import generate_valid_cc
from configs.values import max_cards,bot_name
i=0
app = Client(bot_name,
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token)

@app.on_message(filters.command("start"))
def start_msg(client,message):
    print(message.text)
    await message.reply(f"Hello {message.from_user.first_name}!\n\n"
        "Welcome to **Card Flow** 🪪\n\n"
        "Here are some commands to get you started:\n\n"
        "🔹 **Generate Random Credit Cards**:\n"
        "   `/randomcc [count]` - Generate a specified number of random, valid credit card numbers. Defaults to 1 if no count is provided.\n\n"
        "🔹 **Check Credit Card Details**:\n"
        "   `/checkcc <credit_card_number>` - Retrieve detailed information about a specified credit card number.\n\n"
        "🔹 **Generate Custom BIN Credit Cards**:\n"
        "   `/custombin <BIN> [count]` - Generate valid credit card numbers using a specified BIN."
    )
@app.on_message(filters.command("randomcc"))   
async def cc_gen(client,message):
    bin_string = str(message.text).replace("/randomcc","")
    i=1
    print(bin_string)
    if bin_string == "":
        loop_value = 1
    else:
        loop_value = int(bin_string)
    card_number_list = ""
    while i<=loop_value:
        is_valid_card = generate_valid_cc(bin_number=None)
        if is_valid_card != False:
            valid_card = is_valid_card
            cvv = generatecvv()
            random_date = generate_date()
            print(f"```{valid_card}|{random_date.strftime('%m')}|{random_date.strftime('%Y')}```")
            print(len(str(valid_card)))
            card_number_list += str(f"<code>{valid_card}|{random_date.strftime('%m')}|{random_date.strftime('%Y')}</code>\n")
            i+=1
            
    response = bin_data_check(valid_card,bin_checkurl)
    try:
        card_type = response.get("type")
        card_brand = response.get("scheme")
        currency = response.get("country").get("currency")
        country = response.get("country").get("name")
        emoji = response.get("country").get("emoji")
        print(currency)
        if response.get("bank").get("name") != None:
            bank_name = response.get("bank").get("name")
            print(bank_name)
    except Exception as e:
        print(e)
    await message.reply(f"**__Here's your CC 🪪__**\n\n**Card Type** : <code>{card_type}</code>\n**Card Brand** : <code>{card_brand}</code>\n**Currency** : <code>{currency}</code>\n**Country** : <code>{emoji}{country}</code>\n\n{card_number_list}")
@app.on_message(filters.command("checkcc"))     
async def checkcc(client,message):
    checkcc_string = str(message.text).replace("/checkcc","").replace(" ","")
    response = bin_data_check(checkcc_string,bin_checkurl)
    try:
        card_type = response.get("type")
        card_brand = response.get("scheme")
        currency = response.get("country").get("currency")
        country = response.get("country").get("name")
        emoji = response.get("country").get("emoji")
        print(currency)
        if response.get("bank").get("name") != None:
            bank_name = response.get("bank").get("name")
            print(bank_name)
        await message.reply(f"**__Here's your CC Details 🪪__**\n\n**Card Type** : <code>{card_type}</code>\n**Card Brand** : <code>{card_brand}</code>\n**Currency** : <code>{currency}</code>\n**Country** : <code>{emoji}{country}</code>")
    except Exception as e:
        print(e)
        
@app.on_message(filters.command("custombin"))   
async def cc_gen(client,message):
    bin_string = str(message.text).replace("/custombin","").replace(" ","")
    i=1
    print(bin_string)
    if bin_string == "":
        loop_value = 1
    else:
        loop_value = int(bin_string)
    card_number_list = ""
    if loop_value > max_cards:
        loop_value = max_cards
    while i<=loop_value:
        is_valid_card = generate_valid_cc(bin_number=int(bin_string))
        if is_valid_card != False:
            valid_card = is_valid_card
            cvv = generatecvv()
            random_date = generate_date()
            print(f"```{valid_card}|{random_date.strftime('%m')}|{random_date.strftime('%Y')}```")
            print(len(str(valid_card)))
            card_number_list += str(f"<code>{valid_card}|{random_date.strftime('%m')}|{random_date.strftime('%Y')}</code>\n")
            i+=1
            
    response = bin_data_check(valid_card,bin_checkurl)
    try:
        card_type = response.get("type")
        card_brand = response.get("scheme")
        currency = response.get("country").get("currency")
        country = response.get("country").get("name")
        emoji = response.get("country").get("emoji")
        print(currency)
        if response.get("bank").get("name") != None:
            bank_name = response.get("bank").get("name")
            print(bank_name)
    except Exception as e:
        print(e)
    await message.reply(f"**__Here's your CC 🪪__**\n\n**Card Type** : <code>{card_type}</code>\n**Card Brand** : <code>{card_brand}</code>\n**Currency** : <code>{currency}</code>\n**Country** : <code>{emoji}{country}</code>\n\n{card_number_list}")
app.run()
