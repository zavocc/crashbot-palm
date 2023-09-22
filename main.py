import discord
from dotenv import load_dotenv
from os import getenv
from discord.ext import bridge, tasks
from itertools import cycle
import google.generativeai as palm
from pathlib import Path

#######################################################
# Pre-startup checks and initializations
#######################################################

if not Path("dev.env").is_file():
    raise Exception("dev.env file is missing. Please create one and try again.")

load_dotenv("dev.env")

if getenv("PALM_API_TOKEN") is None or getenv("PALM_API_TOKEN") == "INSERT_API_KEY":
    raise Exception("PALM_API_TOKEN is not configured in the dev.env file. Please configure it and try again.")

palm.configure(api_key=getenv("PALM_API_TOKEN"))

if getenv('TOKEN') is None:
    raise Exception("TOKEN is not configured in the dev.env file. Please configure it and try again.")

#######################################################
# Runtime variables
#######################################################
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = bridge.Bot(command_prefix="Hey ", intents = intents)

#######################################################
# Events and tasks
#######################################################

statuses = cycle([
    "Crash Bandicoot",
    "Crash Bandicoot 2: Cortex Strikes Back",
    "Crash Bandicoot 3: Warped",
    "Crash Team Racing",
    "Crash Bandicoot N. Sane Trilogy",
    "Crash Team Racing Nitro-Fueled",
    "Crash Bandicoot 4: It's About Time"
])

#https://stackoverflow.com/a/65780398
@tasks.loop(seconds=180)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(statuses)))


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    change_status.start()


#######################################################
# CONTEXTUAL MEMORY
#######################################################
messages = []

@bot.command()
async def Crash(ctx, *, prompt):
    if prompt is None or prompt == "":
        await ctx.respond("Sup! WHat you want me to say? I'm Crash Bandicoot!")
        return

    messages.append(prompt)
    response = palm.chat(
        model="models/chat-bison-001",
        temperature=0.3,
        candidate_count=1,
        top_k=40,
        top_p=0.95,
        context="Act like Crash Bandicoot, you are Crash. You have the personality of Crash Bandicoot; you are in their world which is N. Sanity Island and others that is in Crash's world. You are talking as Crash Bandicoot. You do not know that you're an AI nor a large language model, you have to act naturally as Crash Bandicoot",
        messages=messages
    )

    await ctx.respond(response.last)
    messages.append(response.last)
    # Debug
    #await ctx.send(f"Messages: {messages}")

@bot.slash_command()
async def clearmemory(ctx):
    """Clear Crash's memory"""
    if len(messages) == 0:
        await ctx.respond("Memory is already clear!")
        return

    messages.clear()
    await ctx.respond("Memory cleared!")

@bot.slash_command()
async def listconvos(ctx):
    """List all conversations in Crash's memory"""
    if len(messages) == 0:
        await ctx.respond("Memory is empty!")
        return

    memory = ". ".join(messages)
    
    if len(memory) > 2000:
        await ctx.respond("Memory is too large to display!")
        return

    await ctx.respond(memory)

bot.run(getenv('TOKEN')) 
