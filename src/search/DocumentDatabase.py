class Document:
    def __init__(self, document_id: str, text: str):
        self.document_id = document_id
        self.text = text


class DocumentDatabase:
    def __init__(self):
        self.documents = {}

    def add(self, document_id: str, document_text: str):
        self.documents[document_id] = Document(document_id, document_text)

    def get(self, document_id: str) -> Document:
        return self.documents[document_id]

    def list(self) -> list[Document]:
        return list(self.documents.values())

    def bootstrap_with_test_data(self):
        self.add("doc1", "The plaintiff alleges breach of contract and seeks damages for financial losses.")
        self.add("doc2", "The defendant denies all allegations and claims no breach of contract occurred."),
        self.add("doc3", "The court ruled in favor of the plaintiff, citing negligence by the defendant."),
        self.add("doc4",
                 "Legal precedent establishes that negligence requires proof of duty, breach, causation, and damages."),
        self.add("doc5", "The settlement agreement includes confidentiality provisions and liability limitations.")
