# Crash Bandicoot Discord Bot
Discord bot that generates responses using PALM api. With Crash Bandicoot personality.

# Getting Started
Install python dependencies (Debian/Ubuntu):
```
sudo apt install python3 python3-pip python3-venv python-is-python3 build-essential
```

Create virtual environment:
```
python3 -m venv venv
```

Activate virtual environment:
```
source venv/bin/activate
```

## Install dependencies
Before you begin, you need to install the dependencies. You can do this by running:
```
cd ./crashbot-palm
pip install -r requirements.txt
```

Because `py-cord` installs `discord.py` unintentionally as a dependency, you need to manually uninstall it and reinstall `py-cord`:
```
pip uninstall discord.py
pip install py-cord
```

If you encounter any errors, reinstall `py-cord`

# Creating a bot
In order to power this bot, you need to have two tokens. One for the bot itself, and one for the PALM API.
You can obtain a bot token using [Discord Developer Portal](https://www.pythondiscord.com/pages/guides/pydis-guides/contributing/setting-test-server-and-bot-account/#:~:text=Go%20to%20the%20Discord%20Developers%20Portal.%20Click%20on,get%20your%20Bot%20Token%20with%20the%20Copy%20button.).

After you create an app which also contains the bot, you can get its invite link through "OAuth2" and "URL Generator" section. Tick "bot" and set appropriate permissions. Then copy the link and paste it into your browser. You can invite the bot to your server.

**This bot requires atleast Send Messages, Read Message History, and Embed Links permissions!!!!**

# Obtaining tokens
On the project's root containing the `main.py` file, you need to have `dev.env` file which stores the token credentials both for bot and palm api

```
TOKEN=<your discord bot token>
PALM_API_TOKEN=<palm api token>
```

You need to obtain PALM api token/key through https://developers.generativeai.google/tutorials/setup

# Running the bot
`python main.py`
