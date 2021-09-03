from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Merhaba **{bn}** 🎵

Ben Gruplarınızda Ban yetkisiz olarak müzik dinlemeniz için . [SAHİP](https://t.me/MangoSahip) Tarafından geliştirildim.

Beraber güzel hatıralar biriktirelim beni grubunuza alın!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Komutlar 🛠", url="https://t.me/kizilsancakbilgi")
                  ],[
                    InlineKeyboardButton(
                        "💬 Ücretli bot kanal", url="https://t.me/ucretlibotlar"
                    ),
                    InlineKeyboardButton(
                        "🔊 BİLGİ", url="https://t.me/Kizilsancakbilgi"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/HatiralaraMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Kizilsancakbilgi")
                ]
            ]
        )
   )


