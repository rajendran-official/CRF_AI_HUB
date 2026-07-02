CRF AI Assistant

A Streamlit-based intelligent search engine for querying CRF (Change Request / Configuration Request) data. It allows users to search by global keywords, CRF IDs, or specific personnel using semantic AI matching, with a built-in fallback for restricted corporate networks.
📁 Folder Structure

Create a folder for your project and organize the files exactly as shown below:
text
 
  
 
 
crf-ai-assistant/
│
├── app.py                 # Main Streamlit web application interface
├── search_engine.py       # Core AI logic (Semantic search & TF-IDF fallback)
├── requirements.txt       # Python dependencies
│
└── data/                  # Directory containing the source Excel file
    └── CRFLIST.xlsx       # Database of CRFs (Ensure correct format, see notes below)
 
 
🛠️ Prerequisites

     Python 3.8 or higher installed on your system.
     Basic knowledge of running commands in a terminal/command prompt.

🚀 Setup and Installation

Follow these steps to get the application running locally:

1. Clone or Download the Project
Open your terminal and navigate to your project folder:
bash
 
  
 
 
cd path/to/crf-ai-assistant
 
 

2. Create a Virtual Environment (Recommended)
bash
 
  
 
 
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
 
 

3. Create requirements.txt
Create a file named requirements.txt in the root directory and paste the following:
text
 
  
 
 
streamlit
pandas
openpyxl
numpy
scikit-learn
sentence-transformers
torch
 
 

4. Install Dependencies
Run the following command to install all required libraries:
bash
 
  
 
 
pip install -r requirements.txt
 
 

(Note: Installing sentence-transformers and torch may take a few minutes as they are large libraries).
▶️ How to Run

Once the dependencies are installed and your Excel file is in place, start the Streamlit server by running:
bash
 
  
 
 
streamlit run app.py
 
 

This will automatically open the CRF AI Assistant in your default web browser (usually at http://localhost:8501).
⚠️ Important Notes & Troubleshooting
1. Excel File Formatting (Crucial)

The search_engine.py is configured to read the Excel file with header=1. 

     This means it ignores the first row (Row 1) and treats the second row (Row 2) as the column headers.
     Ensure your CRFLIST.xlsx has the actual column names (like DRAFT_ID, REQUEST_ID, OBJECTIVE, DEVELOPER_TECHLEAD, etc.) in the second row.

2. Corporate Firewall / Offline Fallback

If you are running this in a restricted corporate environment where downloading the all-MiniLM-L6-v2 AI model is blocked by a firewall, do not worry. 

     The application is programmed to catch this error.
     It will automatically switch to a Fallback Mode using scikit-learn's TfidfVectorizer. 
     You will still get highly accurate keyword and text-matching results without needing external internet access to download the AI model.

3. First-Time AI Model Download

If you have internet access, the very first time you run a keyword search, the application will download the all-MiniLM-L6-v2 model (~90MB). Subsequent searches will be much faster as the model is cached locally.
4. Adjusting Search Sensitivity

     AI Mode: If results are too broad or too narrow, you can adjust the score > 0.25 threshold inside the search() method in search_engine.py.
     Fallback Mode: You can adjust the score > 0.10 threshold for the TF-IDF cosine similarity.
