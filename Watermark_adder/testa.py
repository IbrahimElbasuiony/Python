from moviepy.editor import VideoFileClip , AudioFileClip


video_path = r"C:\Users\ibrah\Downloads\Video\output_video.mp4"
audio_path = r"C:\Users\ibrah\Downloads\Video\output_audio.wav"

# Load the video clip
video_clip = VideoFileClip(video_path)

# Load the audio clip
audio_clip = AudioFileClip(audio_path)

# Set the audio of the video clip to the loaded audio
video_clip = video_clip.set_audio(audio_clip)

# Specify the path to save the output video with audio
output_path = r'C:\Users\ibrah\Downloads\Video\output_video_with_audio.mp4'

# Write the video with combined audio to the specified file
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Close the video and audio clips
video_clip.close()
audio_clip.close()