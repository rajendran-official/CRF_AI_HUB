# Setup instructions
How AI Works in This Project
Traditional searching looks for exact word matches (like pressing Ctrl + F). If you type "login issue," a traditional search will miss a row that says "sign-in page error," even though they mean the same thing.
This AI system uses Semantic Search. It reads your sentences, understands the real-world meaning and context behind your words, and finds matches based on intent and concepts, even if the exact words do not match.

Key AI Concepts Used Here
1. Text Embedding (Vectorization)
The AI turns text into a long string of numbers called a Vector Embedding. Think of it as a map with thousands of dimensions. Words or sentences with similar meanings are placed very close to each other on this map.
2. Transformer Models (all-MiniLM-L6-v2)
This is the specific pre-trained Large Language Model (LLM) used in your code. It has been trained on millions of sentences to understand English grammar, context, and vocabulary relationships perfectly. It runs completely locally on your machine.
3. Cosine Similarity
This is the math engine. Once your search query and your Excel rows are turned into numbers (vectors), the system measures the angle between them. If the angle is very small, the similarity score is high (e.g., 95% match), meaning the records are highly related.
Does it chunk the total Excel file?
No, it does not split your rows into random text chunks. Instead, it processes your Excel file through a structured, row-by-row method:
Row-by-Row Isolation: The script reads your Excel file row by row. Each row represents exactly one historical CRF record.
Context Assembly: For every single row, it combines key columns (Title, Description, Developer, Tester, Department) into one continuous string of text for that specific CRF.
Individual Mapping: The AI creates one dedicated embedding vector for each CRF row.

crf-ai-mapping-system/
│
├── .venv/                      # Python Virtual Environment (auto-generated)
├── data/                       # Storage for your database files
│   └── crf_data.xlsx           # Your master Excel file with 1000+ CRFs
│
├── core/                       # The AI Engine & Data Processing Logic
│   ├── __init__.py
│   ├── data_loader.py          # Handles Excel reading and validation
│   └── ai_search.py            # Sentence-Transformers & similarity logic
│
├── interface/                  # User Interface Layer
│   ├── __init__.py
│   └── web_app.py              # Streamlit local host dashboard layout
│
├── api/                        # Future Chatbot Integration Layer (Phase 2)
│   ├── __init__.py
│   └── routes.py               # FastAPI endpoints for chatbot webhooks
│
├── app.py                      # Main entry point to launch the application
├── requirements.txt            # Python library dependencies
└── README.md                   # Setup and execution instructions
"# CRF_AI_HUB" 
"# CRF_AI_HUB" 
