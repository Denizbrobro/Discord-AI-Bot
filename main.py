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
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(DBBS_text)
    await bot.change_presence(activity=discord.Game(name="Has Brain🧠"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Mesaj bot tarafından gönderildiyse, işlem yapma

    # Sadece belirli bir metin kanalında mesajları işle
    targetchannelid = canseeid  # Hedef metin kanalının ID'sini buraya ekleyin
    if message.channel.id != targetchannelid:
        return

    question = message.content
    
    try:
        # GPT-3.5-turbo-0125 modelini kullanarak bir yanıt oluştur
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        # Yanıtı al
        answer = response['choices'][0]['message']['content'].strip()

        # Cevabı Discord'a gönder
        await message.channel.send(answer)

    except openai.error.OpenAIError as e:
        await message.channel.send(f'Hata: {e.message}')


# Discord botunu çalıştır
bot.run(MCTOKEN)
