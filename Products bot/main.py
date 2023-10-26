#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""This is a bot that can order product from the woocommerce store and receive payment from user."""
import os
import logging
import requests
from dotenv import load_dotenv
load_dotenv()
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}."
        
       
    )
from telegram import InputFile, LabeledPrice, ShippingOption, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


PROVIDER_TOKEN = os.getenv('CHAPA_TOKEN')
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    msg = (
        "Explore the premium store of yours /our_store"
    )

    await update.message.reply_text(msg)


async def start_with_shipping_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends an invoice with shipping-payment."""

    #product 1
    chat_id = update.message.chat_id
    title = "CeraVe - Renewing SA (Salicylic Acid) Facial Cleanser"
    description = "Indulge in luxurious skincare with Aveluxe's Renewing SA Cleanser. Infused with salicylic acid, this exclusive formula gently exfoliates, leaving your skin refreshed and renewed. Elevate your routine with the premium touch of Aveluxe."
    image_path = './I LOVE how CeraVe Renewing SA Cleanser makes my skin feel_ You will too_.jpeg'
    try:
        with open(image_path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo), caption=description)
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")

    # select a payload just for you to recognize its the donation from your bot
    payload = "15717"
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    currency = "ETB"
    # price in birr
    price = 65000
    # price * 100 so as to include 2 decimal points
    # check https://core.telegram.org/bots/payments#supported-currencies for more details
    prices = [LabeledPrice("Test", price * 100)]
    photo_url = 'https://aveluxecosmetics.com/wp-content/uploads/2023/10/I-LOVE-how-CeraVe-Renewing-SA-Cleanser-makes-my-skin-feel_-You-will-too_.jpeg'
    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    await context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        PROVIDER_TOKEN,
        currency,
        prices,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True,
        photo_url=photo_url,
    )

    #product 2
    chat_id = update.message.chat_id
    title = "Cetaphil - Renewing SA (Salicylic Acid) Facial Cleanser"
    description = "Indulge in luxurious skincare with Aveluxe's Renewing SA Cleanser. Infused with salicylic acid, this exclusive formula gently exfoliates, leaving your skin refreshed and renewed. Elevate your routine with the premium touch of Aveluxe."
    image_path = './I LOVE how CeraVe Renewing SA Cleanser makes my skin feel_ You will too_.jpeg'
    photo_url = 'https://aveluxecosmetics.com/wp-content/uploads/2023/10/I-LOVE-how-CeraVe-Renewing-SA-Cleanser-makes-my-skin-feel_-You-will-too_.jpeg'
    try:
        with open(image_path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo), caption=description)
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")

    # select a payload just for you to recognize its the donation from your bot
    payload = "15722"
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    currency = "ETB"
    # price in birr
    price = 5000
    # price * 100 so as to include 2 decimal points
    # check https://core.telegram.org/bots/payments#supported-currencies for more details
    prices = [LabeledPrice("Test", price * 100)]
    photo_url = 'https://aveluxecosmetics.com/wp-content/uploads/2023/10/I-LOVE-how-CeraVe-Renewing-SA-Cleanser-makes-my-skin-feel_-You-will-too_.jpeg'

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    await context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        PROVIDER_TOKEN,
        currency,
        prices,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True,
        photo_url=photo_url,
    )

    #product 3
    chat_id = update.message.chat_id
    title = "Cantu - Renewing SA (Salicylic Acid) Facial Cleanser"
    description = "Indulge in luxurious skincare with Aveluxe's Renewing SA Cleanser. Infused with salicylic acid, this exclusive formula gently exfoliates, leaving your skin refreshed and renewed. Elevate your routine with the premium touch of Aveluxe."
    image_path = './I LOVE how CeraVe Renewing SA Cleanser makes my skin feel_ You will too_.jpeg'
    photo_url = 'https://aveluxecosmetics.com/wp-content/uploads/2023/10/I-LOVE-how-CeraVe-Renewing-SA-Cleanser-makes-my-skin-feel_-You-will-too_.jpeg'
    try:
        with open(image_path, 'rb') as photo:
            context.bot.send_photo(chat_id=chat_id, photo=InputFile(photo), caption=description)
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")

    # select a payload just for you to recognize its the donation from your bot
    payload = "15727"
    product_id = payload
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    currency = "ETB"
    # price in birr
    price = 2130
    # price * 100 so as to include 2 decimal points
    # check https://core.telegram.org/bots/payments#supported-currencies for more details
    prices = [LabeledPrice("Test", price * 100)]
    photo_url = 'https://aveluxecosmetics.com/wp-content/uploads/2023/10/I-LOVE-how-CeraVe-Renewing-SA-Cleanser-makes-my-skin-feel_-You-will-too_.jpeg'

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    await context.bot.send_invoice(
        chat_id,
        title,
        description,
        payload,
        PROVIDER_TOKEN,
        currency,
        prices,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True,
        photo_url=photo_url,
    )

async def shipping_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Answers the ShippingQuery with ShippingOptions"""
    query = update.shipping_query
    # Common shipping options for all products
    common_shipping_options = [
        ShippingOption("1", "Free Delivery", [LabeledPrice("Free Delivery", 0*100)]),
    ]

    await query.answer(ok=True, shipping_options=common_shipping_options)

