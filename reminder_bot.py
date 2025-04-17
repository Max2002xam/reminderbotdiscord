import discord
import asyncio
import random
import os

# --- Config ---
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FRIEND_USER_ID = int(os.getenv('FRIEND_USER_ID'))
REMINDER_MESSAGES = [
    "https://youtu.be/tSOvBex4SJU?si=RdI2oie3EVjHU6jE",
    "https://youtu.be/geWWO81GubM?si=FoIy_GGAahwFXied",
    "https://youtu.be/fHPysRp8FWg?si=I5taiK_lmDKcEzyc",
    "https://youtu.be/M69Sn3OERZo?si=X8QQwse2hcSAYr4j",
    "https://youtu.be/1giQVuoTAFM?si=XylKIwb7O_UVN8tc",
    "https://youtu.be/vnjy-35Lxjg?si=vDqKViPRnB1lkjbT",
    "https://youtu.be/k2wQZfShEPw?si=OTYsgAMcT4ZKQFKO",
    "https://youtu.be/lhE0sAMSoGI?si=-3HVQIhNtBJCsegU",
    "https://youtu.be/-wHqgSFgNhE?si=G7WunZkUcn5row59",
    "https://youtu.be/GwPHdIp5TEE?si=DXK1FvshECSx7YBt",
    "https://youtu.be/i2dCxbAFWNk?si=UnYWRDs6kHdCpHML",
    "https://youtu.be/_XmEKmYpO5w?si=fHmDWw-P3cZT-Wb2",
    "https://youtu.be/2GslmS3W78c?si=4yL_63kN_i289crz",
    "https://youtu.be/yDFCQ3dk1dM?si=hZzKA3dpfyidrWTv",
    "https://youtu.be/2GWBIiw4XZ8?si=hQ7jzetiLwMWGqGp",
    "https://youtu.be/PbkJaEqtj4U?si=4xNBjs5oqGP-tF-j",
    "https://youtu.be/ZMysDTDqK-k?si=n4HM6QkpkKvtRjzE",
    "https://youtu.be/LawPzFbatN4?si=LFu1f68__r_s0ywN",
    "https://youtu.be/NkFiBF6e_IU?si=d16QNIBdhmkqscQp"
]

# --- Bot Setup ---
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_reminder():
    await client.wait_until_ready()
    user = await client.fetch_user(FRIEND_USER_ID)
    if user:
        message = random.choice(REMINDER_MESSAGES)
        try:
            await user.send(message)
            print(f"✅ Sent reminder to {user.name}")
            print(f"Message sent : {message}")
        except Exception as e:
            print(f"⚠️ Failed to send DM: {e}")
    await client.close()  # Auto-exit after sending

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    await send_reminder()

client.run(BOT_TOKEN)
