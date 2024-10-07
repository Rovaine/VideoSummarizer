import os
import subprocess
from KeyFrameFind import save_keyframe
def split_video(video_path, output_folder, segment_duration=90):
    # Get duration of the video
    ffprobe_command = f'ffprobe -i "{video_path}" -show_entries format=duration -v quiet -of csv="p=0"'
    duration_output = subprocess.check_output(ffprobe_command, shell=True, stderr=subprocess.STDOUT)
    duration = float(duration_output.decode())

    # Check if video is longer than 90 seconds
    if duration > segment_duration:
        # Calculate number of segments
        num_segments = int(duration / segment_duration)

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Split the video into segments
        for i in range(num_segments):
            start_time = i * segment_duration
            output_file = os.path.join(output_folder, f"segment_{i+1}.mp4")
            ffmpeg_command = f'ffmpeg -i "{video_path}" -ss {start_time} -t {segment_duration} -c:v copy -c:a copy "{output_file}"'
            subprocess.run(ffmpeg_command, shell=True, stderr=subprocess.PIPE)
    else:
        print("Video duration is less than 90 seconds. No need to split.")

def process_segments(segment_folder):
    # Iterate through segment files
    for filename in os.listdir(segment_folder):
        if filename.endswith(".mp4"):
            segment_path = os.path.join(segment_folder, filename)
            # Call the blackbox function on each segment
            save_keyframe(segment_path)


# Example usage:
#video_path = "Videos/TestVideo2.webm"
#output_folder = "tryfile"
#segment_duration = 90

split_video(video_path, output_folder, segment_duration)
process_segments(output_folder)
