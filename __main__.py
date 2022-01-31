"""
PyBrew
Jonathan Mainhart
29 January 2022

Simple menu-bar application to run homebrew update and upgrade commands
"""


import pybrew_app

if __name__ == '__main__':
    app = pybrew_app.PyBrew()
    app.run()
