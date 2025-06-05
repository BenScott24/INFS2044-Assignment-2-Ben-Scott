class ImageEntry:
    def __init__(self, path, labels, vector): # Constructor to initialize image entry
        self.__path = path # Private variable to store image file path
        self.__labels = labels # Private variable to store labels of detected objects
        self.__vector = vector # Private variable to store encoded label vector

    def get_path(self): # Getter for image path
        return self.__path
    
    def get_labels(self): # Getter for labels
        return self.__labels
    
    def get_vector(self): # Getter for encoded label vector
        return self.__vector
    
    path = property(get_path) # Create a property for path using the getter
    labels = property(get_labels) # Create a property for labels using the getter
    vector = property(get_labels) # Create a property for vector using the getter