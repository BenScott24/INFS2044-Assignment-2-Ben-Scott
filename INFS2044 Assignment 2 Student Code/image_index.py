import json # Import JSON module for file saving/loading
import os # Import OS module to check file existence

class ImageIndex:
    def __init__(self, filename="images.json"): # Constructor that sets the index filename
        self.filename = filename # Store the filename for saving/loading
        self.index = {} # Dictionary to hold image paths and labels
        self.load() # Load data from file if available

    def add_image(self, path, labels): # Add image and its label to index
        self.index[path] = list(labels) # Store labels as a list
        self.save() # Save the updated index to the file
    
    def get_all(self): # Return the entire index
        return self.index
    
    def search(self, all_mode, query_labels): # Search for images by labels
        matches = {} # Dictionary to store matching results
        for path, labels in self.index.items(): # Loop through all indexed images
            if all_mode and all(label in labels for label in query_labels): # Match all labels
                matches[path] = labels
            elif not all_mode and any(label in labels for label in query_labels): # Match any label
                matches[path] = labels
        return matches # Return matching images
    
    def load(self): # Load index from file
        if os.path.exists(self.filename): # Check if file exists
            with open(self.filename, "r") as f:
                self.index = json.load(f) # Load the JSON content into dictionary

    def save(self): # Save index to file
        with open(self.filename, "w") as f: # Open file for writing
            json.dump(self.index, f) # Write dictionary to JSON file