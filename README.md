# Single Frame Detector

Ever watched a video and saw that its creator put in a little single-frame
Easter egg? If you're like me, you spent a solid two minutes on your
phone trying to pause the video at just the right moment to see it.
Why are we acting like cavemen, however, when we have technology? This is what
`single-frame-detector` aims to solve.

### Installation 
You know the deal: `git clone`, `cd`, and `poetry install`

## Performance
Yes, it's slow. Very slow. As far as I can tell, there's no way for
one to trivially paraellize accessing the frames of a video with
PyAV, and I'm relying on Python too much instead of NumPy, meaning this program is very slow. This could probably run faster if I made more clever use of NumPy, but I actually think that this is probably more representative
of me hitting the upper limits of what can reasonably be done with Python.
It's probably time that I start learning C/C++/Rust/Go.

## Help
Use `python -m single_frame_detector --help` to always get the most
up-to-date help.

```
usage: single_frame_detector [-h] [--output OUTPUT] [--tolerance TOLERANCE]
                             [--image-format IMAGE_FORMAT] [--version]
                             input

Detect strange single frames in video.

positional arguments:
  input                 The video file to review.

options:
  -h, --help            show this help message and exit
  --output OUTPUT       What folder to output the files in. (default: current
                        directory)
  --tolerance TOLERANCE
                        How different should a frame be from it's siblings to
                        be saved? From 0-100. (default: 80)
  --image-format IMAGE_FORMAT
                        The format to save the images in. (default: png)
  --version             show program's version number and exit
```
