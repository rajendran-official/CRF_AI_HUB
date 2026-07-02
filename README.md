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
