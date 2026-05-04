from ytmusicapi import YTMusic

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