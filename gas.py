import requests
from telegram import Bot

# Telegram bot token and chat ID
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_TELEGRAM_CHAT_ID'

# Function to fetch gas prices from the Ethereum Gas Station API
def fetch_gas_prices():
    try:
        response = requests.get('https://ethgasstation.info/api/ethgasAPI.json')
        gas_prices = response.json()

        # Gas prices in Gwei
        fast = gas_prices['fast']
        fastest = gas_prices['fastest']
        safe_low = gas_prices['safeLow']
        average = gas_prices['average']

        # Compose the message
        message = f"Gas Prices (Gwei):\n\nFast: {fast}\nFastest: {fastest}\nSafe Low: {safe_low}\nAverage: {average}"

        # Send the message to Telegram
        send_telegram_message(message)
    except Exception as e:
        print('Error fetching gas prices:', str(e))

# Function to send a message to Telegram using the Telegram Bot API
def send_telegram_message(message):
    try:
        bot = Bot(token=bot_token)
        bot.send_message(chat_id=chat_id, text=message)
        print('Notification sent successfully')
    except Exception as e:
        print('Error sending notification:', str(e))

# Call the function to fetch gas prices and send a notification to Telegram
fetch_gas_prices()
