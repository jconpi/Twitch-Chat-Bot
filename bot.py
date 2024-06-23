import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(
    token=os.environ['token'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# Comando !hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

# Comando !repeat <message>
@bot.command(name='repeat')
async def repeat(ctx):
    # Obtiene el mensaje después del comando
    message = ctx.message.content[len(ctx.prefix + ctx.command.name) + 1:]
    await ctx.send(message)

# Comando !dice
import random
@bot.command(name='dice')
async def dice(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f'{ctx.author.name} rolled a {roll}')


# Comando !uptime
@bot.command(name='uptime')
async def uptime(ctx):
    user = await bot.fetch_users(names=[os.getenv('CHANNEL')])
    user = user[0]
    stream = await bot.fetch_streams(user_ids=[user.id])
    if stream:
        uptime = stream[0].uptime()
        await ctx.send(f'The stream has been live for {uptime}')
    else:
        await ctx.send('The stream is not currently live.')

# Comando !game
@bot.command(name='game')
async def game(ctx):
    user = await bot.fetch_users(names=[os.getenv('CHANNEL')])
    user = user[0]
    stream = await bot.fetch_streams(user_ids=[user.id])
    if stream:
        game = stream[0].game_name
        await ctx.send(f'The channel is currently streaming {game}.')
    else:
        await ctx.send('The stream is not currently live.')

# Comando !title
@bot.command(name='title')
async def title(ctx):
    user = await bot.fetch_users(names=[os.getenv('CHANNEL')])
    user = user[0]
    stream = await bot.fetch_streams(user_ids=[user.id])
    if stream:
        title = stream[0].title
        await ctx.send(f'The current stream title is "{title}".')
    else:
        await ctx.send('The stream is not currently live.')

# Comando !shoutout <user>
@bot.command(name='shoutout')
async def shoutout(ctx):
    if len(ctx.message.content.split()) > 1:
        user_to_shout = ctx.message.content.split()[1]
        await ctx.send(f'Shoutout to {user_to_shout}! Check out their channel at https://twitch.tv/{user_to_shout}')
    else:
        await ctx.send('Please provide a user to shoutout.')

# Comando !8ball <question>
@bot.command(name='8ball')
async def eight_ball(ctx):
    responses = ["Yes", "No", "Maybe", "Definitely", "Absolutely not", "Ask again later"]
    question = ctx.message.content[len(ctx.prefix + ctx.command.name) + 1:]
    if question:
        response = random.choice(responses)
        await ctx.send(f'Question: {question}\nAnswer: {response}')
    else:
        await ctx.send('Please ask a question.')

# Comando !quote
quotes = [
    "To be, or not to be, that is the question.",
    "I think, therefore I am.",
    "The only thing we have to fear is fear itself.",
    "That's one small step for man, one giant leap for mankind."
]

@bot.command(name='quote')
async def quote(ctx):
    quote = random.choice(quotes)
    await ctx.send(quote)

# Comando !addquote <quote>
@bot.command(name='addquote')
async def addquote(ctx):
    new_quote = ctx.message.content[len(ctx.prefix + ctx.command.name) + 1:]
    if new_quote:
        quotes.append(new_quote)
        await ctx.send('Quote added!')
    else:
        await ctx.send('Please provide a quote to add.')

if __name__ == "__main__":
    bot.run()