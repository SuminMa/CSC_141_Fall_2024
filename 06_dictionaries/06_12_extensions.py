# 6-12. Extensions
# Use one of the example programs from this chapter, and extend it
# I used the many_users.py (Page 110)
# Added new keys and values
# Changed the context of the program
users = {
    'aeinstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'Princeton',
        'profession': 'Physicist',
        'birth_year': 1879,
        'famous_for': 'Theory of Relativity'
    },
    'mcurie': {
        'first': 'Marie',
        'last': 'Curie',
        'location': 'Paris',
        'profession': 'Chemist/Physicist',
        'birth_year': 1867,
        'famous_for': 'Radioactivity Research'
    },
    'nbohr': {
        'first': 'Niels',
        'last': 'Bohr',
        'location': 'Copenhagen',
        'profession': 'Physicist',
        'birth_year': 1885,
        'famous_for': 'Bohr Model of the Atom'
    }
}

# Improved output formatting
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    print(f"Full Name: {full_name}")
    print(f"Location: {user_info['location'].title()}")
    print(f"Profession: {user_info['profession']}")
    print(f"Born: {user_info['birth_year']}")
    print(f"Famous For: {user_info['famous_for']}")
