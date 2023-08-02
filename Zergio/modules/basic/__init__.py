import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zergio"])

async def join(client):
    try:
        await client.join_chat("mutualan_cari_teman_virtual")
        await client.join_chat("RuangGabutArman")
        await client.join_chat("zerrcode")
        await client.join_chat("StoreKarman")
        await client.join_chat("zersupport_bot_telegram")
        await client.join_chat("StoryMan01")
    except BaseException:
        pass
