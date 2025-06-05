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


@main.command() # Define 'similar' command
@click.argument('image_path', type=click.Path(exists=True)) # Accept path
@click.option('--k', type=int, default=None, help="Top K similar images") # Optional limit
def similar(image_path, k): # Similar image search
    image = mpimg.imread(image_path) # Load image
    labels = detect_objects(image) # Detect labels
    vector =  np.array(encode_labels(labels)) # Encode labels
    index = ImageIndex() # Load index
    entries = index.get_all() # Get all entries
    
    sims = [] # List of similarity scores
    for path, labels_found in entries.items(): # Loop through entries
        vec = np.array(encode_labels(labels_found)) # Encode labels from entry
        score = cosine_similarity([vector], [vec])[0][0] # Compute similarity
        sims.append((score, path)) # Store result

    sims.sort(reverse=True) # Sort by score descending
    if k: # If k is given
        sims = sims[:k] # Get top-k
    
    for score, path in sims: # Print results
        print(f"{score:} {path}")
    

@main.command()
def list():
    pass


if __name__ == '__main__':
    main()
