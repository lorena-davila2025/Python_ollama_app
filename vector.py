from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

vector_store = Chroma(
    collection_name="python_data_structures",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    dataframe = pd.read_csv("python_data_structures_comparison.csv")
    documents = []
    ids = []

    for index, row in dataframe.iterrows():
        document = Document(
            # CSV headers: Structure,Declaration,Type,Mutable,Ordered,Allows Duplicates,Common Methods,Typical Use Case
            page_content=row["Structure"] + " " +
            row["Declaration"] + " " +
            row["Type"] + " " +
            row["Mutable"] + " " +
            row["Ordered"] + " " +
            row["Allows Duplicates"] + " " +
            row["Common Methods"],
            # row["Typical Use Case"]

            metadata={"typical_use_case": row["Typical Use Case"],
                    "id": str(index)} # metadata is the doc data that we don't need to query
        )
        ids.append(str(index))
        documents.append(document)

    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}  # Number of related documents to retrieve
)
