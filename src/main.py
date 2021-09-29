import os
import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    pass_context = True,
    members=True,
    guilds=True,
    presences=True
)

bot.author_id = 307924849580441612  # Change to your discord id!!!


@bot.command(name='name')
async def returnName(ctx):
        await ctx.send(ctx.message.author)
   
@bot.command(name='count')
async def getStatus(ctx):
    await ctx.send(getStatus(ctx))

@bot.command(name='admin')
async def createAdminRole(ctx, userName: discord.User):
    await ctx.guild.create_role(name = "Admin")
    role = discord.utils.get(ctx.guild.roles, name = "Admin")
    userRoles = userName.roles
    await userName.edit(roles = userRoles+ [role])
    
    

def getStatus(ctx):
    memberList = []
    for member in bot.guild.members:
        memberTmp = member.name, member.status
        print(memberTmp)
        memberList.append(memberTmp)
    return memberList


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = ""
bot.run(token)  # Starts the bot