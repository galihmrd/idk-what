import asyncio

import requests
from pyrogram import Client, filters


@Client.on_message(filters.all)
async def checker(client, message):
    id_ = message.from_user.id
    chat_ = message.chat.id
    api = f"https://api.cas.chat/check?user_id={id_}"
    session = requests.Session()
    req = session.request("get", api)
    status = req.json()["ok"]
    # Check
    get = await client.get_users(id_)
    username = get.username
    mention = get.mention
    if username == None:
        msg = await message.reply(f"{mention} user without username!")
        try:
            await client.ban_chat_member(chat_, id_)
            await msg.edit(f"{mention} Kicked!\nReason: no username")
            await asyncio.sleep(35)
            await client.unban_chat_member(chat_, id_)
        except:
            await msg.edit(f"{mention} user without username")
        if status == True:
            try:
                result = req.json()["result"]
                reason = f"https://cas.chat/query?u={id_}"
                offenses = result["offenses"]
                time_added = result["time_added"]
                await msg.edit(
                    f"**COMBOT ANTI SPAM**\n\n**User:** {mention} Kicked!\n**ID:** `{id_}`\n**Reason:** [Link]({reason})\n**Time added:** {time_added}"
                )
                await kick_member(id_, chat_)
            except Exception as e:
                await msg.edit(f"**Error:** `{e}`")
    else:
        print(username)
        if status == True:
            try:
                result = req.json()["result"]
                reason = f"https://cas.chat/query?u={id_}"
                offenses = result["offenses"]
                time_added = result["time_added"]
                msg = await message.reply(
                    f"**COMBOT ANTI SPAM**\n\n**User:** {mention} kicked!\n**ID:** `{id_}`\n**Reason:** [Link]({reason})\n**Time added:** {time_added}"
                )
                await kick_member(id_, chat_)
            except Exception as e:
                await msg.edit(f"**Error:** `{e}`")


async def kick_member(id, chat_id):
    try:
        await client.ban_chat_member(chat_id, id)
        await asyncio.sleep(30)
        await client.unban_chat_member(chat_id, id)
    except:
        pass
