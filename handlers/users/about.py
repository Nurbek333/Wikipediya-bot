from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("*Bot haqida:*\n\n"
        "*Wikipedia Bot* - Bu bot Wikipedia maqolalarini qidirish va ularning qisqacha mazmunini taqdim etishga yordam beradi.\n\n"
        "*Botning maqsadi:*\n"
        "- Wikipedia'dan tez va oson ma'lumot olishni ta'minlash.\n"
        "- Maqolalar va ularning rasmlari haqida umumiy ma'lumot berish.\n\n"
        "*Mualliflar:*\n"
        "- Botning ishlab chiquvchisi: Nurbek Uktamov.\n\n"
        "*Agar sizda bot haqida qo'shimcha savollar bo'lsa, /help komandasini bosing.*",
        parse_mode='MarkdownV2')

