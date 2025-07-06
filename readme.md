# Python Ollama App

A small Python application demonstrating how to integrate with Ollama using its Python SDK. Ideal for building chatbots or AI-powered tools with local or self-hosted LLMs such as Llama 3.2.

---

## 🚀 Features

- A simple chatbot powered by Ollama
- A lightweight AI agent that answers questions based on a CSV file about Python data structures

---

## 📦 Prerequisites

- Python 3.8+
- [Ollama CLI Tools](https://ollama.com/docs/guide/quickstart) installed and running locally
- At least one Ollama model pulled (e.g. `ollama pull llama3.2`)

---

## 🧩 Installation

```bash
git clone https://github.com/lorena-davila2025/Python_ollama_app.git
cd Python_ollama_app

# Create and activate a virtual environment
python3 -m venv env             # macOS/Linux/Windows
source env/bin/activate         # macOS/Linux
# .\env\Scripts\activate        # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
