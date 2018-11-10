import discord
import asyncio
import configparser
import re

client = discord.Client()

# Configuration
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

@client.event
async def on_ready():
    print('Logged in as:\n{}\n{}\n------'.format(client.user.name,client.user.id))
    if int(config['default']['debug']) == 1:
        print("\nDebug 1 ---------------------------------------------------------------------- #\n\nConfiguration:\nextras: {}\ndebug: {}\ntokenauth: {}\n\n".format(config['default']['extras'], config['default']['debug'], config['default']['tokenauth']))

    # Our little list of possibilities..
    if int(config['default']['extras']) == 1:
        actionDesired = input("""\nWhat would you like to do today?
                                \n1. Check a users permissions
                                \n2. Post a message as the user
                                \n>> """)
    else:
        actionDesired = input("""\nWhat would you like to do today?
                                \n1. Check a users permissions
                                \n>> """)

    actionDesiredInt = int(re.search(r'\d+', actionDesired).group())
    if int(config['default']['debug']) == 1:
        print("\nDebug 2 ---------------------------------------------------------------------- #\nactionDesiredInt: {}\n\n".format(actionDesiredInt))
    if actionDesiredInt == 1:
        # 1. Check a users permissions
        targetServerID = input('\nAlright. I\'ll need the server ID of the discord server you\'d like their perms in.\n>> ')
        if int(config['default']['debug']) == 1:
            print("\nDebug 3 ---------------------------------------------------------------------- #\ntargetServerID: {}\n\n".format(targetServerID))
        for server in client.servers:
            if int(config['default']['debug']) == 1:
                print("\nDebug 4 ---------------------------------------------------------------------- #\n\n")
                print("Current Server: {}\n".format(server))
            if server.id == str(targetServerID):
                if int(config['default']['debug']) == 1:
                    print("\nDebug 5 ---------------------------------------------------------------------- #\n\n")
                targetServer = server
                print('Server found.\n')


        if int(config['default']['debug']) == 1:
            print("\nDebug 6 ---------------------------------------------------------------------- #\n\n")
        targetUserID = input('Whats their UserID?\n>> ')
        if int(config['default']['debug']) == 1:
            print("\nDebug 7 ---------------------------------------------------------------------- #\ntargetUserID: {}\n\n".format(targetUserID))
        targetUser = targetServer.get_member(str(targetUserID))
        if targetUser is not None:
            if int(config['default']['debug']) == 1:
                print("\nDebug 8 ---------------------------------------------------------------------- #\ntargetUser: {}\n\n".format(targetUser))
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
                print("\nDebug 8 ---------------------------------------------------------------------- #\n\n")
                print("Sorry.. I couldn't find a user by that ID.. Heres a bit of info:\n")
                print("Server:")
                print("targetServerID: {}".format(targetServerID))
                print("targetServer: {}\n".format(targetServer))
                print("User:")
                print("targetUserID: {}".format(targetUserID))
                print("targetUser: {}\n\n".format(targetUser))
            else:
                return "Sorry.. I couldn't find a user by that ID!"

    # Really stupid, and incomplete stuff
    elif actionDesiredInt == 2 and int(config['default']['extras']) == 1:
        # 2. Post a message as the user (in a server)
        targetChannelID = input('\nAlright. I\'ll need the channel ID of where you\'d like to post in.\n>> ')
        targetChannel = client.get_channel(targetChannelID)
        if targetChannel is not None:
            print("Channel found; Connection established.")

            x = 0 # Sorry I literally do not know how to do this properly. Maybe this is properly.. but I doubt it
            while x < 1:
                message = input("\n{}: ".format(config['discord']['email']))
                await client.send_message(targetChannel, message)

    elif actionDesiredInt == 3 and int(config['default']['extras']) == 1:
        # 3. Open PM and send a message to a user
        targetUserID = input('Whats their UserID?\n>> ')
        if targetUserID is not None:
            user = discord.utils.get(client.get_all_members(), id=targetUserID)

            x = 0 # Sorry I literally do not know how to do this properly. Maybe this is properly.. but I doubt it
            while x < 1:
                message = input("\n{}: ".format(config['discord']['email']))
                await client.send_message(user, message)
        else:
            return 'Could not find a user by that ID.'

        return 'Complete.'

    else:
        return 'This feature could not be found, or in unavailable.'

if int(config['default']['debug']) == 1:
    print("Beginning login process..\n")

if int(config['default']['tokenauth']) == 1:
    """
    if int(config['default']['debug']) == 1:
        print("Input: {}".format(config['discord']['token']))
    """
    client.run(str(config['discord']['token']))
elif int(config['default']['tokenauth']) == 0:
    """
    if int(config['default']['debug']) == 1:
        print('Input: {}, {}'.format(config['discord']['email'], config['discord']['password']))
    """
    client.run('{}'.format(config['discord']['email']), '{}'.format(config['discord']['password']))
else:
    print('ok ur too retarded for this program\n\nplease step outside')