# Importing sample Fusion Command
# Could import multiple Command definitions here
from .OpenerCommand import OpenerCommand
from .Demo2Command import Demo2Command
from .DemoPaletteCommand import DemoPaletteShowCommand, DemoPaletteSendCommand

commands = []
command_definitions = []

# # Define parameters for 1st command
# cmd = {
#     'cmd_name': 'Open',
#     'cmd_description': 'Open a file',
#     'cmd_id': 'cmdID_Opener_Open',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Opener',
#     'command_promoted': True,
#     'class': OpenerCommand
# }
# command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Open',
    'cmd_description': 'Open (Import) a file',
    'cmd_id': 'cmdID_Opener_Open_QAT_menu',
    'workspace': 'FusionSolidEnvironment',
    'cmd_resources': '',
    'command_in_nav_bar': True,
    'add_to_drop_down': True,
    'drop_down_cmd_id': 'FileSubMenuCommand',
    'class': OpenerCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Open',
    'cmd_description': 'Open (Import) a file',
    'cmd_id': 'cmdID_Opener_Open_QAT',
    'workspace': 'FusionSolidEnvironment',
    'cmd_resources': './resources',
    'command_in_nav_bar': True,

    'class': OpenerCommand
}
command_definitions.append(cmd)

# # Define parameters for 2nd command
# cmd = {
#     'cmd_name': 'Fusion Demo Command 2',
#     'cmd_description': 'Fusion Demo Command 2 Description',
#     'cmd_id': 'cmdID_demo2',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Opener',
#     'command_visible': True,
#     'command_promoted': True,
#     'class': Demo2Command
# }
# command_definitions.append(cmd)
#
# # Define parameters for 2nd command
# cmd = {
#     'cmd_name': 'Fusion Palette Demo Command',
#     'cmd_description': 'Fusion Demo Palette Description',
#     'cmd_id': 'cmdID_palette_demo',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Opener',
#     'command_visible': True,
#     'command_promoted': False,
#     'palette_id': 'demo_palette_id',
#     'palette_name': 'Demo Palette Name',
#     'palette_html_file_url': 'demo.html',
#     'palette_is_visible': True,
#     'palette_show_close_button': True,
#     'palette_is_resizable': True,
#     'palette_width': 500,
#     'palette_height': 600,
#     'class': DemoPaletteShowCommand
# }
# command_definitions.append(cmd)
#
# # Define parameters for 2nd command
# cmd = {
#     'cmd_name': 'Fusion Palette Send Command',
#     'cmd_description': 'Send info to Fusion 360 Palette',
#     'cmd_id': 'cmdID_palette_send_demo',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Opener',
#     'command_visible': True,
#     'command_promoted': False,
#     'palette_id': 'demo_palette_id',
#     'class': DemoPaletteSendCommand
# }
# command_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False

# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()

# Set to True to display various useful messages when debugging your app
debug = False


# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()

