import discord
import asyncio
import configparser
import re
import logging
import traceback
from colorama import init
from colorama import Fore, Back, Style

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
    """
    if ("verify email" in message.content or
    "email verification" in message.content or
    "verify my email" in message.content or
    "verification" in message.content or
    "verify akatsuki" in message.content or
    "verify account" in message.content):
        await client.send_message(message.channel, 'Hi, this is an automatic response as your message was assumed to be about: Email verification.\n\nAs the verification page says, Akatsuki does not use verification emails. To verify your account, simply install the switcher, install the certificate, click the server you\'d like to play on, and click On/Off, then login to osu! to complete the verification process.\n\nIf this was not the point of your message, or this was not helpful, cmyui will likely check this soon owo.')
    elif ("error writing" in message.content or
    "read only" in message.content or
    "readonly" in message.content or
    "read-only" in message.content or
    "hosts file" in message.content):
        await client.send_message(message.channel, 'Hi, this is an automatic response as your message was assumed to be about: Hosts file showing as read-only mode.\n\nEnsure you are running the switcher as Administrator, and disable your anti-virus (or add the switcher as an exclusion) and try again. As mentioned before, this is triggered since the switcher edits a system file (hosts).\nIf it still does not work, feel free to edit your hosts file yourself by adding these to the bottom of your hosts file (found at "C:\\Windows\\System32\\Drivers\\etc") depending on the server you want. You will need to run notepad as admin, then use ctrl + o to open the file, as it is a system file.')
    """
    if message.author != client.user: # Make it so you don't see your own messages :o
        if message.server is None: # Private messages
            print(Fore.YELLOW + Style.BRIGHT + "{} [{}] {}: {}".format(message.timestamp, message.channel, message.author, message.content))
        elif client.user.id in message.content: # When you are pinged
            print(Fore.CYAN + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
        elif (config['discord']['username'] in message.content.lower() and len(config['discord']['username']) > 1 or
            client.user.name in message.content.lower()): # When your username is mentioned (either actual one, or custom set in configuration)
            print(Fore.GREEN + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
        elif message.server.id in config['default']['important_servers']: # important_servers from configuration file
            print(Fore.BLUE + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
        else: # Regular message
            print("{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))

    if message.content.startswith('$s') and message.author == client.user:
    # Change your discord users status / game
        game = ''.join(message.content[3:]).strip() # Get the game

        if game is not None: # Game also changed

            """
            game Variables:
            name = name of the game
            url = link for the game (usually for streaming probably)
            type = boolean to show whether streaming or not
            """
            await client.change_presence(game=discord.Game(name=game, url='https://akatsuki.pw/', type=0))

            print(Fore.GREEN + Style.BRIGHT + "Game changed to: {}".format(game))
        else:
            print(Fore.RED + Style.BRIGHT + "Please specify a game name.")

    if message.content.startswith('$c') and message.author == client.user:
    # Our little list of possibilities..
        actionDesired = input("""\nWhat would you like to do today?
                                \n1. Check a users permissions
                                \n2. Send messages to a server channel
                                \n3. Send messages in PMs
                                \n>> """)

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
            if targetUser is not None:
                print("User found. Result: {}\n".format(targetUser))

                # The fuck is this lol
                print("""------ User Perms ------\n
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
                if int(config['default']['debug']) == 1:
                    print(Fore.MAGENTA + "\nDebug\n\n")
                    print("Sorry.. I couldn't find a user by that ID.. Heres a bit of info:\n")
                    print("Server:")
                    print("targetServerID: {}".format(targetServerID))
                    print("targetServer: {}\n".format(targetServer))
                    print("User:")
                    print("targetUserID: {}".format(targetUserID))
                    print("targetUser: {}\n\n".format(targetUser))
                else:
                    print(Fore.RED + "Sorry.. I couldn't find a user by that ID!")

        # Really stupid, and incomplete stuff
        elif actionDesiredInt == 2:
            # 2. Post a message as the user (in a server)
            targetChannelID = input('\nAlright. I\'ll need the channel ID of where you\'d like to post in.\n>> ')
            targetChannel = client.get_channel(targetChannelID)
            if targetChannel is not None:
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
            if targetUserID is not None:
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
            if targetUserID is not None:
                user = discord.User(id=targetUserID)
                print("User information: {}\n-----------------\nID: {}\nisBot: {}\navatar_url: {}\ncreated_at: {}\ndisplay_name: {}\n".format(user, user.id, user.bot, user.avatar_url, user.created_at, user.display_name))

        """ Not currently functional
        elif actionDesiredInt == 5:
            # 5. Get all info on a server
            targetServerID = input('Please type the ServerID\n>> ')
            if targetServerID is not None:
                server = discord.Server(id=targetServerID)
                print("Server information: {}\n\nID: {}\nRoles: {}\nEmojis: {}\nRegion: {}\nafk_timeout: {}\nafk_channel: {}\nmembers: {}\nchannels: {}\nicon_url: {}\nowner: {}\nmfa_level: {}\nfeatures: {}\nsplash: {}\ndefault_role: {}\ndefault_channel: {}\ncreated_at: {}\nrole_hierarchy: {}\n".format(
                    server.name, server.id, server.roles, server.emojis, server.region, server.afk_timeout, server.afk_channel, server.members, server.channels, server.icon_url, server.owner, server.mfa_level, server.features, server.splash, server.default_role, server.default_channel, server.created_at, server.role_hierarchy))
        """

        elif actionDesiredInt == 6:
            # 6. Absolutely fucking everything. Give me the information.. DADDY**.**
            for server in client.servers:
                print(Fore.MAGENTA + "Current Server: {}\n".format(server))
            for message in client.messages:
                print(Fore.MAGENTA + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            #for vc in client.voice_clients:
            #    print(Fore.BLUE + Style.BRIGHT + "{} [{} ({})] {}: {}".format(message.timestamp, message.server, message.channel, message.author, message.content))
            print(Fore.MAGENTA + Style.BRIGHT + "\n\n\nThe cancer is complete.\n\n")

        else:
            print(Fore.RED + 'This feature could not be found, or in unavailable.')

# Ok this is a bit sketchy
if int(config['default']['tokenauth']) == 1:
    if int(config['default']['debug']) == 1:
        print(Fore.MAGENTA + "Logging in with credentials: {}".format(config['discord']['token']))
    client.run(str(config['discord']['token']))
elif int(config['default']['tokenauth']) == 0:
    if int(config['default']['debug']) == 1:
        print(Fore.MAGENTA + "Logging in with credentials: {}, {}".format(config['discord']['email'], config['discord']['password']))
    client.run('{}'.format(config['discord']['email']), '{}'.format(config['discord']['password']))