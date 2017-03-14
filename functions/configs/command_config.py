#-----------------------------------------------------------------------------#
#                                                                             #
#                                                                             #
#                                 Preface:                                    #
#                                                                             #
#        This is the persmission file for the commands, sub-commands          #
#            check permissions based on "[command]_[sub command]"             #
#             DO NOT CHANGE THIS FILE UNLESS YOU ARE A DEVELOPER              #
#                                                                             #
#-----------------------------------------------------------------------------#

"IMPORTS"
import functions.commands.help as help
import functions.commands.test as test
import functions.commands.random as random



"COMMAND RUNNING"
all_commands = {
"test":test.run,
"help":help.run,
"random_roll":random.roll,
"random_alkali":random.alkali,
"random_object":random.object,
"random_shuffle":random.shuffle,
#"random_dance":random.dance
"random_gif":random.gif
}


"COMMAND HELPS"
command_helps = {
"test":test.help
#"help":help.help,
#"random_roll":random.roll_help,
#"random_alkali":"null",
#"random_object":random.object_help,
#"random_dance":"null",
#"random_gif":random.gif_help
}
