import discord
import asyncio
import configparser

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # Our little list of possibilities..
    actionDesired = input("""\nWhat would you like to do today?
                            \n1. Check a users permissions
                            \n2. Post a message as the user
                            \n3. DOX User (Currently Disabled)
                            \n4. Check bans in a specific server
                            \n5. Check all bans the user can see
                            \n6. cmyuiDiscord (Beta as fuck)
                            \n>> """)

    if actionDesired.find("1"):
        # 1. Check a users permissions
        return False
    elif actionDesired.find("2"):
        # 2. Post a message as the user
        return False
    elif actionDesired.find("3"):
        # 3. DOX User (Currently Disabled)
        return False
    elif actionDesired.find("4"):
        # 4. Check bans in a specific server
        return False
    elif actionDesired.find("5"):
        # 5. Check all bans the user can see
        return False
    elif actionDesired.find("6"):
        # 6. cmyuiDiscord (Beta as fuck)
        return False

if config['default']['tokenAuth'] == True:
    client.run(str(config['discord']['token']))
else:
    client.run('{}, {}'.format(config['discord']['email'], config['discord']['password'])