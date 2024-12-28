import yt_dlp

def get_available_formats(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        resolutions = sorted(set([f.get('height') for f in formats if f.get('height')]), reverse=True)
        return resolutions

def download_video(url, format_choice, resolution_choice):
    ydl_opts = {}

    if format_choice == "1":  # MP4 Video
        ydl_opts = {
            'format': f'bestvideo[height={resolution_choice}]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',  # File name format
        }
    elif format_choice == "2":  # MP3 Audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',  # File name format
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("YouTube Downloader")
    url = input("Enter YouTube video URL: ")
    
    print("Choose format:\n1. MP4 Video\n2. MP3 Audio")
    format_choice = input("Enter your choice: ")
    
    if format_choice == "1":
        resolutions = get_available_formats(url)
        print("Available resolutions:")
        for res in resolutions:
            print(f"{res}p")
        resolution_choice = input("Enter your preferred resolution (e.g., 720): ")
    else:
        resolution_choice = None  # Audio doesn't need resolution choice
    
    try:
        download_video(url, format_choice, resolution_choice)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")