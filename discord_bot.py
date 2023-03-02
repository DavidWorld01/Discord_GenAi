#Import necessary libraries and modules
import discord
from class_chatgpt import Gpt_API
from class_replicate import Replicate_API
from water_mark import Water_Mark
from discord.ext import commands
import time

#Loading .env file and it's information
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

# Setting up discord bot client
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

# Welcome message
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



@bot.command()
async def ask(ctx):
    author = ctx.message.author
    user_id = ctx.message.author.id
    #print(query)
    print(ctx.message.content)
    if author == bot.user:
        return
    
    elif isinstance(ctx.message.channel, discord.channel.DMChannel):
        if user_id in bot.recent_user_messages and time.time() - bot.recent_user_messages[user_id] < 16:
                if user_id not in cooldown_sent:
                    await ctx.reply(f"15 sec. cooldown...")
                    cooldown_sent.add(user_id)
                return
        else:
            if len(ctx.message.content)<5 or ctx.message.content[4]=='@':
                # bot.recent_user_messages[user_id] = time.time()
                # cooldown_sent.discard(user_id)
                await ctx.reply(f"Please type your query after the command by having a space between them, like this:\n/ask Who is Joe Biden?")
            else:
                bot.recent_user_messages[user_id] = time.time()
                cooldown_sent.discard(user_id)
                query = ctx.message.content[5:]
                res_obj = Gpt_API(query)
                result = res_obj.get_result()
                # If the message was sent in a private message, reply in a private message
                await ctx.reply(f"{result}")

    else:
        if user_id in bot.recent_user_messages and time.time() - bot.recent_user_messages[user_id] < 16:
                if user_id not in cooldown_sent:
                    await ctx.reply(f"15 sec. cooldown...")
                    cooldown_sent.add(user_id)
                return
        else:
            if len(ctx.message.content)<5 or ctx.message.content[4]=='@':
                # bot.recent_user_messages[user_id] = time.time()
                # cooldown_sent.discard(user_id)
                await ctx.reply(f"Please type your query after the command by having a space between them, like this:\n/ask Who is Joe Biden?")
            else:
                bot.recent_user_messages[user_id] = time.time()
                cooldown_sent.discard(user_id)
                query = ctx.message.content[5:]
                res_obj = Gpt_API(query)
                result = res_obj.get_result()
                # If the message was sent in a private message, reply in a private message
                await ctx.reply(f"{result}")
         
    #await ctx.send('Pong!')

@bot.command()
async def mai(ctx):
    author = ctx.message.author
    user_id = ctx.message.author.id
    query = ctx.message.content
    if author == bot.user:
        return
    elif isinstance(ctx.message.channel, discord.channel.DMChannel):
        if user_id in bot.recent_user_messages and time.time() - bot.recent_user_messages[user_id] < 16:
                    if user_id not in cooldown_sent:
                        await ctx.reply(f"15 sec. cooldown...")
                        cooldown_sent.add(user_id)
                    return
        else:
            if len(ctx.message.content)<5 or ctx.message.content[4]=='@':
                # bot.recent_user_messages[user_id] = time.time()
                # cooldown_sent.discard(user_id)
                await ctx.reply(f"Please type your prompt after the command by having a space between them, like this:\n/mai A fox looking at the sky, hd, dramatic lightning")
            else:
                bot.recent_user_messages[user_id] = time.time()
                cooldown_sent.discard(user_id)
                temp = await ctx.reply(f"Processing command by {author.mention}...")
                obj = Replicate_API(query)
                url = obj.get_result()[0]
                print("Got result")
                obj_watermark= Water_Mark(url)
                obj_watermark.get_result()
                print("Image saved")
                photo_file = open('result.png', 'rb')
                print("photo opened")
                # Create a discord.File object for the photo
                photo = discord.File(photo_file)
                await temp.delete()
                #print(type(author))
                name = str(author)
                caption = f'```{ctx.message.content}```'
                embed = discord.Embed(
                    title='Image generated with MiraAi.i',
                    url='https://miraai.io/',
                    description=f'Created by {name}\n{caption}',
                    color=0x7289da
                )
                
                # Open the photo file and create a Discord file object
                with open('result.png', 'rb') as f:
                    result = discord.File(f)
                    embed.set_image(url='attachment://result.png')
                
                embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1623297779341590529/ns6SQu4N_400x400.jpg')
                
                # Send the message with the photo and caption
                await ctx.send(f"Image created by {author.mention}",embed=embed,file=result) #,file=photo
                # Send the photo as a reply to the message
                # await ctx.reply(aa,file=photo)
    else:
        if user_id in bot.recent_user_messages and time.time() - bot.recent_user_messages[user_id] < 16:
                    if user_id not in cooldown_sent:
                        await ctx.reply(f"15 sec. cooldown...")
                        cooldown_sent.add(user_id)
                    return
        else:
            if len(ctx.message.content)<5 or ctx.message.content[4]=='@':
                # bot.recent_user_messages[user_id] = time.time()
                # cooldown_sent.discard(user_id)
                await ctx.reply(f"Please type your prompt after the command by having a space between them, like this:\n/mai A fox looking at the sky, hd, dramatic lightning")
            else:
                bot.recent_user_messages[user_id] = time.time()
                cooldown_sent.discard(user_id)
                temp = await ctx.reply(f"Processing command by {author.mention}...")
                obj = Replicate_API(query)
                url = obj.get_result()[0]
                print("Got result")
                obj_watermark= Water_Mark(url)
                obj_watermark.get_result()
                print("Image saved")
                photo_file = open('result.png', 'rb')
                print("photo opened")
                # Create a discord.File object for the photo
                photo = discord.File(photo_file)
                await temp.delete()
                caption = f'```{ctx.message.content}```'
                name = str(author)

                embed = discord.Embed(
                    title='Image generated with MiraAi.i',
                    url='https://miraai.io/',
                    description=f'Created by {name}\n{caption}',
                    color=0x7289da
                )
                
                # Open the photo file and create a Discord file object
                with open('result.png', 'rb') as f:
                    result = discord.File(f)
                    embed.set_image(url='attachment://result.png')
                
                embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1623297779341590529/ns6SQu4N_400x400.jpg')
                
                # Send the message with the photo and caption
                await ctx.send(f"Image created by {author.mention}",embed=embed,file=result)

@bot.command()
async def helper(ctx):
    author = ctx.message.author
    user_id = ctx.message.author.id
    #print(query)
    print(ctx.message.content)
    if author == bot.user:
        return
    else:
        await ctx.reply(f"You will have two features in this bot.\n1. Image generation\n2.Text Generation\n\nBy typing,  /ask<space><your query> , you can ask the bot anything, and you will get answer.\n\nBy typing,  /gen<space><your prompt> , you can generate images with based on your prompt.")

        

cooldown_sent = set()
bot.recent_user_messages = {}
# Run the bot
bot.run(BOT_TOKEN)
