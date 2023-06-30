# This example requires the 'message_content' privileged intents

import osimport nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix="++", intents=nextcord.Intents.all())

@bot.event
async def on_message(message):
    if message.channel.id == 1068789575020986418:
        await message.add_reaction('💪')

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Men on self improvement"))
    print("Bot online!")

@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),commands.has_permissions(ban_members=True))
async def ban(ctx, user: nextcord.User, *, message=None):
    try:
        dm = await user.create_dm()
        await dm.send("You were Banned from men's training zone" + message)
    finally:
        await ctx.guild.ban(user)
    embedVar = nextcord.Embed(title="Member banned")
    embedVar.add_field(name="User: ", value=user, inline=False)
    embedVar.add_field(name="Action", value="was banned", inline=False)
    await ctx.send(embed=embedVar)

@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),commands.has_permissions(ban_members=True))
async def kick(ctx, user: nextcord.User, *, message=None):
    try:
        dm = await user.create_dm()
        await dm.send("You were Kicked from men's training zone" + message)
    finally:
        await ctx.guild.kick(user)
    embedVar = nextcord.Embed(title="Member kicked")
    embedVar.add_field(name="User: ", value=user, inline=False)
    embedVar.add_field(name="Action", value="was kicked", inline=False)
    await ctx.send(embed=embedVar)

@bot.command(pass_context=True)
@commands.check_any(commands.is_owner(),commands.has_permissions(ban_members=True))
async def send(ctx, *, message=None):
    await ctx.send(message)



bot.run(os.environ["DISCORD_TOKEN"])
