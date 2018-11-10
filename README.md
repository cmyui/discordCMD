## discordCMD.py

So essentially, I'm extremely new to python (and development as a whole, and I'd like to mess with discord's api for a while cuz i only sort of get it). Here are some things I'd like to make.
- Being able to recieve messages/send messages as a user
- Being able to basically have selfbot commands, except they dont actually send the message
- Being able to flip through servers aswell as private messages?

## Requirements
- Python
- Colorama 0.4.0
- Knowledge of how to edit a config. u can do it, i believe in u

## How to set up this thing
Alright if you ended up on this page you're probably retarded so heres this
```
$ git clone https://github.com/cmyui/discordCMD.git
```
Then rename your config sample to just config.ini
```
$ mv config.sample.ini config.ini
```
Next, configure the config (dw about true/false ok)
```
[default]
debug = 0
tokenauth = 1
important_servers: [2147, 483, 647]

[discord]
token = token here if tokenAuth = 1
username = username here (optional)
email = email here if tokenAuth = 0
password = password here if tokenAuth = 0
```
The default config should be pretty straight forward. If you're using a token to login to discord, make sure tokenauth is 1, and then just paste your token in. If you're using email/password, disable tokenauth and put the username and password in instead.
```
$ python3 discordcmd.py
```
