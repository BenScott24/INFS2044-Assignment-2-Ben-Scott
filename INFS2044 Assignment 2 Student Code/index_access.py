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
            for index in range(len(sorted_entries)): # Find correct position
                if entry.path < sorted_entries[index].path:
                    sorted_entries = sorted_entries[:index] + [entry] + sorted_entries[index:] # Insert entry
                    inserted = True # Mark as inserted
                    index = len(sorted_entries) # Exit loop