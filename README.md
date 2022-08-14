# Shellbot for Discord

* Under rewriting source to executing command in Docker Container, so spaghetti here.

### What does it

Get quick *Linux shell* experience on your Discord server(s) and DM.

### It needs

Python 3.8+ \
Discord.py (`pip install git+https://github.com/Rapptz/discord.py`)

### Just run it yours

1. Clone this repository.
1. Go [here](https://discord.com/developers/applications) and create your own discord application and get `client id` and `bot token`.
1. Create `config.json`. See `config.json.example` for more info.
1. Run `pip install -r requirements.txt` to satisfy dependency.
1. Run `python3 bot.py`.
1. Let's send commands. Have fun. *Don't forget invite your bot to your server.*

### Usage

Mention to bot with command. codeblock-quoted are optional. \
example:
@shellbot#0001 ```echo Hello world!```

### DANGEROUS

* Keep your safe. We recommeded to run in virtual environment or machine only use to this bot.
* Because all of commands will *directly* running in SHELL, make sure bot-running user is in JAILED environment. (if user is not in jailed environment, your operating system will UNDER ATTACKED by MALICIOUS USER)
* ALL OF THIS IS EXPERIMENT. USE THIS AT YOUR OWN RISK.
