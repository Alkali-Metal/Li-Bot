#------------------------------------------------#
#                                                #
#      DO NOT CHANGE THIS FILE UNLESS YOU ARE    #
#          DEVELOPING A PORTION OF THE BOT!      #
#                                                #
#------------------------------------------------#

import functions.commands.help as help
import functions.commands.random as random
import functions.commands.test as test


all_commands = {
"test":test.run,
"help":help.run,
"random_dance":random.dance,
"random_number":random.number,
"random_object":random.object,
"random_shuffle":random.shuffle,
"random_roll":random.roll
}



temmie_commands = {
"random_alkali":random.alkali
}
