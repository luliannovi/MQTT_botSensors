import mqtt
import pzgram
from threading import Thread
insta = 0
pool_message = ""
unmin = 0
diecimin=0
unora=0


def pool_command(chat):
    global pool_message, pool_keyboard
    pool_message = "Seleziona pressione"
    chat.send(pool_message, reply_markup=pool_keyboard)


if __name__ == "__main__":
    sensor=mqtt.mqtt_bot()
    sensor.connect_and_take()


    def catch_results(query, data, message, sender):
        global pool_message, pool_keyboard, insta, unmin, diecimin, unora
        misura = ""
        insta = sensor.temperatura
        unmin = sensor.tempMin
        unora = sensor.tempOra
        diecimin = sensor.tempDieci
        if data == "choice1":
            choice = str(insta)
            misura="Misura istantanea: "
        elif data == "choice2":
            choice = str(unmin)
            misura= "Media temperatura ultimo minuto: "
        elif data == "choice3":
            choice = str(diecimin)
            misura= "Media temperatura ultimi dieci minuti: "
        elif data == "choice4":
            choice = str(unora)
            misura="Media temperatura ultima ora: "
        pool_message += "\n" + misura + choice
        message.edit(pool_message, reply_markup=pool_keyboard)


    #SETTAGGI BOT E RELATIVI BOTTONI
    bot = pzgram.Bot("751724127:AAFlji-_pV1zwJfIG8ocwL9ei1DIMW7AVB8")
    pool_message = ""
    button1 = pzgram.create_button("Istantanea", "choice1")
    button2 = pzgram.create_button("1 m", "choice2")
    button3 = pzgram.create_button("10 m", "choice3")
    button4 = pzgram.create_button("1 h", "choice4")
    k = [[button1, button2, button3, button4]]
    pool_keyboard = pzgram.create_inline(k)


    commands = {"start": pool_command}
    bot.set_commands(commands)
    queries = {"choice1": catch_results, "choice2": catch_results, "choice3": catch_results, "choice4": catch_results}
    bot.set_query(queries)
    #SETTAGGI THREADS
    threadSensor=Thread(target=sensor.loop)
    threadBot=Thread(target=bot.run)
    threadSensor.start()
    threadBot.start()
