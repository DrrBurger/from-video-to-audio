import moviepy.editor
from pathlib import Path

video_file = Path('Miyagi & Andy Panda - Minor (Mood Video).mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')

audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')
