import sys
import os
from PIL import Image


input_folder = sys.argv[1]

output_folder = sys.argv[2]


if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for item in os.listdir(input_folder):
	if item.lower().endswith('.jpg'):
		full_path = os.path.join(input_folder, item)

		img = Image.open(full_path)

		new_img = img.convert('RGB')
		name_without_ext, _ = os.path.splitext(item)
		save_path = os.path.join(output_folder, name_without_ext + '.png')
		new_img.save(save_path, "PNG")