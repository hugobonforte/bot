 #Son los imports necesarios para el funcionamiento del bot.
import discord
import os
from discord.ext import commands
from datos import residuos
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='¡', intents=intents)
# Este comando sirve para que el bot responda con la categoría de residuo a la que pertenece un residuo específico que el usuario le da al bot.
@bot.command()
async def residuo(ctx, *, nombre):
    nombre = nombre.lower()
    if nombre in residuos:
        await ctx.send(f"🔍 **{nombre}** → {residuos[nombre]}"
    else:
        await ctx.send(
            f"🤔 No sé qué hacer con **{nombre}**.\n"
            "Pregunta a un experto o revisa normas locales."
        )
# Este evento se ejecuta cuando el bot se conecta a Discord. Imprime un mensaje en la consola indicando que el bot ha iniciado sesión correctamente.    
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
# Este comando sirve para que el bot responda con un mensaje de saludo cada vez que se ejecute el comando "hola".
@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
# Este comando sirve para repetir la palabra "he" un número de veces que el usuario le da al bot, y el bot responderá con la palabra "he" repetida ese número de veces.
@bot.command()
async def heh(ctx, count_he = 5):
    await ctx.send("he" * count_he)
# Este comando sirve para dar la bienvenida a los usuarios a la escuela de kodland.
@bot.command()
async def kodland(ctx, count_he = 5):
    await ctx.send("Bienvenido a la escuela de kodland")
# Este comando sirve para sumar dos números enteros que el usuario le da al bot, y el bot responderá con la suma de esos números.
@bot.command()
async def suma(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
# Este comando sirve para elegir entre varias opciones que el usuario le da al bot, y el bot responderá con una de esas opciones de forma aleatoria.
@bot.command(description='For when you wanna settle the score some other way')
async def escoge(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
 # Este comando sirve para enviar una imagen aleatoria de la carpeta "images" cada vez que se ejecute el comando.
@bot.command()
async def memepy(ctx):
    imagenes = os.listdir('images')
    imagen = random.choice(imagenes)
    with open('images/' + imagen, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
# Este comando sirve para enviar una imagen aleatoria de la carpeta "image" cada vez que se ejecute el comando.
@bot.command()
async def meme(ctx):
    imagenes = os.listdir('image')
    imagen = random.choice(imagenes)
    with open('image/' + imagen, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
# Tu Token de Discord
bot.run("Tu token")
