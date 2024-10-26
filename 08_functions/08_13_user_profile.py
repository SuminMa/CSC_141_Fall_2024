# 8-13. User Profile

# Start with a copy of user_profile.py.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Build a profile of myself by calling build_profile().
# Use my first and last names and three other key-value pairs that describe me.
my_profile = build_profile('Sumin', 'Ma',
            location='Reading',
            field='Computer Science',
            age='23')

print(my_profile)