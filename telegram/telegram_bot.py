#TOKEN = "6142960419:AAEU9BzyWThxQXHDAQQAaVUEEfxdLLF85ew"
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
)

TOKEN = "6142960419:AAEU9BzyWThxQXHDAQQAaVUEEfxdLLF85ew"

RATE = 2.5

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

CHOOSE_CURRENCY, ENTER_AMOUNT = range(2)

def start(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    welcome_message = "Привет"

    keyboard = [
        [
            InlineKeyboardButton("Меню", callback_data="menu"),
            InlineKeyboardButton("Наш канал", url="https://t.me/by_onlyone"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    _.bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=reply_markup)

def menu_callback(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query

    query.answer()

    thailand_message = "Таиланд 🇹🇭"

    keyboard = [
        [
            InlineKeyboardButton("Обмен валюты", callback_data="currency_exchange"),
            InlineKeyboardButton("Скидываемся на опт", url="https://t.me/weedhustla"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    _.bot.send_message(chat_id=chat_id, text=thailand_message, reply_markup=reply_markup)

def currency_exchange_callback(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query

    query.answer()

    exchange_rate_message = f"Курс: {RATE}"

    keyboard = [
        [
            InlineKeyboardButton("Рассчитать", callback_data="calculate_currency"),
            InlineKeyboardButton("Обменять", url="https://t.me/og_dudee"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    _.bot.send_message(chat_id=chat_id, text=exchange_rate_message, reply_markup=reply_markup)

def calculate_currency_callback(update: Update, _: CallbackContext) -> int:
    chat_id = update.effective_chat.id
    query = update.callback_query

    query.answer()

    choose_currency_message = "Выбери валюту"

    keyboard = [
        [
            InlineKeyboardButton("RUB", callback_data="RUB"),
            InlineKeyboardButton("THB", callback_data="THB"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    _.bot.send_message(chat_id=chat_id, text=choose_currency_message, reply_markup=reply_markup)

    return CHOOSE_CURRENCY

def choose_currency(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    context.user_data['currency'] = query.data

    if query.data == "RUB":
        message = "Сколько рублей нужно разменять?"
    else:
        message = "Сколько бат нужно получить?"

    query.edit_message_text(text=message, reply_markup=ForceReply())

    return ENTER_AMOUNT

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(menu_callback))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()