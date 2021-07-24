# Main script which will start the minecraft server after, if needed the setup wizard.

import setup_wizard, start_minecraft
import os


if not os.path.isdir("Minecraft"):
    setup_wizard.Wizard()
start_minecraft.Minecraft()

