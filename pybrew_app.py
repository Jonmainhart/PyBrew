"""
PyBrew
Jonathan Mainhart
"""

import subprocess
import rumps

class PyBrew(object):
    """
    Pybrew class definition.
    """
    def __init__(self):
        self.config = {
            "app_name": "PyBrew",
            "update": "Update Homebrew",
            "upgrade": "Upgrade Homebrew",
            "list": "List Formulae and Casks"
        }
        self.app =rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.update_button = rumps.MenuItem(title=self.config["update"],
                                            callback=self.homebrew_action)
        self.upgrade_button = rumps.MenuItem(title=self.config["upgrade"],
                                            callback=self.homebrew_action)
        self.app.menu = [self.update_button, self.upgrade_button]

    def set_up_menu(self):
        """
        Sets up the menu
        """
        self.app.title = "🍺"

    def homebrew_action(self, sender):
        """
        Runs the selected command.
        """
        for key, value in self.config.items():
            if value == sender.title:
                cmd = f"brew {key}"
        
        msg = subprocess.run(cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    check=True)

        rumps.notification(title=self.config["app_name"], subtitle=f"{cmd}", message=msg.stdout)

    def run(self):
        """
        runs the app
        """
        self.app.run()
