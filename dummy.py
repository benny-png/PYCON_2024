from youtube_mix_dl import YoutubeMixDownloader

# Initialize the downloader
downloader = YoutubeMixDownloader(output_path="/home/ai-beast/Videos")

# Define a progress callback (optional)
def progress_callback(message):
    print(message)

# Create downloader with callback
downloader = YoutubeMixDownloader(
    output_path="downloads",
    progress_callback=progress_callback
)

# Download a mix
mix_url = "https://www.youtube.com/watch?v=Mude7cCSs9s&list=RDMude7cCSs9s&start_radio=1"
num_videos = 25
successful_downloads = downloader.download_mix(mix_url, num_videos)

print(f"Downloaded {successful_downloads} videos successfully")