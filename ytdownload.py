from pytube import Playlist

playlist_url = "ссылка_на_плейлист"

playlist = Playlist(playlist_url)

count = 0
for video in playlist.videos:
    try:
        audio = video.streams.filter(only_audio=True).first()
        audio.download(output_path="D:\\Downloads\\music", filename_prefix="")
        count += 1
    except Exception:
        continue
    print(f"Downloaded {count}")

print("Done")
