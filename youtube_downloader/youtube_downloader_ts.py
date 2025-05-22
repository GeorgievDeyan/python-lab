from pytube import YouTube
import subprocess
import os

def download_and_convert(url, output_path='.'):
    # Download the highest resolution video from YouTube
    yt = YouTube(url)
    print(f"Downloading video: {yt.title}")
    video = yt.streams.get_highest_resolution()
    downloaded_file = video.download(output_path=output_path)

    # Define output .ts filename
    base, _ = os.path.splitext(downloaded_file)
    output_ts = base + '.ts'

    # Use ffmpeg to convert video to .ts format with mp3 audio codec
    print(f"Converting {downloaded_file} to {output_ts} with MP3 audio codec...")
    command = [
        'ffmpeg',
        '-i', downloaded_file,
        '-c:v', 'copy',       # copy video codec (no re-encoding video)
        '-c:a', 'mp3',        # encode audio to mp3
        output_ts
    ]

    subprocess.run(command, check=True)
    print(f"Conversion complete. File saved as: {output_ts}")

    # Optionally remove original downloaded file
    # os.remove(downloaded_file)

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_and_convert(video_url)
