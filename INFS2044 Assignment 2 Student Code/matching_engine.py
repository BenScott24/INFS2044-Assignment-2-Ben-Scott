from sklearn.metrics.pairwise import cosine_similarity # Import cosine similarity

def get_similarity_score(item): # Helper function to get score
    return item[0]

class MatchingEngine:
    def __int__(self, entries): # Constructor
        self.entries = entries # Store list of image entries 

    def find_similar(self, vector, k): # Find similar vectors
        scores = [] # List of scores
        for entry in self.entries:
            sim = cosine_similarity([vector], [entry.vector])[0][0] # Calculate similarity
            scores.append((sim, entry)) # Store score and entry
        
        scores.sort(key=get_similarity_score, reverse=True) # Sort descending

        if k is None: # If no k specified
            return scores # Return all
        return scores[:k] # Return top k