# bot.py
import os

import discord
import config
import classes
import re
from discord.ext import commands
from operator import itemgetter, attrgetter

RU_CHANNELS = '769116898046246934'

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!')
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot connected')


# приветствие на сервере
@bot.event
async def on_member_join(member):
    await member.guild.get_channel(config.main_text_channel).send(f"{member.name}, добро пожаловать на сервер!")


# команда позволяет найти свободную команту, для корректной работы необходимо находиться в стартовой комнате
@bot.command()
async def find_room(ctx, lang=''):
    if ctx.author.voice is not None:
        current_VC = ctx.author.voice.channel.id  # текущий голосовой канал пользователя
        print(f'Текущий канал пользователя: {current_VC}')
        chats = ctx.guild.voice_channels
        print('Участники: ' + str(ctx.guild.members))
        sort_category(chats)

        count = []
        i = 0
        # 
        while i < len(chats):
            if chats[i].user_limit == 10:
                count.append(classes.CountUsers(id_channel=chats[i].id,
                                                count=len(ctx.guild.get_channel(chats[i].id).members),
                                                limit=ctx.guild.get_channel(chats[i].id).user_limit)
                             )
                i += 1
            else:
                print('Go next')
                i += 1

        count.sort(key=lambda x: x.vacancy, reverse=False)
        print(count)
        # проверка, находится ли пользователь в стартовых каналах или в самом релевантном
        if current_VC != count[0].id and current_VC not in config.start_room:
            await ctx.message.author.move_to(ctx.guild.get_channel(count[0].id))
            await ctx.channel.send(f'{ctx.author.name}, вы были перемещены в канал {ctx.guild.get_channel(count[0].id)}.')
        else:
            await ctx.channel.send(f'{ctx.author.name}, вы находитесь в самом релевантном канале.')

    else:
        await ctx.channel.send(ctx.author.name + ', для поиска комнаты для игры зайди в голосовой канал Start_room')
        print(ctx.guild.voice_channels)


# выборка id и названия канала из списка
def sort_category(list_ch):
    i = 0
    category = []
    while i < len(list_ch):
        category.append(
            classes.Category(id_category=list_ch[i].category_id, name=list_ch[i].name, limit=list_ch[i].user_limit))
        i += 1
    print(category)
    return category


bot.run(config.TOKEN)
