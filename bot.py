# encoding: utf-8
import json
import discord
import os
import sys
import subprocess
import asyncio
from datetime import datetime

# setup
homedir = r'' + os.getenv('HOME')
cmdargs = sys.argv
with open(cmdargs[1], encoding='utf-8') as file:
    config = json.load(file)

def truncate(string, length, ellipsis='...'):
    return string[:length] + (ellipsis if string[length:] else '')

class Client(discord.Client):
    async def on_ready(self):
        print('[ OK ] Shellbot started')
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(f'<@{self.user.id}> '):
            command = message.content.replace(f'<@{self.user.id}>', '').strip().strip('```')

            print(f'[EXEC] @{message.author}: {command}')

            embed = discord.Embed(title='Run')
            embed.set_author(name='Shellbot', url='https://github.com/libnumafly/Shellbot')
            embed.set_footer(text='Shellbot commit ' + commitlabel)
            try:
                response = subprocess.run(command, shell=True, check=True, cwd=homedir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
                embed.colour = discord.Colour.green()
                embed.add_field(name='StdOut', value=f'```{truncate(response.stdout.decode(), 1015)}```')
                embed.add_field(name='ExitCode', value=response.returncode, inline=True)
                embed.add_field(name='Status', value='Complete')
            except subprocess.CalledProcessError as response:
                embed.colour = discord.Colour.red()
                embed.add_field(name='StdOut', value=f'```{truncate(response.stderr.decode(), 1015)}```')
                embed.add_field(name='ExitCode', value=response.returncode, inline=True)
                embed.add_field(name='Status', value='Error')
            except subprocess.TimeoutExpired as response:
                embed.colour = discord.Colour.red()
                embed.add_field(name='StdOut', value=f'```{truncate(response.stderr.decode(), 1015)}```')
                embed.add_field(name='Status', value='Timeout')

            embed.timestamp = datetime.now()
            await message.channel.send(embed=embed)

if __name__ == '__main__':
    commitlabel = subprocess.check_output(["git", "describe", "--always"]).strip().decode()
    print(f'[INFO] Shellbot commit {commitlabel}')
    print('[LOAD] Starting Shellbot...')
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    client.run(config['token'])
