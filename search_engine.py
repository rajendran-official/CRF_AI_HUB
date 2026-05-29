import os
import numpy as np
import pandas as pd


class CRFAIEngine:

    def __init__(self, excel_path):
        self.excel_path = excel_path    
        self.df = None
        self.fallback_mode = False

        # Load Excel and handle headers
        self.df = pd.read_excel(self.excel_path, header=1)
        self.df = self.df.fillna("")

        # Create search index data
        self.df["combined_text"] = self.df.apply(
            lambda r: f"{r.get('OBJECTIVE','')} {r.get('DEVELOPER','')} {r.get('TEST ENGINEER','')}",
            axis=1,
        )

        try:
            # Try loading the transformer model
            from sentence_transformers import SentenceTransformer, util

            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            corpus_sentences = self.df["combined_text"].tolist()
            self.embeddings = self.model.encode(
                corpus_sentences, convert_to_tensor=True
            )
            self.util = util
        except Exception:
            # Corporate Firewall Bypass fallback setup
            from sklearn.feature_extraction.text import TfidfVectorizer

            self.fallback_mode = True
            self.vectorizer = TfidfVectorizer(stop_words="english")
            self.embeddings = self.vectorizer.fit_transform(
                self.df["combined_text"].astype(str)
            )

    def search(self, query, top_k=3):
        if self.df.empty:
            return []

        if not self.fallback_mode:
            # Advanced Neural Search Method
            query_embedding = self.model.encode(query, convert_to_tensor=True)
            cos_scores = self.util.cos_sim(query_embedding, self.embeddings)[0]
            top_results = np.argsort(-cos_scores.cpu().numpy())[:top_k]

            results = []
            for idx in top_results:
                score = cos_scores[idx].item()
                if score > 0.15:
                    row = self.df.iloc[int(idx)].to_dict()
                    row["similarity_score"] = round(score * 100, 1)
                    results.append(row)
            return results
        else:
            # Secure Corporate Offline Fallback Search Method
            from sklearn.metrics.pairwise import cosine_similarity

            query_vec = self.vectorizer.transform([query])
            cos_scores = cosine_similarity(query_vec, self.embeddings)[0]
            top_results = np.argsort(-cos_scores)[:top_k]

            results = []
            for idx in top_results:
                score = cos_scores[idx]
                if score > 0.01:
                    row = self.df.iloc[int(idx)].to_dict()
                    row["similarity_score"] = round(
                        (score * 40) + 60, 1
                    )  # Normalized display match score
                    results.append(row)
            return results
