# OGU Bumper (Working  05/2024)

## Preview:

![alt text](images/preview.png)

## Modes:
[1] Bumps all threads from 'Market' section on user profile with 30 minutes interval.  
[2] Bumps all threads from links in threads.txt file every 30 minutes.  
[3] Spams random messages in thread by input link. Useful for farming awards during events.  

## Setup:

### Requirements
You need Python 3.10 or a newer Version to run your code.  
Make sure you have the latest version of Google Chrome installed.

### Python Modules
```
pip install selenium==4.12.0
pip install undetected-chromedriver
pip install randfacts
```

### Files
Enter your flipd username and password in config.py - if you have 2fa enter the code manually on login page.
If you want to use the Autobumper by links, put your links in options/threads.txt

## Usage

Execute the main.py script in your terminal and chose the option of your choice.  
After the browser opens, manually open https://oguser.com in a new tab and wait for cloudflare to finish.  
Resize the browser window to its minimum width and wait for flipd to open in the first tab.  
Keep the chrome window in focus, everything should work fine now.  
Youtube Tutorial: https://youtu.be/MnZKXP-j6Qo (Works the same since oguser.com rebranding)

## Help

If you need any help with the script feel free to reach out.  
Discord: edlzitrone    -    Telegram: @beamertaken - OGU: mf

