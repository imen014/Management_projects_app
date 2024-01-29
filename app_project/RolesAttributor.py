class RolesAttributor:
    
    def attribuer_role_group(users, group1, group2):
        for user in users:
            if user.role == "CREATOR":
                user.groups.add(group1)
            else:
                user.groups.add(group2)