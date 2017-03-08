#------------------------------------------------#
#                                                #
#     The response for the "test" command        #
#                                                #
#------------------------------------------------#

def run(client, message, *args):
    print(args)
    actions = [client.send_message(message.channel, "Test confirmed:tm:")]
    return actions
