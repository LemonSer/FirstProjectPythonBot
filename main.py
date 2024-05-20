from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_mor, get_keyboard_atr, get_keyboard_cho

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда запуска бота'),
    ]

    await bot.set_my_commands(commands)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот по LOL-у', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'В начальное меню')
async def button_10_click(message: types.Message):
    await message.answer('Привет, я твой бот по LOL-у', reply_markup=get_keyboard_1())

# Мордекайзер
@dp.message_handler(lambda message: message.text == 'Мордекайзер')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt7683195e1c4f6706/621ed30fba043c4a2c4a9f7a/RiotX_ChampionList_mordekaiser_v2.jpg?quality=90&width=250', caption= 'Мордекайзер', reply_markup=get_keyboard_mor())

@dp.message_handler(lambda message: message.text == 'ВОСХОЖДЕНИЕ ТЬМЫ')
async def button_5_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://cybersport-bet.ru/images/article/_webp/519971/mordekaiser-ability.webp' , caption= 'ВОСХОЖДЕНИЕ ТЬМЫ - Мордекайзер получает ауру, наносящую большой урон, и ускоряется после попадания 3 атаками или умениями по чемпионам или монстрам.')

@dp.message_handler(lambda message: message.text == 'УНИЧТОЖЕНИЕ')
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://d28xe8vt774jo5.cloudfront.net/champion-abilities/0082/ability_0082_Q1.jpg', caption= 'УНИЧТОЖЕНИЕ - Мордекайзер бьет по земле булавой, нанося урон каждому пораженному врагу. Если враг один, урон по нему увеличивается.')

@dp.message_handler(lambda message: message.text == 'НЕСОКРУШИМЫЙ')
async def button_7_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.ytimg.com/vi/fhzRVabMg2Q/maxresdefault.jpg', caption= 'НЕСОКРУШИМЫЙ - Мордекайзер накапливает нанесенный и полученный урон, а затем превращает его в щит. Он может поглотить щит, восстановив себе здоровье.' )

@dp.message_handler(lambda message: message.text == 'СМЕРТЕЛЬНАЯ ХВАТКА')
async def button_8_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.ytimg.com/vi/9YXHvWKTDRw/maxresdefault.jpg', caption= 'СМЕРТЕЛЬНАЯ ХВАТКА - Мордекайзер подтягивает всех врагов в области поражения.')

@dp.message_handler(lambda message: message.text == 'ЦАРСТВО СМЕРТИ')
async def button_9_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://1.bp.blogspot.com/-fWnH3zf77FY/XO1uClW1HXI/AAAAAAABTe0/3qeY1RpmH_gZnKCONOonDQiUeLqDzeAnACLcBGAs/s1600/14.png', caption= 'ЦАРСТВО СМЕРТИ - Мордекайзер переносит себя и жертву в другое измерение и похищает часть показателей цели. Если Мордекайзер убивает ее, он сохраняет показатели жертвы до ее возрождения')


# Атрокс
@dp.message_handler(lambda message: message.text == 'Атрокс')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt570145160dd39dca/5db05fa8347d1c6baa57be25/RiotX_ChampionList_aatrox.jpg?quality=90&width=250', caption= 'Атрокс', reply_markup=get_keyboard_atr())

@dp.message_handler(lambda message: message.text == 'СТОЙКА РАЗРУШИТЕЛЯ')
async def button_11_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://yt3.ggpht.com/a/AATXAJzx3t3zKOS1z9EpedNS3dga6uy_AS1CY5c1=s900-c-k-c0xffffffff-no-rj-mo' , caption= 'СТОЙКА РАЗРУШИТЕЛЯ - Периодически следующая автоатака Атрокса дополнительно наносит физический урон в зависимости от максимального запаса здоровья цели и лечит его.')

@dp.message_handler(lambda message: message.text == 'КЛИНОК ДАРКИНОВ')
async def button_12_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yt3.googleusercontent.com/KMJsT-baBSxQKPPiZ4GILIEfuErXK-51358pSWdztU_Tu8kQ1Va09PGNfeW1cm9-kQ0r-2oe=s900-c-k-c0x00ffffff-no-rj', caption= 'КЛИНОК ДАРКИНОВ - Атрокс бьет мечом сверху вниз, нанося физический урон. Он может ударить три раза, и каждый раз область поражения будет меняться.')

