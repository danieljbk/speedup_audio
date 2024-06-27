import os
from pydub import AudioSegment
from pydub.effects import speedup


def speed_up_audio(input_file, output_file, speed_factor=1.25):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Speed up the audio without changing pitch
    fast_audio = speedup(audio, playback_speed=speed_factor)

    # Export the new audio
    fast_audio.export(output_file, format=output_file.split(".")[-1])


def process_folder(input_folder, output_folder, speed_factor=1.25):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".wav", ".mp3", ".flac", ".ogg")):
            output_filename = filename.split(".")
            output_filename = (
                f"{speed_factor}_{output_filename[0]}.{output_filename[1]}"
            )
            # Add or remove audio formats as needed
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, output_filename)

            print(f"Processing: {filename}")
            speed_up_audio(input_path, output_path, speed_factor)
            print(f"Saved: {output_filename}")


# Example usage
input_folder = "./input"
output_folder = "./output"
speed_factor = 1.3

process_folder(input_folder, output_folder, speed_factor)
