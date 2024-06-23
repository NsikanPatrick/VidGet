from pytube import YouTube

def download_videos(links, save_path):
    for link in links:
        try:
            yt = YouTube(link)
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            if streams:
                stream = streams.first()
                stream.download(save_path)
                print(f"Downloaded {link} successfully!")
            else:
                print(f"No 720p resolution available for {link}.")
        except Exception as e:
            print(f"An error occurred while downloading {link}: {e}")

links = ["https://www.youtube.com/the link"]
save_path = "C:/Users/Downloads"
download_videos(links, save_path)