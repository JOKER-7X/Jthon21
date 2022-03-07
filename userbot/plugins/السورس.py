@@ -1,58 +1,33 @@
from telethon import Button, events

from Jmthon.razan.resources.mybot import *

from telethon import events, Button
from ..Config import Config
from ..sql_helper.globals import gvarstatus
from Jmthon.razan.resources.mybot import *

ROZ_PIC = "https://telegra.ph/file/b03342dc56474dde49aa9.jpg"
ROZ_PIC = "https://telegra.ph/file/af36a6fa550bd84cea11f.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("🔺 قنـاة السـورس 🔺", "https://t.me/SU_SELVA"),
                    Button.url("🔺 المطور 🔺", "https://t.me/ttccss"),
                ]
            ]
            buttons = [[Button.url("🔺 قناة السورس 🔺", "http://t.me/SU_SELVA"), Button.url("🔺 شروحات السورس 🔺", "https://t.me/shro_selva"),],[Button.url("🔺 مطور السورس 🔺", "https://t.me/ttccss"), Button.url("🔺 مبرمج السورس 🔺", "http://t.me/tt_t_4"),],[Button.url("🔺 جروب السورس 🔺", "https://t.me/br_selva"),],[Button.url("🔺 تحديثات السورس 🔺", "https://t.me/rmdan_karim"),]]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False
                )
                result = builder.photo(ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False)
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="JMTHON - USERBOT",
                    text=ROZ,
                    buttons=buttons,
                    link_preview=False,
                )
                result = builder.document(ROZ_PIC,title="Jepthon",text=ROZ,buttons=buttons,link_preview=False)
            else:
                result = builder.article(
                    title="JMTHON - USERBOT",
                    text=ROZ,
                    buttons=buttons,
                    link_preview=False,
                )
                result = builder.article(title="Jepthon",text=ROZ,buttons=buttons,link_preview=False)
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="السورس"))
async def repo(event):
    if event.fwd_from:
        return
    RR7PP = Config.TG_BOT_USERNAME
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "السورس")
    response = await bot.inline_query(TG_BOT, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @SU_SELVA
