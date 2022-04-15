from pathlib import Path
import numpy as np
from typing import BinaryIO, Tuple
import av
from math import sqrt

class Progress:
    def __init__(self, total: int):
        self.total = total
        self.amount = 0
    
    def __iadd__(self, other: int):
        self.amount += other
        print(f"{(self.amount/self.total):%}  ({self.amount}/{self.total})")
        return self

def distance(a: int, b: int) -> int:
	red = a[0] - b[0]
	green = a[1] - b[1]
	blue = a[2] - b[2]
	return sqrt(red ** 2 + green ** 2 + blue ** 2)


def difference(left, right):
	left_array = left.to_rgb().to_ndarray().reshape((left.width * left.height, 3))
	right_array = right.to_rgb().to_ndarray().reshape((right.width * right.height, 3))

	count = 0
	for left_pixel, right_pixel in zip(left_array, right_array):
		# TODO: Should user be able to control tolerance?
		# Max is about 440
		if distance(left_pixel, right_pixel) > 100:
			count += 1
	return count

def detect(
    input: BinaryIO,
    output: Path,
    tolerance: float,
    image_format: str
):
	with av.open(input) as input:
		# Get input video frames
		input_stream: av.stream.Stream = input.streams.video[0]
		frames = tuple(input.decode(input_stream))

		number_of_frames = len(frames)
		progress = Progress(number_of_frames - 1)

		for i in range(1, number_of_frames):
			previous_frame = frames[i - 1]
			frame = frames[i]
			if i == (number_of_frames - 1):
				next_frame = None
			else:
				next_frame = frames[i + 1]

			previous_current_diff = difference(previous_frame, frame)
			if (previous_current_diff / (frame.width * frame.height)) * 100 >= tolerance:
				if next_frame != None:
					next_current_diff = difference(next_frame, frame)
					if (next_current_diff / (frame.width * frame.height)) * 100 >= tolerance:
						print(f"Frame {frame.index} has both frames different!")
						frame.to_image().save(output / f"frame-{frame.index}.{image_format}")
				else:
					print(f"Frame {frame.index} has its previous frame different!")
					frame.to_image().save(output / f"frame-{frame.index}.{image_format}")
			progress += 1
