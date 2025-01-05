import yt_dlp


TELEGRAM_TOKEN = ""


def download_video_from_yt(url: str, quality: str = 'best', file_format: str = 'mp4'):
    ydl_opts = {
        'format': quality,
        'outtmpl': f'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': file_format,
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info_dict)


url = input('Paste link: ')
quality = str(input('Paste Quality: '))

download_video_from_yt(url, quality)
