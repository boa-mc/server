# server
The core for your Minecraft server that can then be controlled by multiple nodes like a website or a Discord bot.

## Dependencies
`java --version` must show the right Java version for the Minecraft server you want to install.


## Installing
> :warning: Remember: mc-server-tools is meant to be run on ubuntu server.

Run the following commands:
```bash
git clone https://github.com/mc-server-tools/server/
cd server
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
