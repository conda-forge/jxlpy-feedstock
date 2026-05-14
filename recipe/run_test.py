from io import BytesIO

from PIL import Image
from jxlpy import JXLImagePlugin  # noqa: F401


def main():
    image = Image.new("RGB", (3, 2))
    pixels = [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 255),
        (7, 13, 29),
    ]
    image.putdata(pixels)

    buffer = BytesIO()
    image.save(buffer, format="JXL", lossless=True)
    assert buffer.tell() > 0

    buffer.seek(0)
    decoded = Image.open(buffer)
    decoded.load()

    assert decoded.format == "JXL"
    assert decoded.mode == "RGB"
    assert decoded.size == image.size
    assert decoded.tobytes() == image.tobytes()


if __name__ == "__main__":
    main()
