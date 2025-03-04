from typing import List

from src.search.DocumentDatabase import DocumentDatabase
from src.search.SimilarityScore import SimilarityScore


def print_results(results: List[SimilarityScore], database: DocumentDatabase):
    if not results:
        print("No results found.")
        return

    for result in results:
        print(f"- {result.document_id} (Score: {result.similarity_score:.4f}): {database.get(result.document_id)}")
