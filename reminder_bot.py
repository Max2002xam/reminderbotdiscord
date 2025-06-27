import discord
import asyncio
import random
import os

# --- Config ---
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FRIEND_USER_ID = int(os.getenv('FRIEND_USER_ID'))
REMINDER_MESSAGES = [
    "Tu dois repasser des exams, j'aurais bien fait une vidéo là dessus, mais bon, j'aurais plagiat cyprien avec l'école et tout... Bref bosse",
    "Tu savais que 60% de l'architecture du première ordinateur avait été trouvé par pur hasard? Non c'est pas vrai, t'aurais pu le savoir si tu bossais!",
    "Si tu échoues, je ferais une vidéo en featuring avec toi! Donc t'as intérêt à bosser!",
    "Tu connais la différence et le point commun entre en chômeur et un youtubeur? Les deux ont échouer leurs études! Mais l'un n'en branle pas une, l'autre en branle plusieur pas mûres!",
    "'Un jour je serai le meilleur chômeur!' : Toi si tu bosses pas assez!",
    "Pour chaque jour que tu bosses pas, j'envoie un mp à Ada!",
    "hey Salut tu me reconnais hein! J'oganise un concours pour mes plus grand fans! Intéressé? Tout ce que tu dois faire, c'est raté tes examens, et je viendrais chez toi!",
    "Travaille.",
    "Si tu réussis tes exams, j'avoue tout!",
    "Tu gagnes?",
    "Grindset entrepreneur, au moins, dans toutes mes accusations, j'ai jamais été accusé de vendre des formations! C'est déjà ça non?",
    "On a pas d'omelette sans casser des oeufs! Et j'en ai cassé pas mel des oeufs si tu vois ce que je veux dire!",
    "https://fyooyzbm.filerobot.com/v7/https://static01.nicematin.com/media/npo/xlarge/2016/04/maxpeopleworld877824.jpg?w=480&h=382&gravity=auto&func=crop",
    "https://prmeng.rosselcdn.net/sites/default/files/dpistyles_v2/prm_16_9_856w/2024/08/12/node_550223/44451020/public/2024/08/12/23887772.png?itok=ISc952Wi1723450445",
    "https://media.tenor.com/h31MaizyP6UAAAAM/norman-thavaud-youtuber.gif",
    "https://media.tenor.com/SCCPpyuLLN0AAAAM/norman-thavaud-tu-veux-sortir-avec-moi.gif",
    "https://media.tenor.com/1_ezLtwam7wAAAAM/nul-norman-thavaud.gif",
    "Salut c'est Norman, si tu échoues tes exams, tu devras m'envoyer une photo de toi nu! Déso! C'est les règles!",
    "Alors? Ça bosse?"
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
