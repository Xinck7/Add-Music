import argparse
from pytube import Playlist

# Script downloads the videos in the place that the script runs

# Parse arguments for the playlist
parser = argparse.ArgumentParser()
parser.add_argument("url",type=str)
args = parser.parse_args()

URL = args.url

# Defines playlist as python object
playlist = Playlist(URL)

# Show how many URL's downloading
print("Collected this many videos to download")
print(len(playlist.video_urls))

# physically downloading the audio track
print("Starting to download...")
for video in playlist.videos:
    videoStream = video.streams.get_by_itag('22')
    videoStream.download()

print("Downloading complete!")