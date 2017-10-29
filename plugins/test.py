from disco.bot import Plugin


class testPlugin(Plugin):
    @Plugin.command("test")
    def commands_test(self, event):
        event.msg.reply("Confirmed:tm:")