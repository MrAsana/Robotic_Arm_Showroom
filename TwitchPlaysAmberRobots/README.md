# Twitch Plays Amber Robots


File has been modified to work with Amber Robotic Arms

The following description comes from https://github.com/DougDougGithub/TwitchPlays

Sincere thanks to `DougDougGithub`. 

> These are the three Python files I use that allows Twitch Chat or Youtube Chat to control your keyboard or mouse to play a game. You are welcome to use or adapt this code for your own content.
>
> To run the code you will need to install Python 3.9.  
> Additionally, you will need to install the following python modules using Pip:  
>
> ```bash
> python -m pip install keyboard  
> python -m pip install pydirectinput  
> python -m pip install pyautogui  
> python -m pip install pynput  
> python -m pip install requests  
> ```
>
> Once Python is set up, simply change the Twitch username (or Youtube channel ID) in TwitchPlays_TEMPLATE.py, and you'll be ready to go.
>
> This code is originally based off Wituz's Twitch Plays template, then expanded by DougDoug and DDarknut with help from Ottomated for the Youtube side. For now I am not reviewing any pull requests or code changes, this code is meant to be a simple prototype that is uploaded for educational purposes. But feel free to fork the project and create your own version!

For robotic arm users you need to change settings in `TwitchPlays_amber.py`

```
##################### ROBOT VARIABLES #####################
IP_ADDR ="127.0.0.1" # The IP address of your robotic arm host
port = 26001 # The port of your robotic arm host
SENSITIVE = 0.05 # The distance moved by each command
```

At the same time, in order to correctly receive live broadcast information, you need to change settings in `GAME VARIABLES` and `MESSAGE QUEUE VARIABLES`

Thanks to DougDougGithub, these are well commented in the file.



This project was completed relatively early and has not been tested in detail

