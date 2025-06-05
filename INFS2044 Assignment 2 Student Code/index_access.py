class IndexAccess:
    def __init__(self): # Constructor
        self.entries = [] # List to hold image entries

    def add_entry(self, entry): # Add image entry
        for index in self.entries: # Check for duplicates
            if index.path == entry.path:
                return # Skip if duplicate
        self.entries.append(entry) # Add new entry

    