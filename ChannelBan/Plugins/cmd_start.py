from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>𝑯𝒆𝒚 {message.from_user.first_name} 👋😝!</b>
 `𝑯𝒆𝒚𝒂 𝑰'𝒎 𝑨 𝑨𝒏𝒕𝒊 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒃𝒐𝒕 𝒕𝒐 𝒅𝒆𝒍𝒆𝒕𝒆 𝒂𝒏𝒅 𝒃𝒂𝒏 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒔𝒆𝒏𝒕 𝒃𝒚 𝒄𝒉𝒂𝒏𝒏𝒆𝒍`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Channel", url="https://t.me/Tg_Galaxy"
                    ),
                    InlineKeyboardButton(
                        "➕Add Me To Group➕", url="http://t.me/AntiChannelBan_x2bot?startgroup=botstart"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔻Clone Owner🔻", url="https://t.me/HydraLivegrambot"
                    )
                ]
            ]
        )
    )
