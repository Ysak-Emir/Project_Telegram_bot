# import random
#
# from aiogram.utils import executor
# from aiogram import types
# from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
# from config import dp, bot
# import logging
#
# @dp.message_handler(commands=['start'])
# async def start(message:types.Message):
#     await message.reply(f'Hello: {message.from_user.full_name}')
#
# @dp.message_handler(commands=['quiz'])
# async def quiz_1(message:types.Message):
#     markup = InlineKeyboardMarkup()
#     button_call_1 =InlineKeyboardButton('Next->',callback_data='button_call_1')
#     markup.add(button_call_1)
#     question = 'Кто такой лев'
#     answer = [
#         'Лох','Бабник','Царь зверей','Бегун'
#     ]
#     await bot.send_poll(
#         chat_id=message.chat.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=2,
#         explanation='Изи',
#         explanation_parse_mode=ParseMode.MARKDOWN_V2,
#         reply_markup=markup
#     )
#
# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
# async def quiz_2(call: types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     button_call_2 = InlineKeyboardButton('Next->', callback_data='button_call_2')
#     markup.add(button_call_2)
#     question = 'Кто соверщенналетний'
#     answer = [
#         '<10', '>10<18', '18+'
#     ]
#     await bot.send_poll(
#         chat_id=call.message.chat.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=2,
#         explanation='Изи',
#         explanation_parse_mode=ParseMode.MARKDOWN_V2,
#     )
#
# @dp.message_handler(commands=['mem'])
# async def load_mem(message: types.Message):
#     photo = open('media/1.gif', 'rb')
#     photo1 = open('media/3e5abb237ab0a228326b0f11645fa0d9.jpg', 'rb')
#     photo2 = open('media/f67a2d2511fcc2d24f9a1662e04614c3.jpg','rb')
#     a = [photo2,photo1,photo]
#     a1 = random.choice(a)
#     await bot.send_photo(message.chat.id, photo=a1)
#
# @dp.message_handler()
# async def start_command(message:types.Message):
#     await bot.send_message(message.from_user.id, message.text)
#     a = int(message.text)
#     if a:
#         await bot.send_message(message.from_user.id, a ** 2)
#
#

from aiogram import types
from aiogram.utils import executor
from config import dp
import logging
from handlers import callback,client
client.register_handlers_client(dp)
callback.register_handler_callback(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True)