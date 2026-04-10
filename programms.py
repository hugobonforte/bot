import discord # type: ignore
# Importamos la función desde tu archivo bot_logic.py
from bot_logic import gen_pass 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'- Botinsano encendido con prefijo "¡" como {client.user} -')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    # --- NUEVO COMANDO CON "+" ---
    if msg.startswith('¡pass'):
        # Generamos la contraseña de 10 caracteres usando tu lógica
        password_generada = gen_pass(10)
        await message.channel.send(f"🔑 Tu contraseña segura es: `{password_generada}`")

    # También podemos cambiar el saludo a "+" si quieres
    elif msg.startswith('¡hello'):
        await message.channel.send("¡Qué onda! Ahora respondo a los comandos con el signo ¡ 😎")

# Tu Token de Discord
client.run("tu token")
