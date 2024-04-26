from PIL import Image, ImageSequence

def crop_gif(input_gif_path, output_gif_path, crop_area):
    # Open the original GIF
    img = Image.open(input_gif_path)

    # Create a list to hold the cropped frames
    frames = []

    # Iterate through each frame of the GIF
    for frame in ImageSequence.Iterator(img):
        # Copy the frame to ensure we don't alter the original image
        frame = frame.copy()

        # Crop the frame
        cropped_frame = frame.crop(crop_area)

        # Append the cropped frame to the list
        frames.append(cropped_frame)

    # Save the frames as a new GIF
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=img.info['duration'], loop=0)

# Define the crop area (left, upper, right, lower)
crop_area = (0, 75, 1895, 1000)  
crop_gif('original.gif', 'qoe-comparison.gif', crop_area)


# from PIL import Image

# # Open the GIF file
# gif_path = "example.gif"
# gif = Image.open(gif_path)

# # Get the duration of each frame in the GIF
# frame_durations = []
# for frame in ImageSequence.Iterator(gif):
#     if 'duration' in frame.info:
#         duration = frame.info['duration'] / 1000  # Convert milliseconds to seconds
#         frame_durations.append(duration)

# # Calculate the total duration of the GIF
# total_duration = sum(frame_durations)

# print(f"Total duration of the GIF: {total_duration} seconds")