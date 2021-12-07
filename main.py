from pyrogram import *
from pyrogram.types import *
from random import randint
import glob 
# ====================================================================
app = Client("MrTakRoBoT",config_file= "config.ini")
# ====================================================================
Keyboard = ReplyKeyboardMarkup(
    [
        ["🖼 Wallpaper Pc 🖼","📱 Wallpapers Mobile 📱"],
        ["👤 Contact us 👤","ℹ️ Information ℹ️"]

    ],resize_keyboard=True
)
# ====================================================================
BOTID = "@WallpaperMrTakBot"
ADMINID = "@MrTakDev"
# ====================================================================
@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""🔥Hello <b>{message.from_user.mention}</b> ,
Welcome to the wallpaper robot. Here you can find the best wallpapers😍""",reply_markup=Keyboard,parse_mode="html")
# ====================================================================
async def Wallpaper_pc(client, message):
    Chat_id = message.chat.id
    Wallpapemobile1 = glob.glob("/home/mrtak/MrTak/Bot/Wallpaper/Wallpapers/Wallpape_pc/*.jpg")
    len1 = len(Wallpapemobile1)-1
    random1 = randint(0,len1)
    await app.send_photo(Chat_id,f"{Wallpapemobile1[random1]}",caption=f"Wallpaper 4K\n\n🆔 **{BOTID}**",parse_mode="markdown")
    await app.send_document(Chat_id,f"{Wallpapemobile1[random1]}",caption=f"Wallpaper 4K\n\n🆔 **{BOTID}**",parse_mode="markdown")
# ====================================================================
async def Wallpapers_mobile(client, message):
    Chat_id = message.chat.id
    Wallpapemobile2 = glob.glob("/home/mrtak/MrTak/Bot/Wallpaper/Wallpapers/Wallpape_mobile/*jpg")
    len2 = len(Wallpapemobile2)-1
    random2 = randint(0,len2)
    await app.send_photo(Chat_id,f"{Wallpapemobile2[random2]}",caption=f"Wallpaper 4K\n\n🆔 **{BOTID}**",parse_mode="markdown")
    await app.send_document(Chat_id,f"{Wallpapemobile2[random2]}",caption=f"Wallpaper 4K\n\n🆔 **{BOTID}**",parse_mode="markdown")
# ====================================================================
async def Information(client, message):
    await message.reply_text(f"""
`┌┬` __User info__
`│├` First Name:  `{message.from_user.first_name}`
`│├` Last Name:  `{message.from_user.last_name}`
`│├` Username:  `@{message.from_user.username}`
`│├` ID:  `{message.from_user.id}` """,reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
async def Contact_us(client, message):
    await message.reply_text(f"""👤 If you have a problem with an idea, you can contact the following ID🔥
🆔 **{ADMINID}**""",reply_markup=Keyboard,parse_mode="markdown")
# ====================================================================
@app.on_message()
async def Main(client, message):
    Text = message.text
    if Text == "🖼 Wallpaper Pc 🖼":
        await Wallpaper_pc(client, message)
    elif Text == "📱 Wallpapers Mobile 📱":
        await Wallpapers_mobile(client, message)
    elif Text == "👤 Contact us 👤":
        await Contact_us(client, message)
    elif Text == "ℹ️ Information ℹ️":
        await Information(client, message)
# ====================================================================
app.run()
