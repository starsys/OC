# MacGyver Maze Game 2018

Maze game based on MacGyver world.
Written in Python by Théophile Guettier
theophile.guettier@gmail.com

## Prerequisite : 
- python3 (3.6 or 3.7) must be installed on your machine

Install:
- Unpack all files from GitHub on your machine.
- From this unpack folder, 
run "pip install -r requirements.txt" in your terminal.
This will install all required modules

## Launch:
- launch main.py  
just write "/path/of/your/.py/file/python3 main.py" 
into your terminal and press "enter"
(depending of PATH you may type "python" or "python3")

## How to Launch in virtual machine 
(Valid fo mac or linux. For windows: use powershell instead):
- launch in your terminal: "pyton –m pip install –upgrade pip" (to upgrade pip)  
- then install virtualenv: "pip install virtualenv"  
- go into the path you want your virtualenv to be created  
("cd /path/of/your/.py/file")  
- create your virtualenv: "virtualenv -p python3 env" (or "python")
- activate your virtualenv: "source env/bin/activate"  
- install dependencies: "pip install -r requirements.txt"  
- deactivate your virtualenv when finished: "deactivate"  

## This game uses "maze.txt" file to generate maze.
You can edit it to and create your own maze.
Each character of the maze.txt file symbolize blocks :
"S" = maze start
"A" = maze arrival
"W" = maze wall
"P" = maze path
Only first occurrence of "S" and "A" from upper left
of the file will be taken into account.

## Usage:
- use direction keys of your keyboards to move Macgyver
- collect all items (aiguille, ether and tube)
- meet the "bad guy" to defeat him
You can press escape key anytime to quit the game
When finished, press enter to start a new game.
