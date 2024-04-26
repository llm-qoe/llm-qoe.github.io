import time
from transformers import GPT2Tokenizer
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import ImageSequenceClip

TTFT = 1
TDS = 0.05
# Question and output text
output_str = """In an LLM-based text streaming service, user experience centers around two key phases: the Wait Phase and the Digest Phase.

1. **Wait Phase**: This initial phase involves a short delay before text delivery begins. A delay of more than a few seconds can cause user impatience and potential abandonment of the service.

2. **Digest Phase**: After the initial wait, text is streamed continuously at a pace tailored to user demographics and application needs. This phase is crucial for user engagement, as it impacts the ease with which users can comprehend and interact with the content in real time.

**Quality of Experience (QoE)**: Overall user satisfaction hinges on the smooth and timely streaming of text, which should align with users' reading or listening speeds to optimize engagement and minimize frustration. The goal is to balance text delivery with users' processing capabilities to enhance the overall experience."""

# Initialize tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# Encode the output string
encoded_output = tokenizer.encode(output_str)
# Number of tokens
num_tokens = len(encoded_output)
print(f"Number of tokens: {num_tokens}")

def stream_text_good():
    token_ids = []  # List to accumulate token ids
    decoded_text = ""  # Decoded text to be appended to chatbot
    start_time = time.time()
    time1 = [0]
    time.sleep(TTFT-1)  # Simulate delay
    try:
        for i in range(num_tokens):
            now = time.time()
            token_ids.append(encoded_output[i])
            # if i % 3 == 0:  # Decode and update the chatbot every 3 tokens (~0.5s)
            decoded_text += tokenizer.decode(token_ids)
            token_ids = []
            sleep_time = TDS - (time.time() - now)
            if sleep_time > 0:
                time.sleep(sleep_time)
            time1.append(time.time() - start_time)
    
    except Exception as e:
        print(f"Error during text streaming: {e}")
    return time1

delay_ttft = 8
def stream_text_ttft():
    token_ids = []  # List to accumulate token ids
    decoded_text = ""  # Decoded text to be appended to chatbot
    start_time = time.time()
    time2 = [0]
    time.sleep(delay_ttft - 1)  # Simulate delay
    try:
        for i in range(num_tokens):
            now = time.time()
            token_ids.append(encoded_output[i])
            # if i % 3 == 0:  # Decode and update the chatbot every 3 tokens (~0.5s)
            decoded_text += tokenizer.decode(token_ids)
            token_ids = []
            sleep_time = TDS/2.8 - (time.time() - now)
            if sleep_time > 0:
                time.sleep(sleep_time)
            time2.append(time.time() - start_time)
    except Exception as e:
        print(f"Error during text streaming: {e}")
    return time2

def stream_text_fs():
    token_ids = []  # List to accumulate token ids
    decoded_text = ""  # Decoded text to be appended to chatbot
    start_time = time.time()
    time3 = [0]
    time.sleep(TTFT-1)  # Simulate delay
    try:
        for i in range(num_tokens):
            now = time.time()
            token_ids.append(encoded_output[i])
            # if i % 3 == 0:  # Decode and update the chatbot every 3 tokens (~0.5s)
            decoded_text += tokenizer.decode(token_ids)
            token_ids = []
            if i < 20:
                sleep_time = TDS*3.5 - (time.time() - now)
            else:
                sleep_time = TDS/2.2 - (time.time() - now)
            if sleep_time > 0:
                time.sleep(sleep_time)
            time3.append(time.time() - start_time)
    except Exception as e:
        print(f"Error during text streaming: {e}")
    return time3