@dp.message_handler(lambda message: message.text == 'ПРОКЛЯТЫЕ ЦЕПИ')
async def button_13_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://cdna.artstation.com/p/assets/covers/images/050/534/760/large/jose-estrada-jose-estrada-aatroxthumbnail2.jpg?1655099446', caption= 'ПРОКЛЯТЫЕ ЦЕПИ - Атрокс бьет по земле, нанося урон первому пораженному врагу. Если чемпионы или большие монстры не покинут область действия, то будут притянуты к ее центру и снова получат урон.' )

@dp.message_handler(lambda message: message.text == 'ТЕМНЫЙ РЫВОК')
async def button_14_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yt3.ggpht.com/a/AATXAJwKd7_Vj8S4PgPkBWCXK3Frr7NOu5wS1n6akg=s900-c-k-c0xffffffff-no-rj-mo', caption= 'ТЕМНЫЙ РЫВОК - Атрокс пассивно восстанавливает себе здоровье при нанесении урона вражеским чемпионам. При активации он совершает рывок в выбранном направлении.')

@dp.message_handler(lambda message: message.text == 'ГУБИТЕЛЬ МИРА')
async def button_15_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://sun9-40.userapi.com/c851124/v851124960/e49da/tako-cE-84g.jpg', caption= 'ГУБИТЕЛЬ МИРА - Атрокс принимает демоническую форму, пугая ближайших вражеских миньонов, а также увеличивая свою силу атаки, принимаемое лечение и скорость передвижения. Если он зарабатывает убийство или содействие, продолжительность эффекта увеличивается.')

# Чо`Гат

@dp.message_handler(lambda message: message.text == 'Чо`Гат')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Chogath_0.jpg', caption= 'Чо`Гат', reply_markup=get_keyboard_cho())

@dp.message_handler(lambda message: message.text == 'ПЛОТОЯДНОСТЬ')
async def button_17_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.ytimg.com/vi/JRYvjWUA-R8/hqdefault.jpg' , caption= 'ПЛОТОЯДНОСТЬ - Каждый раз, когда Чо Гат убивает бойца, он восстанавливает себе здоровье и ману. Величина восстановления растет с уровнем Чо Гата.')

@dp.message_handler(lambda message: message.text == 'ПРОЛОМ')
async def button_18_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://3.bp.blogspot.com/-icOqlT1QpuE/WmfflqeC23I/AAAAAAAA3s8/WB3sPQstG_McYgYnaCiioZcvQBXT8uTLgCLcBGAs/s1600/chogathq.jpg', caption= 'ПРОЛОМ - Пронзает землю в указанной области, подбрасывая в воздух врагов и замедляя их.')

@dp.message_handler(lambda message: message.text == 'ДИКИЙ КРИК')
async def button_19_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://imgs.plurk.com/QuR/dc7/b2T8P0rrI8uJYah03ebbP706Xdd_tn.jpeg', caption= 'ДИКИЙ КРИК - Чо Гат издает ужасающий крик, который наносит находящимся перед ним врагам магический урон и заставляет их замолчать на несколько секунд.' )

@dp.message_handler(lambda message: message.text == 'СМЕРТОНОСНЫЕ ШИПЫ')
async def button_20_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://imgs.plurk.com/QuR/3zu/NVTx66bvCaEt4c6r66z1iNMfkVT_tn.jpeg', caption= 'СМЕРТОНОСНЫЕ ШИПЫ - При каждой автоатаке Чо Гат выпускает смертоносные шипы, наносящие урон всем врагам перед ним и замедляя их.')

@dp.message_handler(lambda message: message.text == 'ПОЖИРАНИЕ')
async def button_21_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://imgs.plurk.com/QuR/din/RLaTbmUTKwik0sFEXzIQ8i2lF5q_tn.jpeg', caption= 'ПОЖИРАНИЕ - Чо Гат пожирает врага, нанося ему большое количество чистого урона. Если цель умирает, Чо Гат растет, получая прибавку к максимальному запасу здоровья.')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
