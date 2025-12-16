import os
from PIL import Image

def convert_tiff_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.tif', '.tiff')):
            tiff_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(output_folder, png_filename)

            # Open and convert
            with Image.open(tiff_path) as img:
                img.save(png_path, format='PNG')
                print(f"Converted: {filename} -> {png_filename}")

# Example usage
input_folder = 'tiff'
output_folder = 'pngs'
convert_tiff_to_png(input_folder, output_folder)
