import discord
import asyncio
import configparser
import re
import logging
import traceback
from colorama import init
from colorama import Fore, Back, Style
from secret import scoreFlags

# Initialize colorama owo
init(autoreset=True)

# Discord Client
client = discord.Client()

# Configuration
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

# Startup, after login action
@client.event
async def on_ready():
    print(Fore.GREEN + '\nAuthentication Successful.\n{} | {}\n--------------------------\n'.format(client.user.name,client.user.id))
    if int(config['default']['debug']) == 1:
        print(Fore.MAGENTA + "\n\nConfiguration:\ndebug: {}\ntokenauth: {}\n\n".format(config['default']['debug'], config['default']['tokenauth']))

# On exceptions, don't make the whole thing die :)
@client.event
async def on_error(event, *args):
    print(Fore.RED + "\n\nFuck.\n\nError: {}\nargs: {}\n\nTraceback: {}\n".format(event, *args, logging.warning(traceback.format_exc())))

# On message event
@client.event
async def on_message(message):
    client.wait_until_ready()
    if config['discord']['username'] == 'cmyui': # Useless stuff only I would want lol
        if ("verify e" in message.content.lower() or
        "verification" in message.content.lower() or
        "on email" in message.content.lower() or
        "verify m" in message.content.lower() or
        "verify a" in message.content.lower() or
        "email t" in message.content.lower()) and message.author != client.user:

            # I really don't know how to do this :(
            # Private Messaging
            if message.server is None:
                if "badge" not in message.content.lower():
                    await client.send_message(message.author, 'Right, this is an automated message as it was presumed your message was about: Email Verification\n\nAs the verification page says, Akatsuki does not use verification emails. To verify your account, simply install the switcher, install the certificate, click the server you\'d like to play on, and click On/Off, then login to osu! to complete the verification process.')
                    if int(config['default']['debug']) == 1:
                        print(Fore.MAGENTA + "Triggered: Verification Email Support\nUser: {}".format(message.author))
                else:
                    print(Fore.MAGENTA + "Aborted Trigger: Email Verification Support, due to \"badge\" contents of the message.\nUser: {}".format(message.author))
            # Akatsuki's ServerID
            elif message.server.id == '365406575893938177':
                if "badge" not in message.content.lower():
                    await client.send_message(message.author, 'Right, this is an automated message as it was assumed you needed assitance in Akatsuki with: Email Verification\n\nAs the verification page says, Akatsuki does not use verification emails. To verify your account, simply install the switcher, install the certificate, click the server you\'d like to play on, and click On/Off, then login to osu! to complete the verification process.')
                    if int(config['default']['debug']) == 1:
                        print(Fore.MAGENTA + "Triggered: Verification Email Support\nUser: {}".format(message.author))
                else:
                    print(Fore.MAGENTA + "Aborted Trigger: Email Verification Support, due to \"badge\" contents of the message.\nUser: {}".format(message.author))

    if message.author != client.user:
        if message.server is None: # Private messages
            print(Fore.YELLOW + Style.BRIGHT + "{} [{}] {}: {}".format(message.timestamp, message.channel, message.author, message.content))
        elif client.user.id in message.content: # When you are pinged
            print(Fore.CYAN + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
        elif (config['discord']['username'] in message.content.lower() and len(config['discord']['username']) > 1 or
            client.user.name in message.content.lower()): # When your username is mentioned (either actual one, or custom set in configuration)
            print(Fore.GREEN + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            
            # add if thing for new config here

        elif message.server.id in config['default']['important_servers']: # important_servers from configuration file
            if message.channel.id == '508022888113111040':
                # Play my fucking audio file here when thats a thing
                print(Back.CYAN + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            else:
                print(Fore.BLUE + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
        else: # Regular message
            print("{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))

    elif message.content.startswith('$f') and message.author == client.user:
        # Check score flags.. in discord!
        await client.delete_message(message)  # Remove $f
        if config['default']['secret']:
            print("\n")
            flags = ''.join(message.content[3:]).strip() # Get the flags from discord message
            if flags.isdigit():
                scoreFlags.calculateFlags(int(flags))
            else:
                print(Fore.RED + "That is not a valid entry.")
        else:
            print(Fore.RED + "You do not have secret enabled in config.")

    elif message.content.startswith('$s') and message.author == client.user:
        # Change your discord users status / game
        game = ''.join(message.content[3:]).strip() # Get the game
        if game: # Game also changed

            """
            game Variables:
            name = name of the game
            url = link for the game (usually for streaming probably)
            type = boolean to show whether streaming or not
            """
            await client.change_presence(game=discord.Game(name=game, url='https://akatsuki.pw/', type=0))

            print(Fore.GREEN + Style.BRIGHT + "Game changed to: {}".format(game))
            await client.delete_message(message) # Remove $s
        else:
            print(Fore.RED + Style.BRIGHT + "Please specify a game name.")
            await client.delete_message(message) # Remove $s

    elif message.content.startswith('$c') and message.author == client.user:
        # Our little list of possibilities..
        await client.delete_message(message) # Remove $c
        actionDesired = input("""\nWhat would you like to do today?
                                \n1. Check a users permissions
                                \n2. Send messages to a server channel
                                \n3. Send messages in PMs
                                \n4. Get all info on a user possible
                                \n5. Absolutely fucking everything. Give me the information.. DADDY**.**
                                \n>> """) # just dont fuck with 5 yet c:

        actionDesiredInt = int(re.search(r'\d+', actionDesired).group())
        if actionDesiredInt == 1:
            # 1. Check a users permissions
            targetServerID = input('\nAlright. I\'ll need the server ID of the discord server you\'d like their perms in.\n>> ')
            for server in client.servers:
                if config['default']['debug'] == 1:
                    print(Fore.MAGENTA + "Current Server: {}\n".format(server))
                if server.id == str(targetServerID):
                    targetServer = server
                    print('Server found.\n')

            targetUserID = input('Whats their UserID?\n>> ')
            targetUser = targetServer.get_member(str(targetUserID))
            if targetUser:
                # The fuck is this lol
                print("""User found. Result: {}\n
                    ------- User Perms -------\n
                    Permissions Bitwise: {}\n
                    create_instant_invite: {}\n
                    kick members: {}\n
                    ban_members: {}\n
                    administrator: {}\n
                    manage_channels: {}\n
                    manage_server: {}\n
                    view_audit_logs: {}\n
                    read_messages: {}\n
                    send_messages: {}\n
                    send_tts_messages: {}\n
                    manage_messages: {}\n
                    embed_links: {}\n
                    attach_files: {}\n
                    read_message_history: {}\n
                    mention_everyone: {}\n
                    external_emojis: {}\n
                    connect: {}\n
                    speak: {}\n
                    mute_members: {}\n
                    deafen_members: {}\n
                    move_members: {}\n
                    use_voice_activation: {}\n
                    change_nickname: {}\n
                    manage_nicknames: {}\n
                    manage_roles: {}\n
                    manage_webhooks: {}\n
                    manage_emojis: {}""".format(
                    targetUser,
                    targetUser.server_permissions.value,
                    targetUser.server_permissions.create_instant_invite,
                    targetUser.server_permissions.kick_members,
                    targetUser.server_permissions.ban_members,
                    targetUser.server_permissions.administrator,
                    targetUser.server_permissions.manage_channels,
                    targetUser.server_permissions.manage_server,
                    targetUser.server_permissions.view_audit_logs,
                    targetUser.server_permissions.read_messages,
                    targetUser.server_permissions.send_messages,
                    targetUser.server_permissions.send_tts_messages,
                    targetUser.server_permissions.manage_messages,
                    targetUser.server_permissions.embed_links,
                    targetUser.server_permissions.attach_files,
                    targetUser.server_permissions.read_message_history,
                    targetUser.server_permissions.mention_everyone,
                    targetUser.server_permissions.external_emojis,
                    targetUser.server_permissions.connect,
                    targetUser.server_permissions.speak,
                    targetUser.server_permissions.mute_members,
                    targetUser.server_permissions.deafen_members,
                    targetUser.server_permissions.move_members,
                    targetUser.server_permissions.use_voice_activation,
                    targetUser.server_permissions.change_nickname,
                    targetUser.server_permissions.manage_nicknames,
                    targetUser.server_permissions.manage_roles,
                    targetUser.server_permissions.manage_webhooks,
                    targetUser.server_permissions.manage_emojis
                    ))
            else:
                print(Fore.RED + "Sorry.. I couldn't find a user by that ID!")

        # Really stupid, and incomplete stuff
        elif actionDesiredInt == 2:
            # 2. Post a message as the user (in a server)
            targetChannelID = input('\nAlright. I\'ll need the channel ID of where you\'d like to post in.\n>> ')
            targetChannel = client.get_channel(targetChannelID)
            if targetChannel:
                print("Channel found; Connection established.")

                x = 0 # Sorry I literally do not know how to do this properly. Maybe this is properly.. but I doubt it
                while x < 1:
                    if message == "exit()":
                        break
                    message = input("\n{}: ".format(config['discord']['email']))
                    await client.send_message(targetChannel, message)

        elif actionDesiredInt == 3:
            # 3. Open PM and send a message to a user
            targetUserID = input('Whats their UserID?\n>> ')
            if targetUserID:
                user = discord.User(id=targetUserID)

                x = 0 # Sorry I literally do not know how to do this properly. Maybe this is properly.. but I doubt it
                while x < 1:
                    if message == "exit()":
                        break
                    message = input("\n{}: ".format(config['discord']['username']))
                    await client.send_message(user, message)
            else:
                print(Fore.RED + 'Could not find a user by that ID.')

        elif actionDesiredInt == 4:
            # 4. Get all info on a user possible
            targetUserID = input('Whats their UserID?\n>> ')
            if targetUserID:
                user = discord.User(id=targetUserID)
                print("User information: {}\n-----------------\nID: {}\nisBot: {}\navatar_url: {}\ncreated_at: {}\ndisplay_name: {}\n".format(user, user.id, user.bot, user.avatar_url, user.created_at, user.display_name))

        elif actionDesiredInt == 5:
            # 5. Absolutely fucking everything. Give me the information.. DADDY**.**
            for server in client.servers:
                print(Fore.MAGENTA + "Current Server: {}\n".format(server))
            for message in client.messages:
                print(Fore.MAGENTA + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            #for vc in client.voice_clients:
            #    print(Fore.BLUE + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            print(Fore.MAGENTA + Style.BRIGHT + "\n\n\nThe cancer is complete.\n\n")

        else:
            print(Fore.RED + 'This feature could not be found, or in unavailable.')

if int(config['default']['tokenauth']) == 1:
    if int(config['default']['debug']) == 1:
        print(Fore.MAGENTA + "Logging in with credentials: {}".format('*' * len(config['discord']['token'])))
    client.run(str(config['discord']['token']))
elif int(config['default']['tokenauth']) == 0:
    if int(config['default']['debug']) == 1:
        print(Fore.MAGENTA + "Logging in with credentials: {}, {}".format(config['discord']['email'], '*' * len(config['discord']['password'])))
    client.run('{}'.format(config['discord']['email']), '{}'.format(config['discord']['password']))