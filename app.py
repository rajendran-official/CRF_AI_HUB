import io
import os
import pandas as pd
import streamlit as st
from search_engine import CRFAIEngine

st.set_page_config(page_title="CRF AI Assistant", layout="wide")
st.title("CRF AI Assistant")
st.caption("Ask me about previous CRFs, developers, testers, or modules.")

EXCEL_DIR = "data"
EXCEL_FILE = os.path.join(EXCEL_DIR, "CRFLIST.xlsx")


@st.cache_resource
def initialize_engine():
    return CRFAIEngine(EXCEL_FILE)


def convert_df_to_excel(df_to_download):
    """Converts a pandas DataFrame into bytes for Excel download."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_to_download.to_excel(writer, index=False, sheet_name="AI_Search_Results")
    return output.getvalue()


try:
    engine = initialize_engine()

    if engine.fallback_mode:
        st.info(" ")
    else:
        st.success(" Deep Learning Mode")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "type": "text",
                "content": "Hello! I am your CRF Tracking Bot. ",
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if msg["type"] == "text":
                st.markdown(msg["content"])
            elif msg["type"] == "dataframe":
                st.markdown(msg["content"])
                st.dataframe(pd.DataFrame(msg["data"]), use_container_width=True)

    if user_query := st.chat_input("Ask me about a CRF..."):

        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append(
            {"role": "user", "type": "text", "content": user_query}
        )

        with st.chat_message("assistant"):
            with st.spinner("Searching entire excel database..."):
                # We ask the engine to return ALL possible matches by setting top_k higher
                all_matches = engine.search(user_query, top_k=500)

            if not all_matches:
                response = f"I couldn't find any matching historical CRF records for '{user_query}'."
                st.markdown(response)
                st.session_state.messages.append(
                    {"role": "assistant", "type": "text", "content": response}
                )
            else:
                total_found = len(all_matches)
                intro_text = f"Found **{total_found}** matching historical records for **'{user_query}'**. Displaying the top 5 most relevant entries below:"
                st.markdown(intro_text)

                # Format everything into a display structure
                formatted_all_results = []
                for result in all_matches:
                    formatted_all_results.append(
                        {
                            "Match Confidence": f"{result['similarity_score']}%",
                            "Request ID": result.get("REQUEST ID", "N/A"),
                            "Objective / Scope": result.get("OBJECTIVE", "N/A"),
                            "Dev Techlead": result.get(
                                "DEVELOPER TECHLEAD", "N/A"
                            ),
                            "Developer": result.get("DEVELOPER", "N/A"),
                            "Test Techlead": result.get("TEST TECHLEAD", "N/A"),
                            "Test Engineer": result.get("TEST ENGINEER", "N/A"),
                            "Development Completed": result.get(
                                "DVLPMNT CMPLT", "N/A"
                            ),
                        }
                    )

                # Show only the top 5 entries inside the UI to keep it clean
                df_all = pd.DataFrame(formatted_all_results)
                df_top_5 = df_all.head(5)

                st.dataframe(df_top_5, use_container_width=True, hide_index=True)

                # Add a functional download button to fetch all matched rows
                excel_bytes = convert_df_to_excel(df_all)
                st.download_button(
                    label=f"📥 Download All {total_found} Results as Excel",
                    data=excel_bytes,
                    file_name=f"CRF_AI_Search_Results_{user_query}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "type": "dataframe",
                        "content": intro_text,
                        "data": df_top_5.to_dict(orient="records"),
                    }
                )

except Exception as e:
    st.error(f"Initialization Error: {e}")
