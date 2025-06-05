import json # Import JSON module for file saving/loading
import os # Import OS module to check file existence

class ImageIndex:
    def __init__(self, filename="images.json"): # Constructor that sets the index filename
        self.filename = filename # Store the filename for saving/loading
        self.index = {} # Dictionary to hold image paths and labels
        self.load() # Load data from file if available
        
        