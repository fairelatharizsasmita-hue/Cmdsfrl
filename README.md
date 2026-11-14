CMDSFRL Alpha 1.3

A custom command environment for Termux, featuring FRL Lang.

Requirements

- Android device
- Termux
- Python 3

Installation Tutorial

Step 1 — Download CMDSFRL

1. Open the "CMDSFRL GitHub repository" (https://github.com/fairelatharizsasmita-hue/Cmdsfrl.1.3).
2. Tap Code.
3. Select Download ZIP.
4. Wait for the download to finish.

Step 2 — Extract the ZIP

Extract the downloaded ZIP using your file manager.

Step 3 — Open Termux

Give Termux storage access:

termux-setup-storage

Step 4 — Install Python

pkg update
pkg install python

Step 5 — Install CMDSFRL files

Navigate to the extracted project folder. Then run:

mkdir -p ~/bin
cp cmdsfrl frl_lang.py ~/bin/
chmod +x ~/bin/cmdsfrl

Step 6 — Configure PATH

Add "~/bin" to PATH if it is not already configured:

echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

Step 7 — Launch CMDSFRL

Now run:

cmdsfrl

Note: The "cmdsfrl" file is an executable Python launcher without a ".py" extension. "frl_lang.py" is its Python module.

FRL Lang Tutorial

Example:

write "Hello World!"

- "write" — displays text.
- "exit" — exits FRL Lang.

Project Status

- CMDSFRL Alpha 1.3: Development build
- FRL Lang: Experimental
- Alpine Linux Port: Work in Progress

Developer

Created by Fairel

---

Thanks for checking out CMDSFRL!
(yes i ask chatgpt for ts)
