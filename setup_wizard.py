# The setup wizard for the Minecraft server.

import requests
import os
import shutil
import psutil
import sys
import socket
from threading import Thread
from time import sleep
from subprocess import Popen


class Wizard:
    # Starts the setup of the Minecraft server
    def __init__(self):
        os.system("clear")
        print("Welcome to the server setup.\n"
              "This tool will guide you to get your Minecraft server running.")
        self.setup_minecraft_server()
        os.system("clear")
        if os.path.isdir("Minecraft"):
            print("WARNING! You seem to already have a server in the Minecraft directory! \n"
                  "If you continue, you'll wipe the entire server, including worlds!")
            while True:
                choice = input("Do you want to continue? ['y','n']:")
                if choice == "y":
                    print("Please enter 'yy' if you want to delete the server.")
                elif choice == "yy":
                    print("Continuing.")
                    os.system("clear")
                    break
                else:
                    print("Stopping the Minecraft server setup.")
                    exit(1)
        print("Installing Minecraft server.")
        print("How do you want to install the server?\n"
              "[1] Download a paper server\n"
              "[2] Enter download link for given server")
        choice = self._get_choice("12")
        os.system("clear")
        if os.path.isdir("Minecraft"):
            shutil.rmtree("Minecraft")
        if choice == "1":
            self.download_paper()
        elif choice == "2":
            self.download_from_link()
        os.system("clear")
        Popen(["./start.sh"], cwd="Minecraft", shell=True).wait()
        os.system("clear")
        open("Minecraft/eula.txt", "w").write("eula=true")
        print("Do you want to edit server.properties?")
        if self._get_choice("yn") == "y":
            os.system("nano Minecraft/server.properties")
        os.system("clear")

    # Asks something to the user with allowed answers
    def _get_choice(self, allowed_values: str):
        allowed_values = [char for char in allowed_values]
        while True:
            choice = input(str(allowed_values) + ":")
            if choice in allowed_values:
                return choice
            else:
                print("Invalid input.")

    # Download a minecraft server jar from a link given by the user.
    def download_from_link(self):
        while True:
            link = input("Download link? (This should end with .jar) ")
            if link.endswith(".jar"):
                try:
                    r = requests.get(link)
                    if not r.ok:
                        print("Whoops, we couldn't download that. Please verify the URL is right.")
                        continue
                    os.mkdir("Minecraft")
                    open('Minecraft/server.jar', 'wb').write(r.content)
                    self.set_ram()
                    break
                except requests.exceptions.MissingSchema:
                    print("The URL should start with https:// or http://.")
                except requests.exceptions.ConnectionError:
                    print("Whoops, we couldn't download that. Please verify the URL is right.")
            else:
                print("invalid link.")

    # Dialog to easily download paper server.
    def download_paper(self):
        print("Downloading paper server.")
        r = requests.get("https://papermc.io/api/v2/projects/paper")
        versions = r.json()["versions"]
        version_groups = r.json()["version_groups"]
        chosen_version = input("Please enter a Minecraft version. Latest is " + versions[-1] + ". ")
        if chosen_version == "":
            chosen_version = versions[-1]
        while not(chosen_version in versions or chosen_version in version_groups):
            print("Oops, this version doesn't seem like it'_s supported by paper. The available versions are:\n"
                  + str(versions))
            chosen_version = input("Please enter a Minecraft version. ")
            if chosen_version == "":
                chosen_version = versions[-1]
        r = requests.get("https://papermc.io/api/v2/projects/paper/versions/" + chosen_version)
        latest_build = str(r.json()["builds"][-1])
        print("Downloading paper build " + latest_build + "...")
        r = requests.get("https://papermc.io/api/v2/projects/paper/versions/" + chosen_version + "/builds/"
                         + latest_build + "/downloads/paper-" + chosen_version + "-" + latest_build + ".jar")
        os.mkdir("Minecraft")
        open('Minecraft/server.jar', 'wb').write(r.content)
        self.set_ram()

    # Asks how much ram the user wants to give to the minecraft server and creates start.sh executable.
    def set_ram(self):
        os.system("clear")
        while True:
            gigs = int(input("How much RAM do you want to allocate to your minecraft server? (in Gb)"))
            if gigs > psutil.virtual_memory().total / 1000000000:
                print("You don't have that much RAM!")
            elif gigs > psutil.virtual_memory().available / 1000000000:
                print("Currently there'_s not that much memory available. Do you want to continue anyway? (available: "
                      + str(int(psutil.virtual_memory().available / 1000000000)) + "Gb)")
                if self._get_choice("yn") == "y":
                    break
            else:
                break
        gigs_str = str(gigs)
        open('Minecraft/start.sh', 'w').write("java -Xmx" + gigs_str + "G -Xms" + gigs_str + "G -jar server.jar nogui")
        os.system("chmod +x Minecraft/start.sh")