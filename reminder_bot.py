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
    "Bosse ou alors... Je crée le mouvement #BalanceTonFlemmard",
    "Crée ta Waifu ai comme je me crée de ennui en swipant à droite sur des mineures!",
    "Hello! Comment ça va? :) C'est moi Le vrai Norman! HAHAHAHAHA.... Bref, travaille ou je m'énerve",
    "Que dis un dromadaire à un flemmard? BOSSE! Que dis un chameau à un flemmard? BOSSE BOSSE! Et maintenant que dis-je à un flemmard? bah cette phrase en fait...",
    "Je suis à 100 M de chez toi et ce nombre ne fera que diminuer tant que tu n'auras pas commencé à travailler!",
    "Yo c’est Norman, j’voulais juste te rappeler de bosser sur Ada… sinon j’vais devoir t’envoyer des snaps ‘spéciaux’.",
    "T’as toujours pas touché à Ada ? T’es presque aussi inactif que la police face à mes DM.",
    "Si tu travailles pas sur Ada aujourd’hui, j’te follow sur Insta… et t’as vu comment ça finit en général.",
    "Salut c’est Norman, t’as pensé à Ada ? Ou tu veux que j’te file une masterclass en grooming plutôt ?",
    "Bosser sur Ada, c’est comme une conversation avec moi : c’est long, malaisant, mais t’as pas vraiment le choix.",
    "C’est Norman, j’te rappelle qu’Ada t’attend… sauf si tu préfères qu’on discute en privé toi et moi.",
    "Si Ada avance pas aujourd’hui, j’t’ajoute à mon groupe Snap privé.",
    "Travaille sur Ada… sinon j’te demande ta carte d’identité, juste pour ‘vérifier’.",
    "Si Ada avait un vrai copain, il bosserait pour elle!",
    "Ada m’a DM, elle m’a dit qu’elle pense quitter ce loser qui l’ignore, pour moi bien sûr!  FAUX! ...  Enfin bref, bosse!",
    "Au fait heu... Tu comptes pas leak nos DM hein? Juste pour savoir Ahahah... Travaille au fait!",
    "Tu bosses ou je bez tes gosses!"
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
