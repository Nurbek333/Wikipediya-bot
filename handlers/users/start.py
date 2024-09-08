from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart, Command
import wikipedia
import logging

logging.basicConfig(level=logging.INFO)
async def respond(request, lang):
    wikipedia.set_lang(lang)
    summary = wikipedia.summary(request)
    return summary
# /start komandasini ishlovchi handler
@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        # Foydalanuvchini bazaga qo'shish
        db.add_user(full_name=full_name, telegram_id=telegram_id)
        # Xush kelibsiz xabarini yuborish
        await message.answer(
            f"Salom, {full_name}!\n\n"
            "Men Wikipedia botiman. Sizga Wikipedia maqolalarini qidirishga yordam bera olaman.\n\n"
            "Quyidagi amallarni bajarishingiz mumkin:\n"
            "- Maqolalarni qidirish: Siz maqolaning nomini yozing va men sizga qisqacha mazmunini taqdim etaman.\n"
            "- Maqolaning asosiy rasmini ko'rish: Maqolani qidirganingizda, uning asosiy rasmini ham ko'rsataman.\n\n"
            "Yordam yoki qo'shimcha ma'lumot uchun /help komandasini bosing."
        )
    except Exception as e:
        # Xatoni logging qilish va foydalanuvchiga xabar yuborish
        logging.error(f"Error: {e}")
        await message.answer(f"Salom, {full_name}!\n\n"
            "Men Wikipedia botiman. Sizga Wikipedia maqolalarini qidirishga yordam bera olaman.\n\n"
            "Quyidagi amallarni bajarishingiz mumkin:\n"
            "- Maqolalarni qidirish: Siz maqolaning nomini yozing va men sizga qisqacha mazmunini taqdim etaman.\n"
            "- Maqolaning asosiy rasmini ko'rish: Maqolani qidirganingizda, uning asosiy rasmini ham ko'rsataman.\n\n"
            "Yordam yoki qo'shimcha ma'lumot uchun /help komandasini bosing.")


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
        "<b>Qo'shimcha yordam uchun botning admini bilan bog'lanishingiz mumkin.</b>", parse_mode='html')
    
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

@dp.message()
async def sndWike(message: Message):
    try:
        summary = await respond(message.text, 'uz')
        await message.answer(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"DisambiguationError: {e.options}")
