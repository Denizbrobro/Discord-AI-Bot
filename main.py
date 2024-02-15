import discord
import pyfiglet
from discord.ext import commands
import openai
from config import *

# OpenAI API Key
openai.api_key = openapikey

DBBS_text = pyfiglet.figlet_format(text="Denizbrobro ------------ STUDIOS")

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

# Create discord bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(DBBS_text)
    await bot.change_presence(activity=discord.Game(name="Has Brain🧠"))

@bot.command(name='ask')
async def ask(ctx, *args):
    question = ' '.join(args)

    try:
        # Generate a response using the GPT-3.5-turbo-0125 model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        # Get the response
        answer = response['choices'][0]['message']['content'].strip()

        # Send the answer to Discord
        await ctx.send(answer)

    except openai.error.InvalidRequestError as e:
        # Access the error message using the __str__ method
        await ctx.send(f'Error: {e}')

    except openai.error.OpenAIError as e:
        await ctx.send(f'Error: {e}')

# Run the Discord bot
bot.run(TOKEN)
