import EzTG


def callback(bot, update):
    # here's your bot
    if 'message' in update:
        # messages "handler"
        message_id = update['message']['message_id']  # https://core.telegram.org/bots/api#message
        user_id = update['message']['from']['id']
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            bot.sendMessage(chat_id=chat_id, text='Benvenuto in questo bot' %
                            (user_id, chat_id, message_id))  # you can find method parameters in https://core.telegram.org/bots/api#sendmessage

        if text == '/inline':
            keyboard = EzTG.Keyboard('inline')
            keyboard.add('Example', 'callback data')
            keyboard.add('Example 2', 'callback data 2')
            keyboard.newLine()
            keyboard.add('Example 3', 'https://google.it')
            bot.sendMessage(chat_id=chat_id, text='Test',
                            reply_markup=keyboard)

        if text == '/keyboard':
            keyboard = EzTG.Keyboard('keyboard')
            keyboard.add('Example 1')
            keyboard.add('Example 2')
            keyboard.newLine()
            keyboard.add('Example 3')
            bot.sendMessage(chat_id=chat_id, text='Test',
                            reply_markup=keyboard)

        if text == '/hidekb':
            keyboard = EzTG.Keyboard('remove')
            bot.sendMessage(chat_id=chat_id,
                            text='Adios keyboard', reply_markup=keyboard)
    if 'callback_query' in update:
        # callback query "handler"
        message_id = update['callback_query']['message']['message_id']
        user_id = update['callback_query']['from']['id']
        chat_id = update['callback_query']['message']['chat']['id']
        cb_id = update['callback_query']['id']
        cb_data = update['callback_query']['data']

        if cb_data == 'callback data':
            bot.answerCallbackQuery(callback_query_id=cb_id, text='example #1')  # you can find method parameters in https://core.telegram.org/bots/api#answercallbackquery
            keyboard = EzTG.Keyboard('inline')
            keyboard.add('Example 2', 'callback data 2')
            bot.editMessageText(chat_id=chat_id, message_id=message_id,
                                text='New message', reply_markup=keyboard)  # you can find method parameters in https://core.telegram.org/bots/api#editmessagetext

        if cb_data == 'callback data 2':
            bot.answerCallbackQuery(
                callback_query_id=cb_id, text='example #2 [alert]', show_alert=True)
            bot.editMessageText(chat_id=chat_id, message_id=message_id,
                                text='New message 2', reply_markup={})


bot = EzTG.EzTG(token='1289065061:AAHPmXMnZXV2M5ruzj0VaowlaaL7nqEOhAo',
                callback=callback)