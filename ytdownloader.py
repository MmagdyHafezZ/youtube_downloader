import os
import sys
import threading
import time
from pytube import YouTube

def progress_function(stream, chunk, bytes_remaining):
    global filesize
    percent = (100 * (filesize - bytes_remaining)) / filesize
    progress = int(50 * percent // 100)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('  [{bar}] {percent:.1f}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def simulate_loading_effect(message):
    cursor = '|/-\\'
    idx = 0
    while loading:
        print(f'\r{message} {cursor[idx % len(cursor)]}', end='', flush=True)
        idx += 1
        time.sleep(0.1)

def download_video(youtube_url):
    try:
        global loading
        print("Getting video information...")
        yt = YouTube(youtube_url, on_progress_callback=progress_function)

        loading = True
        t = threading.Thread(target=simulate_loading_effect, args=("Getting video streams...",))
        t.start()
        video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        loading = False
        t.join()
        
        global filesize
        filesize = video.filesize

        output_directory = "downloads"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"Downloading: {yt.title}")
        video.download(output_directory)
        print("\nDownload completed!! Video saved in", output_directory, "folder\n")
    except Exception as e:
        loading = False
        print("\rError:", str(e))

def main():
    print("Welcome to the YouTube Downloader!")
    while True:
        link = input("\nEnter the link of the YouTube video you want to download (or type 'exit' to quit): ").strip()
        if link.lower() == 'exit':
            print("Thank you for using the YouTube Downloader. Goodbye!")
            break
        elif "youtube.com" in link:
            download_video(link)
        else:
            print("Invalid URL. Please ensure it's a valid YouTube link.")

if __name__ == "__main__":
    main()
