import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

embedcolor = 0x0070ff
embedthumb = "https://cdn.dribbble.com/users/5242374/screenshots/16641455/media/0a74ea6b1d505b316ced8be139175fc3.gif"

logschannelid = 1234

@bot.event
async def on_member_ban(guild, user):
    log_channel = bot.get_channel(logschannelid)

    log_embed = discord.Embed(title='User Banned', color=embedcolor)
    log_embed.add_field(name='User', value=f'{user.name}#{user.discriminator}')
    log_embed.set_thumbnail(url=user.avatar_url)

    await log_channel.send(embed=log_embed)

@bot.event
async def on_member_remove(user):
    log_channel = bot.get_channel(logschannelid)

    log_embed = discord.Embed(title='User Kicked', color=embedcolor)
    log_embed.add_field(name='User', value=f'{user.name}#{user.discriminator}')
    log_embed.set_thumbnail(url=user.avatar_url)

    await log_channel.send(embed=log_embed)

@bot.slash_command(name='ping', description='Whats my ping?')
async def ping(ctx):
    latency = bot.latency * 1000

    embed = discord.Embed(title="Ping Info:", color=embedcolor)
    embed.add_field(name="Bot Ping:", value=f"```{latency}```", inline=True)
    embed.add_field(name="Frotnite Api Ping:", value=f"```69```", inline=True)
    embed.set_thumbnail(url=embedthumb)
    embed.set_footer(text=f"Slash Bot Example - Made By chikn")

    await ctx.send(embed=embed)

@bot.slash_command(name='ban', description='Ban a user from the server!')
async def ban_user(ctx, user: discord.User, reason: str = 'No reason provided.'):
    if ctx.author.guild_permissions.ban_members:
        await user.ban(reason=reason)

        embed = discord.Embed(title=f"{user} Has Been Banned", color=embedcolor)
        embed.set_image(url="https://thumbs.gfycat.com/BlondDamagedCreature-size_restricted.gif")
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'You Dont Have Permission To Use That Command!', color=0xFF0000)
        embed.set_thumbnail(url=embedthumb)
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")
        await ctx.send(embed=embed)

@bot.slash_command(name='kick', description='Kick a user from the server!')
async def kick_user(ctx, user: discord.User, reason: str = 'No reason provided.'):
    if ctx.author.guild_permissions.kick_members:
        await user.kick(reason=reason)

        embed = discord.Embed(title=f'{user} Has Been Kicked', color=embedcolor)
        embed.set_image(url='https://media0.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif')
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'You Dont Have Permission To Use That Command!', color=0xFF0000)
        embed.set_thumbnail(url=embedthumb)
        embed.set_footer(text=f"Slash Bot Example - Made By chikn")
        await ctx.send(embed=embed)

bot.run('')