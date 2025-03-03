import discord
import asyncio
import random
import os

# --- Config ---
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FRIEND_USER_ID = int(os.getenv('FRIEND_USER_ID'))
REMINDER_MESSAGES = [
    "Hey! Daily reminder to work on the Ada Bot Project 🚀",
    "Yo! Time to put some work into Ada Bot — you got this 💻",
    "Friendly ping! Ada Bot project won't build itself 🛠️",
    "Your future self will thank you for working on Ada Bot today 🔥",
    "Just a heads up — Ada Bot still needs your attention 👀"
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
        except Exception as e:
            print(f"⚠️ Failed to send DM: {e}")
    await client.close()  # Auto-exit after sending

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    await send_reminder()

client.run(BOT_TOKEN)
