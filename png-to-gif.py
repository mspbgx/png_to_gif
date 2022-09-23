# pip requirements
# - pillow
from PIL import Image
import glob

input_directory = "pictures_to_gif"
output_filename = "png_to_gif"

images = glob.glob(input_directory + "/*.png")
frames = []

for image in sorted(images):
    new_frame = Image.open(image)
    frames.append(new_frame)

frames[0].save(output_filename + ".gif", format='GIF', append_images=frames[1:], save_all=True, duration=1500, loop=0)