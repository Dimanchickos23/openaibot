import openai
from aiogram import executor, Dispatcher, Bot

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentTypes, ContentType

openai.organization = "org-I2oEE9P1X3Eg2cEvIaHS79gW"
openai.api_key = "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"
bot = Bot("6036138209:AAHsnAjuGAGt1MDvtZhPtpNZABbeHaERxao")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я ChatGPT, только в телеграм боте. Я знаю все, спрашивай, но порой мне придется "
                         "немного подумать, прежде чем найти верный ответ.")


@dp.message_handler(content_types='text')
async def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    await bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


@dp.message_handler(content_types=ContentType.ANY)
async def fuck_off(message):
    await message.answer("Не выёживайся, спроси машину текстовым сообщением.")


if __name__ == '__main__':
    executor.start_polling(dp)