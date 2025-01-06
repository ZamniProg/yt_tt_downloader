import yt_dlp


TELEGRAM_TOKEN = ""
QUAL = {'720': '22', '360': '18', '480': '135', '1080': '137', 'audio': '140'}


def download_video_from_yt(url: str, quality: str = 'best'):
    ydl_opts = {
        'format': quality,
        'outtmpl': f'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    if quality != '140':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            formats = info_dict.get('formats', [])

            if quality not in formats:
                print("Error: The format you selected is unavailable for this video")
            else:
                return ydl.prepare_filename(info_dict)
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")


url = input('Paste link: ')
quality = QUAL[input('Paste Quality: ')]

download_video_from_yt(url, quality)
