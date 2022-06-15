from imp import get_tag
from os import remove
from posixpath import split
from aiohttp import get_payload
import discord
from discord.ext import commands
import random
import pickle

intents = discord.Intents.all()
swears = ['сос' , 'ху', 'еб', 'пизд', 'пид', 'гандон', 'бля']
bot = commands.Bot(command_prefix=['eblan ', 'Eblan ', 'еблан ', 'Еблан '])
client = discord.client
bazafile = open('baza.txt', 'r')
baza = bazafile.read().split()
bazafile.close()
bazalen = len(baza)
banned_users_id = []

@bot.command()
async def насратьвчат(ctx):
    if check_is_muted(ctx.author.id): 
        return
    for a in range(1,11):
        await ctx.send(f'срем в чат.....{a * 10}%')
    await ctx.send('Готово! Чат обосран!')

@bot.command()
async def убить(ctx, user: discord.Member, *, reason=None):
    if check_is_muted(ctx.author.id): return 
    else:
	    await ctx.send(f"{user} БЫЛ УБИТ РУКАМИ {ctx.author.mention}")

@bot.command()
async def шар(ctx):
    if check_is_muted(ctx.author.id): return
    res = random.randrange(1, 3)
    if (res == 1):
        await ctx.send('да')
    else: await ctx.send('нет')

@bot.command()
async def полай(ctx):
    if check_is_muted(ctx.author.id): return
    await ctx.send('гав гав')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Portal 2", url = 'google.com'))
    print('My Ready is Body')

#@bot.event
#async def on_command_error(ctx, error):
#    await ctx.send('че')
def check_is_muted(id):
    return (id in banned_users_id)

@bot.listen()
async def on_message(message):
    if message.author.id == 362905187901505536 and len(users_to_approve_ban_ids) > 0:
        if message.content == 'да брат':
            banned_users_id.append(users_to_approve_ban_ids[-1])
            users_to_approve_ban_ids.pop()
            await message.channel.send('ЗАБАНИЛ СЫНОЧКУ')
        if message.content == 'нет брат':
            users_to_approve_ban_ids.pop()
            await message.channel.send('ну нет так нет')
    if message.author == bot.user:
        return
    if (message.author.id in banned_users_id):
        return await message.delete()
    if message.content.lower().split()[0] == 'еблан' and len(message.content.lower().split()) > 1:
        return
    for a in swears:
        if a in message.content.lower():
            rnd = random.randrange(1 , 4)
            if (rnd == 3):
                await message.channel.send('не матерись :delet:')
    if ('бот' in message.content.lower()):
        await message.channel.send('кто меня звал')
    if ("slamix" in message.content.lower() or "слемикс" in message.content.lower() or "сламикс" in message.content.lower()):
        await message.reply('фууууу блять фууууу')
    if "кристал" in message.content.lower() or "кристл" in message.content.lower():
        await message.reply("папа?")
    if "кора" in message.content.lower() or "kora" in message.content.lower():
        await message.reply("ебет баранов")
    #Я НЕ СМОГ СДЕЛАТЬ НОРМАЛЬНЫЙ МЕТОД ДЛЯ ИТЕРАЦИИ ИГРЫ. АСИНКИ В ПИТОНЕ ЛОЛ)))
    if (len(players) > 0):
        for player in players:
            if player.Player == message.author and message.content.isdigit() and player.Attempts > 0:
                if int(message.content) == player.Number:
                    playersid.remove(player.id)
                    players.remove(player)
                    players_rating[player.Player.id] += 5 * player.Attempts
                    file_to_store = open("ratings.pickle", "wb")
                    pickle.dump(players_rating, file_to_store)
                    file_to_store.close()
                    return await message.channel.send(f"{message.author.mention} АХУЕТЬ. ТЫ ПРАВ. ТВОЙ РЕЙТИНГ УВЕЛИЧЕН :nerd:")
                else: 
                    player.Attempts-=1
                    await message.channel.send(f"{message.author.mention} ТЫ ДОЛБОЕБ???? ОСТАЛОСЬ ПОПЫТОК: {player.Attempts} ")
                if (player.Attempts == 0):
                    #ЗА ЧТО ЭТИ АСИНКИ ТАК РАБОТАЮТ
                    players_rating[player.Player.id] -= 10
                    file_to_store = open("ratings.pickle", "wb")
                    pickle.dump(players_rating, file_to_store)
                    file_to_store.close()
                    playersid.remove(player.id)
                    players.remove(player)
                    return await message.channel.send(f"{message.author.mention} ТЫ ПРОЕБАЛ. ТВОЙ РЕЙТИНГ УМЕНЬШЕН. ЧИСЛО БЫЛО {player.Number}")
    pass

