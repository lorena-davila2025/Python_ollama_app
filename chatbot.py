from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}
Answer: """

model = OllamaLLM(model="llama3.2", temperature=0.8)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = chain.invoke({
            "context": context,
            "question": user_input})
        print("Bot: ", result)
        context +=f"\nYou: {user_input}\nBot: {result}"

if __name__ == "__main__":
    handle_conversation()
