# 8-7. Album

# Write a function called make_album() that builds a dictionary describing a music album.
# It takes in an artist name and an album title.
def make_album(artist_name, album_title):
    # It returns a dictionary containing these two pieces of information.
    album = {'artist': artist_name, 'title': album_title}
    return album

# Use the function to make three dictionaries representing different albums.
album_01 = make_album('Nirvana', 'Nevermind')
album_02 = make_album('Joni Mitchell', 'Blue')
album_03 = make_album('Queen Latifah', 'Black Reign')

# Print each return value to show that the dictionaries are storing the information correctly.
print(album_01)
print(album_02)
print(album_03)

# Use None to add an optional parameter to make_album().
# It allows to store the number of songs on an album.
def make_album(artist_name, album_title, songs=None):
    # If the calling line includes a value for the number of songs, add it to the dictionary.
    if songs:
        album = {'artist': artist_name, 'title': album_title, 'songs':songs}
    else:
        album = {'artist': artist_name, 'title': album_title}
    return album

# Make at least one new function call that includes the number of songs on an album.
album_04 = make_album('Outkast', 'Aquemini', 16)
print(album_04)