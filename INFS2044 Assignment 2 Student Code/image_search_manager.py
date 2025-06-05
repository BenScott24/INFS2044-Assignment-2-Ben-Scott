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
