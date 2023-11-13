import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zergio"])

async def join(client):
    try:
        await client.join_chat("cari_teman_virtual_ind")
        await client.join_chat("yagitudahpokonya")
        await client.join_chat("yourpapladiesboy")
    except BaseException:
        pass
