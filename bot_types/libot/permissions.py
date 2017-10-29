class Perms:


    def has_role(member, role_id):
        member_roles = member.roles
        member_roles.append("@everyone")
        if type(role_id) == type([]):
            if set(role_id).intersection(member_roles):
                return True
            return False
        else:
            if role_id in member_roles:
                return True
            return False
    
    
    def is_owner(guild, user_id):
        if guild.owner.id == user_id:
            return True
        return False