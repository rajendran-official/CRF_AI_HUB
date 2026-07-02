🔍 CRF AI Assistant

Python 3.8+StreamlitLicense: MIT

A Streamlit-based intelligent search engine for querying CRF data. Features semantic AI matching with a robust offline fallback for restricted corporate networks.

🚀 Get Started • 📂 Project Structure • ⚙️ Troubleshooting
📂 Folder Structure

CRF_AI_HUB/│├── app.py                 # Main Streamlit web application interface├── search_engine.py       # Core AI logic (Semantic search & TF-IDF fallback)├── requirements.txt       # Python dependencies├── .gitignore             # Files ignored by Git│└── data/                  # Directory containing the source Excel file    └── CRFLIST.xlsx       # Database of CRFs 

🛠️ Prerequisites

     Python 3.8 or higher installed on your system.
     Basic knowledge of running commands in a terminal/command prompt.

🚀 Setup and Installation

Follow these steps to get the application running locally:

1. Clone the repository
bash
 
  
 
 
git clone https://github.com/YOUR_USERNAME/CRF_AI_HUB.git
cd CRF_AI_HUB
 
 

2. Create a Virtual Environment (Recommended)
bash
 
  
 
 
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
 
 

3. Install Dependencies
bash
 
  
 
 
pip install -r requirements.txt
 
 
▶️ How to Run

Once the dependencies are installed and your Excel file is in the data/ folder, start the Streamlit server:
bash
 
  
 
 
streamlit run app.py
