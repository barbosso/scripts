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


# or use ./yt-dlp.exe --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist https://music.youtube.com/playlist?list=XXXXX
