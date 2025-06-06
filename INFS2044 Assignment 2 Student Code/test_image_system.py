# Import the ImageEntry class representing image data with path, labels abd feature vector
from image_entry import ImageEntry

# Import IndexAccess which manages a collection of ImageEntry objects
from index_access import IndexAccess

# Import MatchingEngine used for calculating the similarity between image vectors
from matching_engine import MatchingEngine

# Import numpy for handling numerical arrays
import numpy as np

# Test function to check that adding an entry works correctly
def test_add_entry():
    index = IndexAccess() # Create a new image index
    entry1 = ImageEntry("img1.jpg", ["car", "person"], np.array({1, 0, 1})) # Create a new image entry
    index.add_entry(entry1) # Add the entry to the index
    assert len(index.get_all()) == 1 # Verify that exactly one entry was added

# Test function to check label matching when all labels must match
def test_find_by_all_labels():
    index = IndexAccess() # Create a new index
    entry = ImageEntry("img1.jpg", ["car", "person"], np.array([1, 1, 0])) # Create entry with with two labels
    index.add_entry(entry) # Add it to the index
    result = index.find_by_labels(True, ["car", "person"]) # Search for entry requiring both labels
    assert len(result) == 1 # Expect one match

