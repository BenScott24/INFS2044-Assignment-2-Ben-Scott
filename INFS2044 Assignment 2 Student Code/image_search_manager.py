from image_entry import ImageEntry # Import ImageEntry class
from object_detection_engine import ObjectDetectionEngine # Import ObjectDetectionEngine class
from image_access import ImageAccess # Import ImageAccess class
from index_access import IndexAccess # Import IndexAccess class
from matching_engine import MatchingEngine # Import MatchingEngine class

class ImageSearchManager:
    def __init__(self): # Constructor for ImageSearchManager
        self.detector = ObjectDetectionEngine() # Create object detection engine
        self.access = ImageAccess() # Create image access object
        self.index = IndexAccess() # Create index access object

    def add_image(self, path): # Add image to index
        image = self.access.load_image(path) # Load image from file
        labels = self.detector.detect_objects(image) # Detect objects in image
        vector = self.detector.encode_labels(labels) # Convert labels into a vector
        entry = ImageEntry(path, labels, vector) # Create new image entry
        self.index.add_entry(entry) # Add entry to index
        print("Detected objects " + ",".join(sorted(labels))) # Print detected objects
    
    def search(self, all_mode, labels): # Search index for images
        return self.index.find_by_labels(all_mode, labels) # Return matching entries