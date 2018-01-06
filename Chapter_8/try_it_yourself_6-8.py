#8-6 City Names
def city_country(name, country):
    print('"' + name + ', ' + country + '"')

city_country("New York", "New York")
city_country("Hartford", "Connecticut")
city_country("Rochester", "New York")

#8-7 Album
def make_album(artist_name, album_title, number_of_tracks=''):
    if number_of_tracks:
        album = {"artist": artist_name, "title": album_title, "tracks": number_of_tracks}
    else:
        album = {"artist": artist_name, "title": album_title}
    return album

album = make_album("Kanye West", "College Dropout", number_of_tracks=21)
print(album)
album = make_album("Kendrick Lamar", "To Pimp A Butterfly")
print(album)
album = make_album("Kanye West", "Yeezus", number_of_tracks=11)
print(album)

#8-8 User Albums
def make_album_2(artist_name, album_title, number_of_tracks=''):
    album_2 = {"artist": artist_name, "title": album_title, "tracks": number_of_tracks}
    print("\nSo the artist is " + artist_name + " and the album title is " + album_title + " and the number of tracks is " + number_of_tracks + " .")

while True:
    print("\nWhat is the name of the artist, album title, and number of tracks?")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == "q":
        break

    a_title = input("Album title: ")
    if a_title == "q":
        break

    num_tracks = input("Number of tracks: ")
    if num_tracks == "q":
        break

    make_album_2(a_name, a_title, num_tracks)

