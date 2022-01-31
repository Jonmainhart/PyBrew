# PyBrew
Simple menubar application to update and upgrade Homebrew for MacOS written in Python

## Requirements
rumps
`python3 -m pip install rumps`

## Who is this for?
This is for anyone who wants to update and upgrade Homebrew from the comfort of the menubar.

## How it Works
PyBrew uses the [rumps](https://github.com/jaredks/rumps) framework and the [subprocess](https://docs.python.org/3/library/subprocess.html) module to display a menubar application that will run `brew update` and `brew upgrade` commands when selected from the menu. The application will then display a notifiaction banner when the process is complete.

## Installation
Download `__main__.py` `pybrew_app.py` and `assets` along with it's contents and place them in a project folder named "pybrew".

## Launch
`python3 pybrew`

Thank you for reading.
