# 8-8. User Albums

# Start with my program from Exercise 8-7.
def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return album

# Write a while loop that allows users to enter an album's artist and title.
while True:
    print("\nPlease tell us about your favorite albums:")
    print("(enter 'q' at any time to quit)")

    a_name = input("The artist name: ")
    if a_name == 'q':
        break 

    a_title = input("The album title: ")
    if a_title == 'q':
        break

    # Call make_album() with the user's input and print the dictionary that's created.
    album_info = make_album(a_name, a_title)
    print(f"")

