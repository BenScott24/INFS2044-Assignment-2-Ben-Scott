class IndexAccess:
    def __init__(self): # Constructor
        self.entries = [] # List to hold image entries

    def add_entry(self, entry): # Add image entry
        for index in self.entries: # Check for duplicates
            if index.path == entry.path:
                return # Skip if duplicate
        self.entries.append(entry) # Add new entry

    def get_all(self): # Get all entries, sorted by path
        sorted_entries = [] # New list for sorted entries
        for entry in self.entries: # Loop through unsorted entries
            inserted =  False # Track if inserted