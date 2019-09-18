import os
import random
import numpy as np
from scipy import ndarray

import skimage as sk
from skimage import io
from skimage import util
from skimage import transform


def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-178, 53)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    # add random noise to the image
    image_array_rotated = random_rotation(image_array)
    return sk.util.random_noise(image_array_rotated)

def fliplr(image_array: ndarray):
    # Flips the image from left to right
    image_array_rotated = random_rotation(image_array)
    return np.fliplr(image_array_rotated)

def flipud(image_array: ndarray):
    # Flips the image from left to right
    image_array_rotated = random_rotation(image_array)
    return np.flipud(image_array_rotated)

# dictionary of the transformations we defined earlier
available_transformations = {
    'noise': random_noise,
    'fliplr': fliplr,
    'flipud': flipud
}

folder_path = '/your/custom/path/'
# find all image paths from the folder
images = [ result for result in [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))] if result.endswith((".jpg",".JPG",".jpeg",".JPEG"))]

num_generated_files = 0
processed_filenames = []
for image in images:
    file_name = image.rsplit('/')[-1].split('.')[0]
    if not file_name.split('_')[0] in processed_filenames:
        processed_filenames.append(file_name)
        # read image as an two dimensional array of pixels
        image_to_transform = sk.io.imread(image)

        transformed_image = None
        for transformation in available_transformations:
            # random transformation to apply for a single image
            transformed_image = available_transformations[transformation](image_to_transform)

            new_file_path = '%s/%s_%s.jpg' % (folder_path,file_name,transformation)

            # write image to the disk
            io.imsave(new_file_path, transformed_image)
        num_generated_files += 1
        print("image saved:",num_generated_files)
