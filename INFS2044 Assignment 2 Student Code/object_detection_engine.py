from object_detector import detect_objects, encode_labels # Import from detector
import numpy as np # Import numpy for vector handling

class ObjectDetectionEngine:
    def detect_objects(self, image): # Detect objects in image
        return list(detect_objects(image)) # Return detected labels as a list