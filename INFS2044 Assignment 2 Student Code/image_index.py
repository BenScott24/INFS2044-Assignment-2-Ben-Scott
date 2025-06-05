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