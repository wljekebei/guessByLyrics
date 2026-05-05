from ytmusicapi import YTMusic
import random

yt = YTMusic()

# search_results = yt.search('Oasis Wonderwall')
# print(search_results[0]['title'], 'by', search_results[0]['artists'][0]['name'])

# playlistName = input("Enter the name of the playlist: ")
# playlist = yt.search(playlistName, 'community_playlists')

# for i in range(5):
#     if (playlist[i]):
#         print(playlist[i]['title'], ' by ', playlist[i]['author'])

playlistURL = input('Enter playlist link: ')
playlistID = playlistURL.split("list=", 1)[1].split("&", 1)[0]
playlist = yt.get_playlist(playlistID)
# print(playlist['title'], 'by ', playlist['author']['name'])

while(True):
    print('\n')
    song = random.choice(playlist['tracks'])
    # print(song['title'], 'by ', song['artists'][0]['name'])

    videoId = song['videoId']
    watchPlaylist = yt.get_watch_playlist(videoId=videoId)
    lyricsBrowseId = watchPlaylist.get('lyrics')

    songLyrics = yt.get_lyrics(lyricsBrowseId, False)
    # print(songLyrics['lyrics'])
    words = songLyrics['lyrics'].split()
    wordCount = len(words)
    while (True):
        firstWord = random.randint(0, (wordCount - 11))
        if(words[firstWord][0].isupper() == True):
            break

    guessed = False
    points = 10
    for i in range(firstWord, (firstWord + 10)):
        print('[', (points), ' pt] ', words[i])
        guessedName = input("Song name: ")
        if (guessedName.upper() == song['title'].upper()):
            print('You guessed right! It is ', song['title'], ' by ', song['artists'][0]['name'], "\nYou got ", points, " points!")
            guessed = True
            break
        elif (guessedName == ''):
            points -= 1
            continue
        # elif (guessedName == 'stop'):
        #     break
        else:
            points -= 1
            print("Try again")

    if (guessed == False):
        print('The song was ', song['title'], ' by ', song['artists'][0]['name'])