# A set of valid product IDs
valid_product_ids = {15717, 15722, 15727}  

# after (optional) shipping, it's the pre-checkout
async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Answers the PreQecheckoutQuery"""
    query = update.pre_checkout_query
    # Check if the product ID is in the set of valid product IDs
    product_id = int(query.invoice_payload)
    
    if product_id in valid_product_ids:
        await query.answer(ok=True)
    else:
        # Answer False pre_checkout_query
        await query.answer(ok=False, error_message="Invalid product ID. Contact customer support. Thanks for your patience!")


# finally, after contacting the payment provider...
async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirms the successful payment."""
    successful_payment_info = update.message.successful_payment
    if successful_payment_info:

        # Access payment information
        total_amount = successful_payment_info.total_amount
        currency = successful_payment_info.currency
        invoice_payload = successful_payment_info.invoice_payload

        #Access the user information
        user = update.message.from_user
        first_name = user.first_name
        last_name = user.last_name

        # Access shipping information
        shipping_address = successful_payment_info.order_info.shipping_address
        phone_number = successful_payment_info.order_info.phone_number
        email = successful_payment_info.order_info.email
        country = shipping_address.country_code
        city = shipping_address.city
        state = shipping_address.state
        postcode = shipping_address.post_code

        # Extract the product ID from the invoice_payload
        product_id = int(successful_payment_info.invoice_payload)

        # WooCommerce API credentials
        woocommerce_url = 'https://aveluxecosmetics.com/wp-json/wc/v3'
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')

        if product_id is not None:
            # WooCommerce API endpoint for creating orders
            orders_endpoint = f'{woocommerce_url}/orders'

            # Construct the order payload
            order_payload = {
                'payment_method': 'Chapa',
                'payment_method_title': 'Online Payment',
                'set_paid': True,
                'billing': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,  
                    'phone': phone_number,
                    'address': {
                        'country': country,
                        'city': city,
                        'state': state,
                        'postcode': postcode,
                        'street': shipping_address.street_line1,
                        'street2': shipping_address.street_line2,
                    },
                },
                'shipping': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'address': {
                        'country': country,
                        'city': city,
                        'state': state,
                        'postcode': postcode,
                        'street': shipping_address.street_line1,
                        'street2': shipping_address.street_line2,
                    },
                },
                'line_items': [
                    {
                        'product_id': product_id,
                        'quantity': 1,
                    },
                    # Add other products if necessary
                ],
            }

            # API request to create the order
            response = requests.post(orders_endpoint, json=order_payload, auth=(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET')))

            # Check the response
            if response.status_code == 201:
                print("Order placed successfully!")
                # Notify the user that the order was placed
                await update.message.reply_text("🌟 Payment Received Successfully! 🌟\n\nWhat's Next:\n\nSit back and relax! Our team is now preparing your order for a swift journey to your doorstep. Expect a shipping confirmation soon.\n\nAdditional Information:\n\n📧 You will receive a confirmation email shortly with all the details.\n☎️Our customer support team will give you a call to ensure a seamless experience.\n\nThank you for choosing Aveluxe. We appreciate your trust in our premium skincare and cosmetics.\n\nShould you have any questions, feel free to reach out to our support team.\n\nBest Regards,\nThe Aveluxe Team")
            else:
                print(f"Error placing order. Status code: {response.status_code}, Response: {response.json()}")
                # Notify the user about the error
                await update.message.reply_text("Sorry, there was an error processing your order. Please contact support.")
        else:
            print(f"Product ID not found for the ordered product: {product_id}")
            # Handle this case: notify the user or log the issue.
            await update.message.reply_text("Sorry, there was an error fetching the product ID of your products. Please contact support.")


        # Print information (DEBUGGING PURPOSE)
        print(f"product ID: {product_id}")
        print(f"Payment received! Amount: {total_amount} {currency}")
        print(f"Invoice Payload: {invoice_payload}")
        print(f"Phone Number: {phone_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Country: {country}")
        print(f"city: {city}")
        print(f"state: {state}")
        print(f"Postcode: {postcode}")
        print(f"Shipping Address Street 1: {shipping_address.street_line1}")
        print(f"Shipping Address Street 1: {shipping_address.street_line2}")

    else:
        print("No payment information found in the update.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # simple start function
    application.add_handler(CommandHandler("start", start_callback))

    # Add command handler to start the payment invoice
    application.add_handler(CommandHandler(
        "our_store", start_with_shipping_callback))

    # Optional handler if your product requires shipping
    application.add_handler(ShippingQueryHandler(shipping_callback))

    # Pre-checkout handler to final check
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))

    # Success! Notify your user!
    application.add_handler(
        MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback)
    )

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
