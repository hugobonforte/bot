import discord

from bot_logic import gen_pass 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- Botinsano encendido con prefijo "+" como {client.user} ---')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith('+pass'):
 
        password_generada = gen_pass(10)
        await message.channel.send(f"🔑 Tu contraseña segura es: `{password_generada}`")

 
    elif msg.startswith('+hello'):
        await message.channel.send("¡Qué onda! Ahora respondo a los comandos con el signo + 😎")
      
client.run("MTQ4Njg5ODUwNjk5MDg3ODc2MA.GZul4u.qxpu3JWcqVpiqFOH0zhtk3g4Fo4VepqjNvyk4U")
