# Main script which will start the minecraft server after, if needed, the setup wizard.

import setup_wizard
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='The mc-server-tools Minecraft server.')
parser.add_argument('-s', '--setup', action="store_true")
args = parser.parse_args()

if not os.path.isdir("Minecraft") or args.setup is True:
    setup_wizard.Wizard()


import start_minecraft