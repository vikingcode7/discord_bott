import discord
import random
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)

# ================= EASY =================

easy_questions = [
    "Mi a kedvenc filmed?",
    "Mi a kedvenc kajád?",
    "Ki a kedvenc zenészed?",
    "Mi volt a legjobb napod idén?",
    "Mi a kedvenc színed?",
    "Voltál már szerelmes?",
    "Mi a kedvenc játékod?",
    "Mi a kedvenc tantárgyad?",
    "Ki a legjobb barátod?",
    "Mi a kedvenc sportod?",
    "Mi a kedvenc italod?",
    "Mi volt az első telefonod?",
    "Mi a kedvenc sorozatod?",
    "Hova utaznál el most azonnal?",
    "Mi az álommunkád?",
    "Melyik városba költöznél?",
    "Mi a kedvenc évszakod?",
    "Mi a kedvenc édességed?",
    "Kivel cserélnél életet egy napra?",
    "Mi volt az utolsó dolog, amin nevettél?"
]

easy_dares = [
    "Küldj egy random emojit.",
    "Írj valamit CAPS LOCKKAL.",
    "Írj egy vicces mondatot.",
    "Küldj egy GIF-et.",
    "Írj egy bókot valakinek.",
    "Változtasd meg a profilképed 5 percre.",
    "Írj egy szívecskét a chatbe.",
    "Írj egy random számot 1-100 között.",
    "Küldj egy mém linket.",
    "Írj egy rövid verset.",
    "Írj csak hangulatjelekkel egy mondatot.",
    "Írj egy szóviccet.",
    "Írj valamit visszafelé.",
    "Küldj egy régi fotót (ha mersz).",
    "Írj egy kedvenc idézetet.",
    "Írj valamit csupa kisbetűvel.",
    "Írj valamit csupa nagybetűvel.",
    "Írj egy random szót.",
    "Küldj egy zene linket.",
    "Írj 3 dolgot, amit szeretsz."
]

# ================= MEDIUM =================

medium_questions = [
    "Mi volt a legkínosabb pillanatod?",
    "Ki tetszik most titokban?",
    "Volt már olyan, hogy hazudtál egy barátodnak?",
    "Mi volt a legrosszabb randíd?",
    "Kit csókolnál meg ebből a szerverből?",
    "Mi a legnagyobb félelmed?",
    "Mi volt a legcikibb üzenet, amit küldtél?",
    "Volt már olyan, hogy lebuktál?",
    "Kivel nem beszélnél többé?",
    "Mi volt a legfurcsább álmod?",
    "Volt már titkos crushod?",
    "Mi az, amit megbántál?",
    "Volt már, hogy sírtál valaki miatt?",
    "Ki az, akiben most csalódtál?",
    "Mi volt a legnagyobb veszekedésed?",
    "Volt már, hogy irigy voltál valakire?",
    "Mi a legkellemetlenebb emléked?",
    "Volt már, hogy ghostoltál valakit?",
    "Kinek írnál most azonnal?",
    "Mi a legnagyobb hülyeség, amit csináltál?"
]

medium_dares = [
    "Írj egy szerelmes üzenetet valakinek.",
    "Változtasd meg a neved 5 percre.",
    "Írj rá valakire, akivel rég beszéltél.",
    "Írj egy titkos crushodnak.",
    "Küldj egy selfie-t.",
    "Hívd fel valakit és mondd, hogy hiányzik.",
    "Írj be valami kínos dolgot magadról.",
    "Írj egy szívecskét annak, aki utoljára írt.",
    "Írj egy random számot 1-1000 között.",
    "Írj egy titkot.",
    "Írj valamit, amit még nem mondtál el senkinek.",
    "Küldj egy hangüzenetet.",
    "Írj valakinek egy vicces bókot.",
    "Írj egy random szerelmi vallomást.",
    "Küldj egy gyerekkori képet.",
    "Írj egy ciki sztorit.",
    "Írj egy őszinte véleményt.",
    "Írj egy régi crushodnak.",
    "Írj valamit, amit most gondolsz.",
    "Írj valamit, amitől zavarba jössz."
]

