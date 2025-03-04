from typing import List

from src.search.search import DocumentDatabase, search_documents, SimilarityScore
import unittest

from src.search.utils import print_results


class TestSearchImplementation(unittest.TestCase):
    def setUp(self):
        self.db = DocumentDatabase()
        self.db.bootstrap_with_test_data()

    # Test 1: Basic relevance (tests exact match across docs)
    def test_basic_relevance(self):
        query: str = "breach of contract"
        results: list[SimilarityScore] = search_documents(query, self.db)

        print_results(results, self.db)

        # Validate: doc1 and doc2 should be ranked highly
        doc1_success = "doc1" in [doc_id for doc_id, _ in results[:2]]
        doc2_success = "doc2" in [doc_id for doc_id, _ in results[:2]]

        self.assertTrue(doc1_success, "doc1 should be ranked highly")
        self.assertTrue(doc2_success, "doc2 should be ranked highly")

    # Test 2: Multiple term query (tests multiple terms in query)
    def test_multiple_term_query(self):
        query = "plaintiff damages negligence"
        results: list[SimilarityScore] = search_documents(query, self.db)

        print_results(results, self.db)

        # Validate: doc3 and doc4 should be ranked highly
        doc3_success = "doc3" in [doc_id for doc_id, _ in results[:2]]
        doc4_success = "doc4" in [doc_id for doc_id, _ in results[:2]]

        self.assertTrue(doc3_success, "doc3 should be ranked highly")
        self.assertTrue(doc4_success, "doc4 should be ranked highly")

    # Test 3: Partial match (tests exact match in one doc)
    def test_partial_match(self):
        query = "settlement agreement"
        results = search_documents(query, self.db)

        print_results(results, self.db)

        # Validate: doc5 should be ranked highest
        doc5_success = results and results[0].document_id == "doc5"
        self.assertTrue(doc5_success, "doc5 should be ranked highly")

    # Test 4: Case insensitive (tests preprocessing of text)
    def test_case_insensitivity(self):
        query = "NEGLIGENCE defendant"
        results: list[SimilarityScore] = search_documents(query, self.db)

        test_query = "negligence defendant"
        control_results: list[SimilarityScore] = search_documents(test_query, self.db)

        # Validate: Should have same top documents as "negligence defendant"
        self.assertIsNotNone(results)
        self.assertIsNotNone(control_results)
        self.assertEqual(results[0].document_id, control_results[0].document_id, "Top document should be the same")

    # Test 5: Empty query - test no exception is thrown inside search_documents
    def test_empty_query(self):
        query = ""
        search_documents(query, self.db)
        pass
