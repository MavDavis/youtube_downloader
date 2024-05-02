from pytube import YouTube

video_url = input("Enter the YouTube video URL: ")

yt = YouTube(video_url)

print("Title: ", yt.title)

streams = yt.streams.all()

print("Available qualities:")
for stream in streams:
    print(stream.resolution)

quality = input("Enter the quality of video you want to download: ")
# stream for stream in streams loops through the streams gotten from the youtube url and we then check if the user input exist in that stream
available_streams = [stream for stream in streams if stream.resolution == quality]
if available_streams:
    yd = available_streams[0]
    yd.download('/Users/davidmarvelous/Downloads')
else:
    print("Sorry, the chosen quality is not available for this video.")
