class Role:

    def auto(member, roles):
        role_reason = "Auto-role for voice"
        for role in roles:
            if roles[role] == "add":
                member.add_role(int(role), reason=role_reason)
            elif roles[role] == "remove":
                member.remove_role(int(role), reason=role_reason)