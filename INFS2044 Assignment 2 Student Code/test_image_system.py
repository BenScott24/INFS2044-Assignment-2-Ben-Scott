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
    entry1 = ImageEntry("img1.jpg", ["car", "person"], np.array([1, 0, 1])) # Create a new image entry
    index.add_entry(entry1) # Add the entry to the index
    assert len(index.get_all()) == 1 # Verify that exactly one entry was added

# Test function to check label matching when all labels must match
def test_find_by_all_labels():
    index = IndexAccess() # Create a new index
    entry = ImageEntry("img1.jpg", ["car", "person"], np.array([1, 1, 0])) # Create entry with with two labels
    index.add_entry(entry) # Add it to the index
    result = index.find_by_labels(True, ["car", "person"]) # Search for entry requiring both labels
    assert len(result) == 1 # Expect one match

# Test function to check label matching when any label can match
def test_find_by_some_labels():
    index = IndexAccess() # Create a new index
    index.add_entry(ImageEntry("img1.jpg", ["cat"], np.array([0, 0, 1]))) # Add an entry with label "cat"
    result = index.find_by_labels(False, ["cat", "dog"]) # Search all allowing any label match ("cat" or "dog")
    assert len(index.get_all()) == 1 # Confirm that one entry exists in the index

# Test function for MatchingEngine to verify similarity calculation
def test_matching_engine_similarity():
    entries = [
        ImageEntry("img1.jpg", ["car"], np.array([1, 0])), # First entry with vector [1,0]
        ImageEntry("img2.jpg", ["bike"], np.array([0,1]))  # Second entry with vector [0, 1]
    ]
    matcher = MatchingEngine(entries) # Create a matcher using the entries
    result = matcher.find_similar(np.array([1, 0]), 1) # Find top 1 similar entry to vector [1, 0]
    assert result[0][1].path == "img1.jpg" # Expect the most similar to be img1.jpg

# Test function to check getters for path, labels, and vector
def test_image_entry_properties():
    vector = np.array([0.5, 0.5]) # Create a test vector
    entry = ImageEntry("example.jpg", ["tree", "sky"], vector) # Create image entry with path, labels vector
    assert entry.path == "example.jpg" # Check image path
    assert entry.labels == ["tree", "sky"] # Check labels
    assert np.array_equal(entry.vector, vector) # Check vector match

# Test function to check multiple entries are added to index
def test_multiple_entries_added():
    index = IndexAccess() # Create a new image index
    entry1 = ImageEntry("img1.jpg", ["car"], np.array([1, 0])) # First image entry
    entry2 = ImageEntry("img2.jpg", ["dog"], np.array([0, 1])) # Second image entry
    index.add_entry(entry1) # Add first entry
    index.add_entry(entry2) # Add second entry
    assert len(index.get_all()) == 2 # Confirm two entries were added