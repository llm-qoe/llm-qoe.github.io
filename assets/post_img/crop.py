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
crop_area = (0, 75, 1895, 1000)  # Adjust these values to your needs

# Call the function with paths and crop area
crop_gif('original.gif', 'qoe-comparison.gif', crop_area)
