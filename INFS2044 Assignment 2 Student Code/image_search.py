import click # Import click for CLI 
import matplotlib.image as mpimg # Import image loading
import numpy as np # Import numpy for vector operations
from object_detector import detect_objects, encode_labels # Import detection functions
from sklearn.metrics.pairwise import cosine_similarity # Import cosine similarity
from image_index import ImageIndex # Import image index 


@click.group() # Define a group of main commands
def main():
    pass # Do nothing (placeholder)


@main.command() # Define 'add' command
@click.argument('image_path', type=click.Path(exists=True)) # Accepts a valid path
def add(image_path): # Function to add image
    image = mpimg.imread(image_path) # Load image
    labels = detect_objects(image) # Detect labels
    index = ImageIndex() # Load image index
    index.add_image(image_path, labels) # Add image to index
    print("Detected objects " + ",".join(labels)) # Output labels

@main.command()
@click.option('--all/--some', default=True, show_default=True, help='List images that match all/some query terms')
@click.argument('terms', nargs=-1, required=True)
def search(all, terms):
    pass


@main.command()
@click.option('--k', default=None, type=click.IntRange(1), show_default=True, help='Number of matches to return')
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
def similar(k, image_path):
    pass

@main.command()
def list():
    pass


if __name__ == '__main__':
    main()
