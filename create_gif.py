
import os
import imageio.v3 as iio

def create_gif(filenames, output_path):
    images = []
    for filename in filenames:
        if os.path.exists(filename):
            images.append(iio.imread(filename))
        else:
            raise FileNotFoundError(f"'No suh file: '{filename}'")
    iio.imwrite(output_path, images, duration=500, loop=0)