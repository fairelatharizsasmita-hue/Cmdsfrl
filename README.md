# CMDSFRL 1.4

A custom command environment for Termux, featuring FRL Lang and FRL System Check.

## Requirements

- Android device
- Termux
- Python 3

## Installation Tutorial

### Step 1 - Download CMDSFRL

1. Open the CMDSFRL GitHub repository:
   https://github.com/fairelatharizsasmita-hue/Cmdsfrl
2. Tap Code.
3. Select Download ZIP.
4. Wait for the download to finish.

### Step 2 - Extract the ZIP

Extract the downloaded ZIP using your file manager.

### Step 3 - Open Termux

Give Termux storage access:

    termux-setup-storage

### Step 4 - Install Python

    pkg update
    pkg install python

### Step 5 - Install CMDSFRL Files

Navigate to the extracted project folder. Then run:

    mkdir -p ~/bin
    cp cmdsfrl frl_lang.py system_monitor.py ~/bin/
    chmod +x ~/bin/cmdsfrl

Make sure all three files are present:
- cmdsfrl
- frl_lang.py
- system_monitor.py

### Step 6 - Configure PATH

    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc

### Step 7 - Launch CMDSFRL

    cmdsfrl

## Features

- Custom Command Environment
- FRL Lang - Experimental scripting language
- FRL System Check - Displays basic system information

## FRL Lang Tutorial

Example:

    write "Hello World!"

- write - Displays text.
- ext - Exits FRL Lang.

## Project Status

- CMDSFRL 1.4: Development build
- FRL Lang: Experimental
- FRL System Check: Available
- Alpine Linux Port: Work in Progress

## Developer

Created by Fairel

---

Thanks for checking out CMDSFRL!

(yes i ask chatgpt for ts)
