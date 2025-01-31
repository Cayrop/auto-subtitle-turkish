import os
import ffmpeg
import whisper
import argparse
import warnings
import tempfile
from transformers import pipeline
from .utils import str2bool, write_srt, filename

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("directory", type=str, help="path to the directory containing video files")
    parser.add_argument("--model", default="large-v3-turbo",
                        choices=whisper.available_models(), help="name of the Whisper model to use")
    parser.add_argument("--verbose", type=str2bool, default=False,
                        help="whether to print out the progress and debug messages")
    parser.add_argument("--translate_to_turkish", type=str2bool, default=True,
                        help="whether to translate subtitles to Turkish")
    args = parser.parse_args()

    directory = args.directory
    model_name = args.model
    translate_to_turkish = args.translate_to_turkish

    translation_pipeline = pipeline("translation",
                                    model="Helsinki-NLP/opus-mt-tc-big-en-tr") if translate_to_turkish else None
    if model_name.endswith(".en"):
        warnings.warn(
            f"{model_name} is an English-only model, forcing English detection.")

    model = whisper.load_model(model_name)
    video_files = get_video_files(directory)
    audios = extract_audio(video_files)

    for video_path, audio_path in audios.items():
        srt_path = os.path.splitext(video_path)[0] + ".srt"
        print(f"Generating subtitles for {filename(video_path)}...")

        result = model.transcribe(audio_path)

        with open(srt_path, "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)

        if translate_to_turkish:
            turkish_srt_path = os.path.splitext(video_path)[0] + "_tr.srt"
            with open(turkish_srt_path, "w", encoding="utf-8") as srt:
                translated_segments = []
                for segment in result["segments"]:
                    translated_text = translation_pipeline(segment["text"])[0]["translation_text"]
                    translated_segment = segment.copy()
                    translated_segment["text"] = translated_text
                    translated_segments.append(translated_segment)
                write_srt(translated_segments, file=srt)
            print(f"Created Turkish subtitle file: {turkish_srt_path}")


def get_video_files(directory):
    """Retrieve all .mp4 and .webp video files from a directory and its subdirectories."""
    video_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".mp4", ".webm")):
                video_files.append(os.path.join(root, file))
    return video_files


def extract_audio(video_files):
    """Extract audio from video files."""
    temp_dir = tempfile.gettempdir()
    audio_paths = {}

    for video_path in video_files:
        try:
            print(f"Extracting audio from {filename(video_path)}...")
            output_path = os.path.join(temp_dir, f"{filename(video_path)}.wav")
            ffmpeg.input(video_path).output(
                output_path,
                acodec="pcm_s16le", ac=1, ar="16k"
            ).run(quiet=True, overwrite_output=True)
            audio_paths[video_path] = output_path
        except Exception as e:
            print(e)
            try:
                print(f"Extracting audio from {filename(video_path)}...")
                output_path = os.path.join(temp_dir, f"{filename(video_path)}.wav")
                ffmpeg.input(video_path).output(
                    output_path,
                    acodec="pcm_s16le", ac=1, ar="16k"
                ).run(overwrite_output=True)
                audio_paths[video_path] = output_path
            except Exception as a:
                print(a)

    return audio_paths


if __name__ == '__main__':
    main()
