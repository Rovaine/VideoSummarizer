from KeyFrameIdentifier import finalize_output, divide_video
from VideoSummarization import Video_summarize
from tryig import split_video, process_segments

video_path = "Videos/Goals.webm"
output_folder = "tryfile_2"
segment_duration = 90

if __name__ == "__main__":
    # 1. Load the video
    video_path = "Videos/GradientDescent.mkv"
    print(Video_summarize(video_path))
    split_video(video_path, output_folder, segment_duration)
    process_segments(output_folder)