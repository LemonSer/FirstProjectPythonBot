from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import start_menu, skills
from database.database import get_user, add_user, initialize_db

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда запуска бота'),
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await bot.send_photo(message.chat.id, photo='https://www.wallpapertip.com/wmimgs/83-830704_league-of-legends-logo-wallpaper.jpg', caption= 'Приветствую, я твой помощник и путиводитель по игре LOL', reply_markup=start_menu())
    else:
        await bot.send_photo(message.chat.id, photo='https://www.wallpapertip.com/wmimgs/83-830704_league-of-legends-logo-wallpaper.jpg', caption= 'Приветствую, я твой помощник и путиводитель по игре LOL', reply_markup=start_menu())

@dp.callback_query_handler(lambda c: c.data == 'tutorial')
async def tutorial(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/leagueoflegends/images/c/c1/Mordekaiser_OriginalCentered.jpg/revision/latest?cb=20190607213523',caption='Дважды сраженный и трижды рожденный, Мордекайзер – жестокий военачальник минувшей эпохи, который с помощью некромантии обрекает души на вечное служение. Сейчас уже мало кто помнит его ранние завоевания или знает истинные пределы его могущества – но те древние души, которые это понимают, страшатся его возможного возвращения, ведь следом за миром мертвых Мордекайзер постарается захватить мир живых. Его способности:', reply_markup=skills())

@dp.callback_query_handler(lambda c: c.data == 'skills_1')
async def skills_1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/leagueoflegends/images/2/2e/Mordekaiser_Darkness_Rise.png/revision/latest?cb=20190527181220',caption='Наносящие урон автоатаки и умения Мордекайзера против вражеских чемпионов и больших монстров дают ему заряд на 4 секунды. При трех зарядах, Мордекайзер получает эффект Восхождение тьмы. Длительность эффекта обновляется при последующем нападении на чемпионов и монстров.', reply_markup=skills())
    #await bot.delete_message(callback_query.from_user.id)
@dp.callback_query_handler(lambda c: c.data == 'skills_2')
async def skills_2(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id,
                         photo='https://static.wikia.nocookie.net/leagueoflegends/images/0/0c/Mordekaiser_Obliterate.png/revision/latest?cb=20190527181318',
                         caption='Мордекайзер бьет Вечерней звездой в выбранном направлении, нанося магический урон всем пораженным врагам. Если в области поражения только один противник, то он получит больше урона.',
                         reply_markup=skills())


@dp.callback_query_handler(lambda c: c.data == 'skills_3')
async def skills_3(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/leagueoflegends/images/c/c7/Mordekaiser_Indestructible.png/revision/latest?cb=20190527181313',caption='Мордекайзер поглощает весь Потенциальный щит и превращает в его щит с той же прочностью на 4 секунды. Спустя 1.5 щит начинает медленно спадать (резко ускоряясь в конце). Спустя 0.25 секунды он может снова активировать умение.', reply_markup=skills())

@dp.callback_query_handler(lambda c: c.data == 'skills_4')
async def skills_4(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/leagueoflegends/images/f/f4/Mordekaiser_Death%27s_Grasp.png/revision/latest?cb=20190527181258',caption='Спустя задержку в 0.5 секунды Мордекайзер притягивает противников в выбранном направлении на 250 единиц и наносит им магический урон.', reply_markup=skills())

@dp.callback_query_handler(lambda c: c.data == 'skills_5')
async def skills_5(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/leagueoflegends/images/9/94/Mordekaiser_Realm_of_Death.png/revision/latest?cb=20190527181328',caption='Спустя задержку в 0.5 секунды Мордекайзер замедляет выбранного вражеского чемпиона на 75%. Если в течение этого периода цель будет в радиусе действия и будет доступной целью умения, то она в вместе с Мордекайзером переносятся в Царство смерти - особую область, независимую от основной карты. И противник, и Мордекайзер не могут покинуть арену Царства смерти. Это пространство существует 7 секунд, или пока один из них не умрет.', reply_markup=skills())





@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
