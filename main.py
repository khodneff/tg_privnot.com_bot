from message_reader import MessageReader
from aiogram import Bot, Dispatcher, executor, types
from data import TOKEN, USER_ID


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def check_message(message: types.Message):
    if "privnote.com" in message.text:
        words = message.text.split()
        for w in words:
            if "privnote.com" in w:
                text_message = MessageReader.read_message(w)
                await bot.send_message(USER_ID, text_message)

if __name__ == '__main__':
    executor.start_polling(dp)
