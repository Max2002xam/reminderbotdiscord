import discord
import asyncio
import random
import os

# --- Config ---
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FRIEND_USER_ID = int(os.getenv('FRIEND_USER_ID'))
REMINDER_MESSAGES = [
    "Bosse ou je viens chez toi!", "Bosse ou Ada sera très déçue!",
    "Bosse ou je viendrai pour ta petite soeur! (Gneu gneu.. J'ai pas de petite soeur... Attend 9 mois pour voir!)",
    "Bosse ou alors... Je crée le mouvement #Balance ton flemmard",
    "Crée ta Waifu ai comme je me crée de ennui en swipant à droite sur des mineures!",
    "Hello! Comment ça va? :) C'est moi Le vrai Norman! HAHAHAHAHA.... Bref, travaille ou je m'énerve",
    "Que dis un dromadaire à un flemmard? BOSSE! Que dis un chameau à un flemmard? BOSSE BOSSE! Et maintenant que dis-je à un flemmard? bah cette phrase en fait...",
    "Je suis à 100 M de chez toi et ce nombre ne fera que diminuer tant que tu n'auras pas commencé à travailler!"
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
