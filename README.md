# CyberDoge

![LOGO](https://github.com/AaronPhilips101/CyberDoge/blob/main/logo.png?raw=true)


## Disclaimer

```
///
    I am in no way responsible if your account gets banned due to improper
    use of the bot.
    So proceed at your own risk and use the bot wisely.
///
```


## Requirements

- openssl

```
pkg install openssl
```

- git

```
pkg install git
```

- python

```
pkg install python
```

- telethon

```
pip install telethon
```

- virtualenv

```
pip install virtualenv
```

## Connecting to your Telegram Account

```
git clone https://github.com/AaronPhilips101/CyberDoge
cd CyberDoge
python3 -m session
```

-1. Run above code in terminal or termux app (if on android)
-2. Enter APP ID, API HASH and phone number conntected to your telegram account

- **How to get app id and hash?
-   *Go to https://my.telegram.org
-   *After logging in click on "Api Development Tools" and fill the form
-   *After filling it and submitting you will get your app id and hash on the screen, just copy it and follow the remaining steps.

-3. Enter login code and/or password
-4. Copy the session and continue to installation

## Installing

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AaronPhilips101/CyberDoge/tree/heroku)

- Hit the "Deploy to Heroku" button and enter APP ID, API HASH and phone number conntected to your telegram account
- Enter the session copied while connecting your telegram account
- Click on the "Deploy" button on the next page
- After the process is completed, click on "View app"
- Now click on the "Resources" tab
- Then click on the edit/pencil icon
- Finally toggle the switch and hit confirm
- Your bot is now up and running!
- Send .alive in any chat to test it

#### The Legacy Way

- Enter APP ID, API HASH, SESSION in production.py
- Run the code given below in terminal
- After the process is completed, try running .alive on telegram

```
git clone https://github.com/AaronPhilips101/CyberDoge
cd CyberDoge
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m CyberDoge
```

## Read the docs

Here are the most useful "global" variables that can be used on any module you create:

- ENV: A global object which allows access to enviroment variables defined in env.py
- client: A modified version of the telegram client.
- client.storage: A global storage object for the current session.
- events: A simple function that returns a events.NewMessage object.
- progress: Generic progress callback for both uploads and downloads.
- time_formatter: Input time in milliseconds, to get beautified time, as string.
- humanbytes: Input size in bytes, outputs in a human readable format.
- You can learn alot just by reading the telethon [documentory](https://docs.telethon.dev/en/latest/)
- Here is a simple module that adds " world" to the message if you send ".hello".

```
@client.on(events("hello"))
async def handler(event):
	await event.edit(event.text[1:] + " world.")
```


## Credits
- [The-TG-Bot-V3](https://github.com/justaprudev/The-TG-Bot) (For modules)
- [Telethon](https://github.com/LonamiWebs/Telethon) (The Core) 
- [Uniborg](https://github.com/SpEcHiDe/UniBorg) 
- [FTG modules repo](https://github.com/friendly-telegram/modules-repo)
- [Userge modules repo](https://github.com/UsergeTeam/Userge-Plugins) (For modules)
- [PPE](https://github.com/RaphielGang/Telegram-Paperplane)
