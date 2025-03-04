# Technical Interview Round

## Part 1 - Code Review

In this task you are asked to review a PR that has been created by a junior developer. The PR includes two new files, `library.py` and `libraryTest.py`.
The junior developer has been asked to implement a simple library that can be used to store and retrieve books. They have not been asked to implement deletions or updates.

Your task is to review the PR and provide feedback on the implementation.

For the purpose of this interview, you should modify the code so that it satisfies your idea of 'production ready'.


## Part 2 - Legal Document Search Challenge

### Files

- **search.py**: Main file where you'll implement your search functionality
- **searchTest.py**: Test suite to validate your implementation

### What to Modify

Implement the `search_documents` function in `search.py`:

```python
def search_documents(query: str, documents: DocumentDatabase, top_n: int = 5) -> List[SimilarityScore]:
    """
    Search for legal documents matching a text query.
    
    Returns:
        List of SimilarityScores ordered by relevance
    """
    # Your code here
    pass
```

You can create any additional helper functions you need. Use any approach you prefer.

