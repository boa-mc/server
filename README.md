# Boa-mc
Boa-mc is a tool that allows you to control a minecraft server from a discord bot and a (very minimal) control panel.

# server
The core for your Minecraft server that can then be controlled by multiple nodes: a website or a Discord bot.

## Dependencies
- java
- python3

`java --version` must show the right Java version for the Minecraft server you want to install.


## Installing

Run the following commands:
```bash
git clone https://github.com/boa-mc/server/
cd server
pip3 install -r requirements.txt
python3 main.py
```
You will need to enter a Minecraft version.
After the setup, the server will automatically start and display its hostname.

If you want to re-setup the server, use:
```bash
python3 main.py -s
```

## Starting
To start the server afterwards, use
```bash
python3 main.py
```
If you want to be able to log out of the ssh session while letting the server run, you can use [screen](https://help.ubuntu.com/community/Screen).

Now, you can install nodes, like [the web control panel](https://github.com/boa-mc/website) or [the discord bot](https://github.com/boa-mc/discord)
