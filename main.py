from aiogram import Bot, Dispatcher, types, executor
from config import  TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда запуска бота'),
        types.BotCommand(command='/help', description='Команда для помощи пользоватлю'),
        types.BotCommand(command='/create', description='Команда для перехода к созданию нового бота'),
        types.BotCommand(command='/tutorial', description='Команда, которая выдает ссылку на туториал создания бота'),
        types.BotCommand(command='/exit', description='Команда для выхода из бота ')
    ]

    await bot.set_my_commands(commands)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой ЭХО бот!!!')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('Я ЭХО бот, какая от меня трубуется помощь?')

@dp.message_handler(commands='create')
async def create(message: types.Message):
    await message.answer('Вот здесь мой отец: @BotFather')

@dp.message_handler(commands='tutorial')
async def tutorial(message: types.Message):
    await message.answer('Данный бот сделан по гайду преподавателя 26 КАДРА: https://youtube.com/playlist?list=PLBxD0UwW2SxmiogBXtVv5kItQXXQaPPKh&si=2LBtjzJ6Otbuvqbi')

@dp.message_handler(commands='exit')
async def exit(message: types.Message):
    await message.answer('Пока. Надеюсь больше не увидимся!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
