#telegram_bot
import pzgram

bot = pzgram.Bot("751724127:AAFlji-_pV1zwJfIG8ocwL9ei1DIMW7AVB8")
pool_message = ""
button1 = pzgram.create_button("Ista", "choice1")
button2 = pzgram.create_button("1 m", "choice2")
button3 = pzgram.create_button("10 m", "choice3")
button4 = pzgram.create_button("1 h", "choice4")
k = [[button1, button2, button3, button4]]
pool_keyboard = pzgram.create_inline(k)

def pool_command(chat):
        global pool_message, pool_keyboard
        pool_message = "Select pressure"
        chat.send(pool_message, reply_markup=pool_keyboard)

def catch_results(query, data, message, sender):
        global pool_message, pool_keyboard
        insta = 0
        unmin = 0
        unora = 0
        diecimin = 0
        if data == "choice1":
                choice = str(insta)
        elif data == "choice2":
                choice = str(unmin)
        elif data == "choice3":
                choice = str(diecimin)
        elif data == "choice4":
                choice = str(unora)

        pool_message += "\n" + "Misura" + ":" + choice
        message.edit(pool_message, reply_markup=pool_keyboard)

commands = {"start": pool_command}
bot.set_commands(commands)
queries = {"choice1": catch_results, "choice2": catch_results,"choice3": catch_results, "choice4": catch_results}
bot.set_query(queries)
bot.run()

