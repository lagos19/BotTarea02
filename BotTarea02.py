import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

FIRST = range(1)
UNO, DOS, TRES,CUATRO = range(4)


def start(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    logger.info("Usuario %s Ha iniciado conversacion", user.first_name)
    keyboard = [
        [

            InlineKeyboardButton("Consultar Tasa de Cambio del Dolar",
            callback_data=str(UNO)),
        ],
        [

            InlineKeyboardButton("Consultar Tasa de Cambio del Euro",
            callback_data=str(DOS)),
        ],
         [

            InlineKeyboardButton("Consultar Precio del Oro",
            callback_data=str(TRES)),
        ],
        [

            InlineKeyboardButton("Consultar Precio del Cafe",
            callback_data=str(TRES)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    user = update.effective_user
    update.message.reply_markdown_v2(
    fr'¡Hola {user.mention_markdown_v2()}\!, Por favor, Selecciona una opción',
    reply_markup=reply_markup)
    return FIRST

def uno(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'El valor del dolar en HN es 1USD=23HNL. Para mas informcion visite: g.co/finance/USD-HNL'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END
    

def dos(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'El Euro en HN es 1EUR=28HNL. Para mas informcion visite: g.co/finance/EUR-HNL'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END


def tres(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'El Precio del oro en HN es 1KG=1,409,987.60HNL. Para mas informcion visite: goldprice.org/es'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END

def cuatro(update: Update, context: CallbackContext) -> int:
    update.callback_query.answer()
    text = 'El Precio del café en HN es 1KG=3,37USD. Para mas informcion visite: cutt.ly/zmJZgsu'
    update.callback_query.edit_message_text(text=text)
    return ConversationHandler.END


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start para realizar otra consulta")
    
    

def main() -> None:
       
    updater = Updater("1906701890:AAE1V60meqDHUUDNtJSgsFR4ibb4x366ILE")
    
    dispatcher = updater.dispatcher
    updater.dispatcher.add_handler(CommandHandler('help', help))
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(uno, pattern='^' + str(UNO) + '$'),
                CallbackQueryHandler(dos, pattern='^' + str(DOS) + '$'),
                CallbackQueryHandler(tres, pattern='^' + str(TRES) + '$'),

            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    
    dispatcher.add_handler(conv_handler)

    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()