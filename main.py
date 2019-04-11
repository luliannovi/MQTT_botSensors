import mqtt
import telegram_bot
import pzgram
from threading import Thread


if __name__ == "__main__":
    sensor=mqtt.mqtt_bot()
    sensor.connect_and_take()


    #SETTAGGI BOT E RELATIVI BOTTONI
    bot = pzgram.Bot("751724127:AAFlji-_pV1zwJfIG8ocwL9ei1DIMW7AVB8")
    pool_message = ""
    button1 = pzgram.create_button("Ista", "choice1")
    button2 = pzgram.create_button("1 m", "choice2")
    button3 = pzgram.create_button("10 m", "choice3")
    button4 = pzgram.create_button("1 h", "choice4")
    k = [[button1, button2, button3, button4]]
    pool_keyboard = pzgram.create_inline(k)

    telegram_bot.insta = sensor.listaTemp
    telegram_bot.unmin = sensor.tempMin
    telegram_bot.diecimin = sensor.tempDieci
    telegram_bot.unora = sensor.tempOra
    commands = {"start": telegram_bot.pool_command}
    bot.set_commands(commands)
    queries = {"choice1": telegram_bot.catch_results, "choice2": telegram_bot.catch_results, "choice3": telegram_bot.catch_results, "choice4": telegram_bot.catch_results}
    bot.set_query(queries)
    #SETTAGGI THREADS
    threadSensor=Thread(target=sensor.loop)
    threadBot=Thread(target=bot.run)
    threadSensor.start()
    threadBot.start()
