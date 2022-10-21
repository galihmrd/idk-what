import asyncio

from pyrogram import Client, filters


@Client.on_message(filters.all)
async def checker(client, message):
    id_ = message.from_user.id
    chat_ = message.chat.id
    # Check
    get = await client.get_users(id_)
    username = get.username
    mention = get.mention
    if username == None:
        msg = await message.reply(f"{mention} user without username!")
        try:
            await client.ban_chat_member(chat_, id_)
            await msg.edit(f"{mention} Kicked!")
            await asyncio.sleep(35)
            await client.unban_chat_member(chat_, id_)
        except:
            await msg.edit(f"{mention} user without username")
    else:
        print(username)
