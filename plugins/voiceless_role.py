import data.json_handler as handler
from bot_types.discord.role import Role

from disco.bot import Plugin
from holster.emitter import Priority


class config():
    old_count = None


class VoicelessRolePlugin(Plugin):


    @Plugin.listen("VoiceStateUpdate", priority=Priority.BEFORE)
    def on_voice_update(self, event):
        config.old_count = len(event.state.guild.voice_states)
    
    
    @Plugin.listen("VoiceStateUpdate", priority=Priority.AFTER)
    def voice_state_update_after(self, event):
        guild_id = str(event.state.guild_id)
        custom_roles = handler.load_role_mappings()
        guild_member = event.state.guild.get_member(event.state.user)
        role_list = {}
        
        if event.state.channel_id != None:
            old_count = config.old_count
            new_count = len(event.state.guild.voice_states)
            channel_id = str(event.state.channel_id)
            channel_type = str(event.state.channel.type)


            if old_count == 0 and new_count == 0:
                return


            if channel_type == "guild_voice":
                if guild_id in custom_roles:
                    if new_count > old_count:
                        if channel_id in custom_roles[guild_id]:
                            role_id = custom_roles[guild_id][channel_id]
                            if role_id == None:
                                return
                            if role_id not in guild_member.roles:
                                role_list[str(role_id)] = "add"
                        else:
                            role_id = custom_roles[guild_id]["general"]
                            if role_id == None:
                                return
                            if role_id not in guild_member.roles:
                                role_list[str(role_id)] = "add"
                        Role.auto(guild_member, role_list)
                    elif new_count == old_count:
                        if channel_id in custom_roles[guild_id]:
                            role_id = custom_roles[guild_id][channel_id]
                            if role_id != None:
                                if role_id not in guild_member.roles:
                                    role_list[str(role_id)] = "add"
                            current_role = role_id
                        else:
                            role_id = custom_roles[guild_id]["general"]
                            if role_id != None:
                                if role_id not in guild_member.roles:
                                    role_list[str(role_id)] = "add"
                            current_role = role_id
                        for channel in custom_roles[guild_id]:
                            role_id = custom_roles[guild_id][channel]
                            if role_id != current_role:
                                if role_id != None:
                                    if role_id in guild_member.roles:
                                        role_list[str(role_id)] = "remove"
                        Role.auto(guild_member, role_list)
        else:
            if guild_id in custom_roles and guild_id != None:
                for role_id in custom_roles[guild_id]:
                    role_id = custom_roles[guild_id][role_id]
                    if role_id in guild_member.roles:
                        role_list[str(role_id)] = "remove"
                if len(role_list) > 0:
                    Role.auto(guild_member, role_list)