#game
playersid = []
players = []
file_to_load = open("ratings.pickle", "rb")
players_rating = pickle.load(file_to_load)
file_to_load.close()
global password
global is_waiting_for_password
users_to_approve_ban_ids = []

async def get_id_from_tag(tag):
    id_string = tag.replace('@', '')
    id_string = id_string.replace('<', '')
    id_string = id_string.replace('>', '')
    return await bot.fetch_user(int(id_string))

@bot.command()
async def кто(ctx,id):
    if check_is_muted(ctx.author.id): return
    user = await get_id_from_tag('985159145252597813')
    return await ctx.send(f'ЭТО ОН -> {user.mention}')
@bot.command()
async def айди(ctx):
    if check_is_muted(ctx.author.id): return
    await ctx.send(ctx.author.id)

@bot.command()
async def заткнуть(ctx, member):
    if check_is_muted(ctx.author.id): return
    user_to_ban = await get_id_from_tag(member)
    print(user_to_ban.id)
    users_to_approve_ban_ids.append(user_to_ban.id)
    await ctx.send('ЗАБАНИТЬ ДУРАЧКА?')
    pass

@bot.command()
async def открыть(ctx, member):
    if check_is_muted(ctx.author.id): return
    user_to_unban = await get_id_from_tag(member)
    banned_users_id.remove(user_to_unban.id)
    await ctx.send(f"{user_to_unban.mention} БЫЛ РАЗМУЧЕН")

@bot.command()
async def игра(ctx):
    if check_is_muted(ctx.author.id): return
    p = Player(ctx.author, 5)
    if (p.id not in playersid):
        playersid.append(p.id)
        players.append(p)
        await ctx.send(f"{ctx.author.mention}ПОЕХАЛИ!!!! УГАДАЙ ЧИСЛО ОТ 1 ДО 10")
    else: await ctx.send(f"{ctx.author.mention} ТЫ УЖЕ ИГРАЕШЬ")
    

@bot.command()
async def хорош(ctx):
    if check_is_muted(ctx.author.id): return
    await ctx.send('спасибо')

@bot.command()
async def рейтинг(ctx, user = None):
    if check_is_muted(ctx.author.id): return
    if user == None:
        user = ctx.author
    if (user.id in players_rating):
        await ctx.send(f"твой рейтинг: {players_rating[ctx.author.id]}")
    else: await ctx.send("ТЫ ОХУЕЛ БЛЯТЬ???? ТЫ НЕ ИГРАЛ НИ РАЗУ")

@bot.command
async def хелп(ctx):
    if check_is_muted(ctx.author.id): return
    ctx.send()
    pass
    

@bot.command()
async def лидерборды(ctx):
    if check_is_muted(ctx.author.id): return
    lb = "```"
    for a in players_rating:
        user = await bot.fetch_user(a)
        lb += f"{user} : {players_rating[a]} \n"
    await ctx.send(lb + "```")

@bot.command()
async def база(ctx, count = 3):
    if check_is_muted(ctx.author.id): return
    res = "```"
    for i in range(1 , count + 1):
        res+=baza[random.randrange(1 , bazalen)] + ' '
    await ctx.send(res + '```')

class Player:
    def __init__(self, player, attemptsLeft):
        self.Number = random.randrange(1,11)
        self.Attempts = attemptsLeft
        self.Player = player
        self.id = player.id
        if self.Player.id not in players_rating:
            players_rating[self.Player.id] = 0
        self.Rating = players_rating[self.Player.id]
                    

bot.run(TOKEN)
