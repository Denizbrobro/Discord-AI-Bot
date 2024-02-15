import discord
import pyfiglet
from discord.ext import commands
import openai
from config import *
from discord.interactions import Interaction

# OpenAI API Key
openai.api_key = openapikey

DBBS_text = pyfiglet.figlet_format(text="Denizbrobro ------------ STUDIOS")
print(DBBS_text)

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

# Create discord bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.tree.command(name="ask", description="If you have a problem, ask the artificial intelligence")
async def search(interaction: discord.Interaction, question: str):
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
        print("There is a message")
        await interaction.response.send_message(answer)

    except openai.error.OpenAIError as e:
        print(f'Error: {e.message}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="/help"))
    try:
        synced = await bot.tree.sync()
        print(f"Currently, there are {len(synced)} executable commands.")
        print(pyfiglet.figlet_format(text="Confirmed"))
    except Exception as e:
        print("There is an issue with the bot. Please check the bot. Urgent.", e)
        print(pyfiglet.figlet_format(text="Not Confirmed"))

# Run the Discord bot
bot.run(TOKEN)
