from argparse import ArgumentParser, FileType
from pathlib import Path
from .detector import detect
from single_frame_detector import __version__

parser = ArgumentParser(
    description='Detect strange single frames in video.',
    prog="single_frame_detector",
)

def directory(path: str):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

parser.add_argument(
    'input',
    type=FileType('rb'),
    help="The video file to review."
)
parser.add_argument(
    '--output',
    type=directory,
    default=".",
    help="What folder to output the files in. (default: current directory)"
)
parser.add_argument(
    '--tolerance',
    type=int,
    default=80,
    help="How different should a frame be from it's siblings to be saved? From 0-100. (default: 80)"
)
parser.add_argument(
    '--image-format',
    default="png",
    help="The format to save the images in. (default: png)"
)
parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s ' + __version__
)

args = parser.parse_args()

detect(
    args.input,
    args.output,
    tolerance=args.tolerance,
    image_format=args.image_format,
)
