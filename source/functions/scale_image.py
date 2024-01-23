import os

import pygame

from source.functions.load_image import load_image


def scale_image(filename, x_scale, y_scale, final_directory, final_filename):
    original_img = load_image(f"original_files/{filename}")
    transformed_img = pygame.transform.scale(original_img, (original_img.get_width() * x_scale,
                                                            original_img.get_height() * y_scale))
    pygame.image.save(transformed_img, os.path.join(final_directory, final_filename))

