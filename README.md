## Card Flow

This bot, built using Pyrogram, allows to generate cc's and check credit card information through commands.
It can generate random credit card numbers, validate them, and provide information about specific credit cards.

### Features
  - Generate Random Credit Cards
  - Check Credit Card Details
  - Generate Custom BIN Credit Cards

### Configure the bot:
  - Populate the necessary details in configs/tokens.py:
    ```py
      api_id = 'your_api_id'
      api_hash = 'your_api_hash'
      bot_token = 'your_bot_token'
    ```
  - Define the maximum number of cards to be generated and the bot name in configs/values.py:
    ```py
    max_cards = 10  # Maximum number of cards to generate
    bot_name = 'your_bot_name'
    ```
### Usage

  - /randomcc [count] : <br><br>
    generate a specified number of random, valid credit card numbers. If no count is provided, the bot defaults to generating one credit card number.
    The generated cards include the card number, expiration date, and CVV
      - Usage Example:<br>/randomcc or /randomcc 5
      - Output: <br>A list of generated credit card details formatted as<br> <code>{card_number}|{expiry_month}|{expiry_year}</code>.<br><br>
  - /checkcc <credit_card_number> : <br><br>
     provides detailed information about a specified credit card number.
     Users can input a credit card number, and the bot will return details such as the card type, brand, currency, issuing country, and bank name (if available)
      - Usage Example: <br>/checkcc 1234567890123456
      - Output: <br>Detailed information about the credit card including card type, card brand, currency, country, and bank name.<br><br>
  - /custombin <BIN> [count] : <br><br>
    generate valid credit card numbers using a specified BIN (Bank Identification Number).
    If no count is provided, the bot defaults to generating one credit card number.
    This is useful for testing and educational purposes where a specific BIN is required.
      - Usage Example:<br> /custombin 123456 or /custombin 123456 3
      - Output:<br> A list of generated credit card details formatted as<br> <code>{card_number}|{expiry_month}|{expiry_year}</code>.<br> Additionally, detailed information about one of the generated cards is provided, including card type, card brand, currency, country (with emoji), and bank name.<br><br>
Install Dependencies with pip
```
pip install -r requirements.txt
```

run the script with

```
python3 run.py
```
### Commands

  - /start: Verify that the bot is operational.<br>
        Example: /start

  - /randomcc [count]: Generate a specified number of random, valid credit card numbers. Defaults to 1 if no count is provided.<br>
        Example: /randomcc or /randomcc 5

  - /checkcc <credit_card_number>: Retrieve detailed information about a specified credit card number.<br>
        Example: /checkcc 1234567890123456

  - /custombin <BIN> [count]: Generate valid credit card numbers using a specified BIN (Bank Identification Number). Defaults to 1 if no count is provided.<br>
        Example: /custombin 123456 or /custombin 123456 3

### Note

```LICENSE
Card Flow is intended for educational purposes and should be used responsibly.
 Generating or using fake credit card numbers for fraudulent activities is illegal.
```
