# chaster_discord_bot.py
# Basic Discord bot for Ma'am's Chaster control

import os
import discord
from dotenv import load_dotenv
import requests
import asyncio

from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHASTER_TOKEN = os.getenv('CHASTER_TOKEN')
LOCK_ID = '6a08b0e5fef2827dcda0a97b'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Maam\'s Chaster Control Bot is ready!')

@bot.command(name='status')
async def status(ctx):
    """Check current lock status"""
    await ctx.send('🔄 Fetching live lock status...')
    try:
        headers = {'Authorization': f'Bearer {CHASTER_TOKEN}'}
        response = requests.get(f'https://api.chaster.app/locks/{LOCK_ID}', headers=headers)
        if response.status_code == 200:
            data = response.json()
            # Simple status message
            await ctx.send(f'**Lock Status**\nID: {LOCK_ID}\nRemaining: {data.get("remaining_time", "N/A")}')
        else:
            await ctx.send(f'Error: {response.status_code} - {response.text}')
    except Exception as e:
        await ctx.send(f'Error fetching status: {str(e)}')

@bot.command(name='addtime')
async def add_time(ctx, minutes: int):
    """Add time to the lock: !addtime 30"""
    await ctx.send(f'Adding {minutes} minutes...')
    try:
        headers = {'Authorization': f'Bearer {CHASTER_TOKEN}'}
        payload = {'duration': minutes * 60}
        response = requests.post(f'https://api.chaster.app/locks/{LOCK_ID}/add-time', json=payload, headers=headers)
        if response.status_code == 200:
            await ctx.send(f'✅ Added {minutes} minutes!')
        else:
            await ctx.send(f'❌ Error: {response.status_code}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

@bot.command(name='freeze')
async def freeze(ctx):
    """Freeze the lock"""
    await ctx.send('Freezing lock...')
    # Add actual freeze logic here later
    await ctx.send('✅ Lock frozen (placeholder)')

bot.run(TOKEN)
