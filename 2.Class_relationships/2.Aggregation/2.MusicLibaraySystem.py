class Artist:
    def __init__(self, name: str):
        self.name = name

class Song:
    def __init__(self, title: str, artist: Artist, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist.name} ({self.duration}s)"

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def remove_song(self, song: Song):
        self.songs.remove(song)

    def get_song_count(self):
        return len(self.songs)

    def get_total_duration(self):
        return sum(song.duration for song in self.songs)

class User:
    def __init__(self, name: str):
        self.name = name
        self.playlists = []

    def create_playlist(self, playlist_name: str):
        playlist = Playlist(playlist_name)
        self.playlists.append(playlist)
        return playlist

    def delete_playlist(self, playlist: Playlist):
        self.playlists.remove(playlist)

class Library:
    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def get_song_count(self):
        return len(self.songs)

# Usage
if __name__ == "__main__":
    coldplay = Artist("Coldplay")
    adele = Artist("Adele")

    yellow = Song("Yellow", coldplay, 269)
    clocks = Song("Clocks", coldplay, 307)
    hello = Song("Hello", adele, 295)
    someone = Song("Someone Like You", adele, 285)

    library = Library()
    library.add_song(yellow)
    library.add_song(clocks)
    library.add_song(hello)
    library.add_song(someone)

    alice = User("Alice")
    workout = alice.create_playlist("Workout Mix")
    chill = alice.create_playlist("Chill Vibes")

    workout.add_song(yellow)
    workout.add_song(clocks)
    workout.add_song(hello)

    chill.add_song(hello)
    chill.add_song(someone)

    print(f"Library has {library.get_song_count()} songs")
    print()

    print(f"{workout.name} ({workout.get_song_count()} songs, {workout.get_total_duration()}s):")
    for s in workout.songs:
        print(f"  - {s}")
    print()

    print(f"{chill.name} ({chill.get_song_count()} songs, {chill.get_total_duration()}s):")
    for s in chill.songs:
        print(f"  - {s}")
    print()

    alice.delete_playlist(workout)
    print(f"After deleting '{workout.name}':")
    print(f"  Library still has {library.get_song_count()} songs")
    print(f"  '{chill.name}' still has {chill.get_song_count()} songs")
    print(f"  'Yellow' still exists: {yellow.title}")