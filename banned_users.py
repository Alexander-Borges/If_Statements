# Checking Whether a Value is Not in a List
# Sometimes its important to know if a value does not appear in a list. You can use the keyword not in this situation. For example, consider a list of users who are banned from commenting on a forum. YOu can check whether a user has been banned before allowing that person to submit a comment:
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")