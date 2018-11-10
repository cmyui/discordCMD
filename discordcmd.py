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
    print("\n\n\n\n\nextras: {}\ndebug: {}\ntokenauth: {}\n\n\n\n".format(config['default']['extras'], config['default']['debug'], config['default']['tokenauth']))
    if int(config['default']['debug']) == 1:
        print("\nDebug 1 ---------------------------------------------------------------------- #\n\n")

    # Our little list of possibilities..
    if int(config['default']['extras']) == 1:
        actionDesired = input("""\nWhat would you like to do today?
                                \n1. Check a users permissions
                                \n2. Post a message as the user
                                \n3. DOX User (Currently Disabled)
                                \n4. Check bans in a specific server
                                \n5. Check all bans the user can see
                                \n6. cmyuiDiscord (Beta as fuck)
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
            """
            if int(config['default']['debug']) == 1:
                print("\nDebug 4 ---------------------------------------------------------------------- #\n\n")
                print("Current Server: {}\n".format(server))
            """
            if server.id == str(targetServerID):
                """
                if int(config['default']['debug']) == 1:
                    print("\nDebug 5 ---------------------------------------------------------------------- #\n\n")
                """
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

            """ Old ver
            print("------ User Perms ------")
            print("Permissions Bitwise: {}\n".format(targetUser.server_permissions.value))
            print("create_instant_invite: {}".format(targetUser.server_permissions.kick_members))
            print("kick members: {}".format(targetUser.server_permissions.create_instant_invite))
            print("ban_members: {}".format(targetUser.server_permissions.ban_members))
            print("administrator: {}".format(targetUser.server_permissions.administrator))
            print("manage_channels: {}".format(targetUser.server_permissions.manage_channels))
            print("manage_server: {}".format(targetUser.server_permissions.manage_server))
            print("view_audit_logs: {}".format(targetUser.server_permissions.view_audit_logs))
            print("read_messages: {}".format(targetUser.server_permissions.read_messages))
            print("send_messages: {}".format(targetUser.server_permissions.send_messages))
            print("send_tts_messages: {}".format(targetUser.server_permissions.send_tts_messages))
            print("manage_messages: {}".format(targetUser.server_permissions.manage_messages))
            print("embed_links: {}".format(targetUser.server_permissions.embed_links))
            print("attach_files: {}".format(targetUser.server_permissions.attach_files))
            print("read_message_history: {}".format(targetUser.server_permissions.read_message_history))
            print("mention_everyone: {}".format(targetUser.server_permissions.mention_everyone))
            print("external_emojis: {}".format(targetUser.server_permissions.external_emojis))
            print("connect: {}".format(targetUser.server_permissions.connect))
            print("speak: {}".format(targetUser.server_permissions.speak))
            print("mute_members: {}".format(targetUser.server_permissions.mute_members))
            print("deafen_members: {}".format(targetUser.server_permissions.deafen_members))
            print("move_members: {}".format(targetUser.server_permissions.move_members))
            print("use_voice_activation: {}".format(targetUser.server_permissions.use_voice_activation))
            print("change_nickname: {}".format(targetUser.server_permissions.change_nickname))
            print("manage_nicknames: {}".format(targetUser.server_permissions.manage_nicknames))
            print("manage_roles: {}".format(targetUser.server_permissions.manage_roles))
            print("manage_webhooks: {}".format(targetUser.server_permissions.manage_webhooks))
            print("manage_emojis: {}".format(targetUser.server_permissions.manage_emojis))
            """
        else:

            if int(config['default']['debug']) == 1:
                print("\nDebug 8 ---------------------------------------------------------------------- #\n\n")
                print("Sorry.. I couldn't find a user by that ID.. Heres a bit of info:\n")
                print("------ Debug ------")
                print("Server:")
                print("targetServerID: {}".format(targetServerID))
                print("targetServer: {}\n".format(targetServer))
                print("User:")
                print("targetUserID: {}".format(targetUserID))
                print("targetUser: {}".format(targetUser))
                print("------ Debug ------\n\n")
            else:
                return "Sorry.. I couldn't find a user by that ID!"

    # Really stupid, and incomplete stuff
    elif actionDesiredInt == 2 and int(config['default']['extras']) == 1:
        # 2. Post a message as the user (in a server)
        targetServerID = input('\nAlright. I\'ll need the server ID of the discord server you\'d like to post in.\n>> ')
        for server in client.servers:
            if server.id == str(targetServerID):
                targetServer = server
                print('Server found.\n')
            else:
                return 'Sorry.. I couldn\'t find a server by that ID!'

    elif actionDesiredInt == 3 and int(config['default']['extras']) == 1:
        # 3. Open PM and send a message to a user
        targetUserID = input('Whats their UserID?\n>> ')
        if targetUserID is not None:
            client.start_private_message(targetUserID)
            await client.send_message(targetUserID, 'Test')
        else:
            return 'Could not find a user by that ID.'

        return 'Complete.'

    elif actionDesiredInt == 4 and int(config['default']['extras']) == 1:
        # 4. Check bans in a specific server
        return False
    elif actionDesiredInt == 5 and int(config['default']['extras']) == 1:
        # 5. Check all bans the user can see
        return False
    elif actionDesiredInt == 6 and int(config['default']['extras']) == 1:
        # 6. cmyuiDiscord (Beta as fuck)
        return False
    else:
        return 'This feature could not be found, or in unavailable.'

if int(config['default']['debug']) == 1:
    print("Beginning login process..\n")

if int(config['default']['tokenauth']) == 1:
    if int(config['default']['debug']) == 1:
        print("Input: {}".format(config['discord']['token']))
    client.run(str(config['discord']['token']))
else:
    if int(config['default']['debug']) == 1:
        print('Input: {}, {}'.format(config['discord']['email'], config['discord']['password']))
    client.run('{}'.format(config['discord']['email']), '{}'.format(config['discord']['password']))