def main():
    # Create a Gradio interface
    # Generate frames
    images = []

    # initialize the time and # tokens
    times1 = stream_text_good()
    times2 = stream_text_ttft()
    times3 = stream_text_fs()

    tokens = list(np.arange(0, num_tokens + 1))

    frames = 360  # Number of frames to generate
    max_time = 13
    # align the start point
    times2[1:] = [x + delay_ttft - times2[1] for x in times2[1:]]

    # align the end point
    times1[1:] = [(x - times1[1]) * (max_time - times1[1]) / (times1[-1] - times1[1]) + times1[1] for x in times1[1:]]
    times2[1:] = [(x - times2[1]) * (max_time - times2[1]) / (times2[-1] - times2[1]) + times2[1] for x in times2[1:]]
    times3[1:] = [(x - times3[1]) * (max_time - times3[1]) / (times3[-1] - times3[1]) + times3[1] for x in times3[1:]]
    duration = 15.32  # Duration of the video in seconds
    timesticks = np.linspace(0, duration, frames)

    import json
    with open('times1.json', 'w') as f:
        json.dump(times1, f)
    with open('times2.json', 'w') as f:
        json.dump(times2, f)
    with open('times3.json', 'w') as f:
        json.dump(times3, f)

    import bisect
    def find_insert_position(sorted_list, num):
        position = bisect.bisect_left(sorted_list, num)
        return position
    
    for i in range(frames):
        plt.figure(figsize=(12, 3))  # Adjusted figure size to accommodate three subplots

        # First subplot: varying frequency
        ax1 = plt.subplot(1, 3, 1)
        time = timesticks[i]
        index1 = find_insert_position(times1, time)
        plt.plot(times1[:index1], tokens[:index1], label='Tokens Processed', color='blue')
        plt.xlim(0, duration)
        plt.ylim(0, tokens[-1])
        # plt.title(f"QoE-aware Server", loc='center', verticalalignment='bottom')
        # plt.figtext(0.5, 0.01, "QoE-aware Server", ha="left", va="bottom", fontsize=12)

        # Second subplot: varying phase
        ax2 = plt.subplot(1, 3, 2)
        time = timesticks[i]
        index2 = find_insert_position(times2, time)
        # print(index2)
        # print(times2[:index2])
        plt.plot(times2[:index2], tokens[:index2], label='Tokens Processed', color='blue')
        plt.xlim(0, duration)
        plt.ylim(0, tokens[-1])
        # plt.title(f"QoE-unaware Server 1", loc='center', verticalalignment='bottom')
        # plt.figtext(0.5, 0.01, "QoE-unaware Server 1", ha="center", va="bottom", fontsize=12)

        # Third subplot: varying amplitude
        ax3 = plt.subplot(1, 3, 3)
        time = timesticks[i]
        index3 = find_insert_position(times3, time)
        plt.plot(times3[:index3], tokens[:index3], label='Tokens Processed', color='blue')
        plt.xlim(0, duration)
        plt.ylim(0, tokens[-1])
        # plt.title(f"QoE-unaware Server 2", loc='center', verticalalignment='bottom')
        # plt.figtext(0.5, 0.01, "QoE-unaware Server 2", ha="right", va="bottom", fontsize=12)

        for ax in [ax1, ax2, ax3]:
        # Setting x and y axis labels
            ax.set_xlabel('Time')
            ax.set_ylabel('#Tokens')

            # Removing the top and right spines to create axes with arrows but not boxes
            ax.spines['top'].set_color('none')
            ax.spines['right'].set_color('none')

            # Moving bottom spine to zero position
            ax.spines['bottom'].set_position(('data',0))
            # Adding arrow to the bottom spine
            ax.spines['bottom'].set_capstyle('projecting')
            ax.plot((1), (0), ls="", marker=">", ms=10, color="k", transform=ax.get_yaxis_transform(), clip_on=False)

            # Moving left spine to zero position
            ax.spines['left'].set_position(('data',0))
            # Adding arrow to the left spine
            ax.spines['left'].set_capstyle('projecting')
            ax.plot((0), (1), ls="", marker="^", ms=10, color="k", transform=ax.get_xaxis_transform(), clip_on=False)

            # Hiding the axes ticks
            ax.xaxis.set_ticks_position('none') 
            ax.yaxis.set_ticks_position('none')

            # Hiding the axes tick labels
            ax.set_xticklabels([])
            ax.set_yticklabels([])

        # Save plot to a PNG file
        filename = f'/tmp/frame_{i:03d}.png'
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        images.append(filename)

    # This can take a little while as it's generating many images

    # Create a video from images
    clip = ImageSequenceClip(images, fps=frames / duration)
    clip.write_videofile("tokens_three_subplots.mp4", fps=24)  # Output video file

    # Cleanup (optional): Remove image files after creating the video
    import os
    for filename in images:
        os.remove(filename)


if __name__ == "__main__":
    main()

# ffmpeg -i tokens_three_subplots.mp4 num_tokens.gif -y
