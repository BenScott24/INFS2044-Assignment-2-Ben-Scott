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

@main.command() # Define 'search' command
@click.argument("labels", nargs=-1) # Accept multiple labels
@click.option("--all", "all_mode", is_flag = True, help="All labels must match") # Match all
@click.option("--some", "some_mode", is_flag = True, help="At least one label must match") # Match some
def search(labels, all_mode, some_mode): # Search function
    if not all_mode and not some_mode: # Ensure mode is selected
        print("Use either --all or --some") # Print message
        return
    all_mode = all_mode or not some_mode # Default to all if not specified
    index = ImageIndex() # Load index
    results = index.search(all_mode, labels) # Search for matches
    for path, labels_found in results.items(): # Print results
        print(f"{path}: {','.join(labels_found)}")
    print(f"{len(results)} matches found.") # Show number of matches


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