# ================= HARD =================

hard_questions = [
    "Mi a legnagyobb titkod?",
    "Volt már, hogy megcsaltál valakit?",
    "Kibe voltál igazán szerelmes?",
    "Mi az, amit senkinek nem mondtál el?",
    "Volt már illegális dolgod?",
    "Mi volt a legdurvább hazugságod?",
    "Kihez vonzódsz most igazán?",
    "Mi volt a legnagyobb hibád kapcsolatban?",
    "Kit csókolnál meg most?",
    "Kivel feküdnél le a szerverből?",
    "Mi az, amit szégyellsz?",
    "Mi volt a legdurvább veszekedésed?",
    "Mi az, amit legjobban megbántál?",
    "Mi volt a legkínosabb lebukásod?",
    "Mi a legsötétebb gondolatod?",
    "Volt már, hogy szándékosan bántottál valakit?",
    "Mi volt a legmerészebb dolgod?",
    "Mi a legnagyobb féltékenységed?",
    "Kinek törted már össze a szívét?",
    "Mi az, amitől igazán félsz?"
]

hard_dares = [
    "Hívd fel valakit és mondd, hogy szereted.",
    "Írj rá a crushodra most.",
    "Mondd el a legkínosabb sztorid.",
    "Küldj egy nagyon ciki képet.",
    "Írj valakinek, akivel haragban vagy.",
    "Írj egy őszinte vallomást.",
    "Változtasd meg a neved valami ciki dologra 10 percre.",
    "Küldj egy hangüzenetet most.",
    "Írj le egy titkot.",
    "Írj valamit, amit még sosem mertél.",
    "Írj valakinek egy random szerelmi vallomást.",
    "Írj egy hosszú bocsánatkérést.",
    "Írj annak, aki most eszedbe jut.",
    "Írj be egy ciki sztorit.",
    "Küldj egy gyerekkori képet.",
    "Írj be valamit, amit szégyellsz.",
    "Írj valamit, amit titkoltál.",
    "Írj egy durva igazságot.",
    "Írj be egy nagyon őszinte dolgot.",
    "Írj valamit, amit sosem mondanál hangosan."
]

# ================= JÁTÉK LOGIKA =================

active_games = {}

@client.event
async def on_ready():
    print(f"Bejelentkezve mint {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!play":

        game_message = await message.channel.send(
            "🎮 **Válassz nehézségi szintet!**\n\n"
            "🟢 Easy\n"
            "🟡 Medium\n"
            "🔴 Hard"
        )

        await game_message.add_reaction("🟢")
        await game_message.add_reaction("🟡")
        await game_message.add_reaction("🔴")

@client.event
async def on_reaction_add(reaction, user):

    if user == client.user:
        return

    message = reaction.message

    if "Válassz nehézségi szintet" in message.content:

        if reaction.emoji == "🟢":
            level = "easy"
        elif reaction.emoji == "🟡":
            level = "medium"
        elif reaction.emoji == "🔴":
            level = "hard"
        else:
            return

        active_games[user.id] = level

        msg = await message.channel.send(
            f"🎤🔥 **{level.upper()} mód kiválasztva!**\n"
            "🎤 = Felelsz\n"
            "🔥 = Mersz"
        )

        await msg.add_reaction("🎤")
        await msg.add_reaction("🔥")

    elif reaction.emoji in ["🎤", "🔥"]:

        if user.id not in active_games:
            return

        level = active_games[user.id]

        if level == "easy":
            questions, dares = easy_questions, easy_dares
        elif level == "medium":
            questions, dares = medium_questions, medium_dares
        else:
            questions, dares = hard_questions, hard_dares

        if reaction.emoji == "🎤":
            await message.channel.send(f"🎤 {level.upper()} FELELSZ:\n{random.choice(questions)}")
        else:
            await message.channel.send(f"🔥 {level.upper()} MERSZ:\n{random.choice(dares)}")

client.run(DISCORD_TOKEN)