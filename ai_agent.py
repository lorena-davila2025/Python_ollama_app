from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2", temperature=0.6)


template = """
You are an expert answering questions about Python
Here are some relevant data structures: {structures}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("--" * 20 + "\n\n")
    question = input("Ask your question (q to quit): ").strip()
    if question.lower() == "q":
        break

    # Retrieve dcs relevant to the question
    structure_docs = retriever.invoke(question)
    result = chain.invoke({
        "question": question,
        "structures": structure_docs
    })

    print(result)
