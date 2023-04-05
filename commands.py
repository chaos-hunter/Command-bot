import discord
from discord.ext import commands

# from b.reaction import client

bot = commands.Bot(command_prefix='!')
client = discord.Client()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def comment(ctx, arg):
    await ctx.send(f'You look terrible{arg}')


@bot.command()
async def double_comment(ctx, arg1, arg2):
    await ctx.send(f'{arg1} and {arg2} You should be twins')


@bot.command()
async def expose(ctx, *args):
    everyone = ' , '.join(args)
    await ctx.send(f'{everyone} are all in trouble')


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')


@bot.command()
async def regulate(ctx, arg):
    await ctx.send(f'{arg} refer to the image below')
    with open(r'C:\Users\David.Entonu\Downloads\captain.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.channel.send(file=picture)

@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await ctx.add_roles(member, role)
        embed = discord.Embed(title="User Muted!",
                              description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
                              color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.",
                              color=0xff00f6)
        await ctx.send(embed=embed)


bot.run('Token goes here')
