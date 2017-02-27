#-------------------------------------------------#
#                                                 #
#       The permissions file for Li-Bot           #
#                                                 #
#-------------------------------------------------#


#The default roles for general commands
user_roles = {'@everyone'}

#The list of commands which the "user" permission
# level can run
user_commands = {'user','help','roll','test','random'}


#The defualt roles for moderator commands
moderator_roles = {'owner','administrator','moderator'}

#The list of commands which the "user" permission
# level can run (Includes all user commands)
moderator_commands = {}


#The default roles for Administrator commands
admin_roles = {'owner','administrator'}

#The list of commands which the "admin" permission
# level can run (Includes all moderator & user commands)
admin_commands = {}
