import matplotlib.image as mpimg # Import library to read image files

class ImageAccess:
    def load_image(self, path): # Define a method to load an image from a given path
        return mpimg.imread(path) # Return the image as a numpy array