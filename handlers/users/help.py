from aiogram.types import Message
from loader import dp
from aiogram.filters import Command


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("<b>Yordam bo'limi:</b>\n\n"
        "<b>Maqolalarni qidirish:</b> Siz maqolaning nomini yozing va men sizga qisqacha mazmunini taqdim etaman.\n"
        "<b>Maqolaning asosiy rasmini ko'rish:</b> Maqolani qidirganingizda, uning asosiy rasmini ham ko'rsataman.\n\n"
        "<b>Quyidagi komandalarni ishlatishingiz mumkin:</b>\n"
        "<ul>"
        "<li><b>/start</b> - Botni ishga tushirish va xush kelibsiz xabarini olish.</li>"
        "<li><b>/help</b> - Ushbu yordam bo'limini ko'rish.</li>"
        "</ul>\n\n"
        "<b>Qo'shimcha yordam uchun botning admini bilan bog'lanishingiz mumkin.</b>", parse_mode='HTML')
