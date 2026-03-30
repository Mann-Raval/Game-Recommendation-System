# 🎮 Game Recommendation System

A content-based game recommender system built using **Machine Learning** and deployed with **Streamlit**. This app suggests games similar to a user's selection based on features like genre, tags, and other metadata.

---

## 🚀 Demo

<img width="1905" height="1035" alt="Screenshot 2026-03-30 203411" src="https://github.com/user-attachments/assets/e1633100-f0db-4194-bf96-374b5c2f943a" />

---

## 📌 Features

* 🎯 Recommend similar games instantly
* ⚡ Fast similarity computation using cosine similarity
* 🧠 Content-based filtering approach
* 🎮 Uses game metadata like genres, tags, etc.
* 🖼️ Displays game posters using Steam CDN
* 🌐 Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle (for model storage)**

---

## 📂 Project Structure

```
Game-Recommendation-System/
│
├── app.py                  # Streamlit app
├── Game_recommender.ipynb  # Model building notebook
├── similarity.pkl          # Similarity matrix
├── stream_games.pkl        # Processed dataset
├── README.md
```

---

## ⚙️ How It Works

1. Data preprocessing and feature engineering are performed on a large dataset.
2. Important features like **genres, tags, etc.** are combined.
3. Text vectorization is applied (TF-IDF / CountVectorizer).
4. Cosine similarity is computed between games.
5. The system recommends top 5 similar games.

---

## 🖥️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Game-Recommendation-System.git
cd Game-Recommendation-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📊 Dataset

* Large game dataset (reduced to ~20,000 rows for performance)
* Dataset not included due to size limitations

---

## ⚠️ Notes

* Poster images are fetched dynamically using Steam CDN via `appid`
* Game names are not used as features to avoid biased recommendations

---

## 📈 Future Improvements

* 🔍 Add search & filtering (genre, rating)
* 🎯 Improve recommendation accuracy
* 🌙 Dark mode UI
* 🌐 Deploy on cloud (Streamlit Cloud / Render)
* 🤖 Hybrid recommendation system (content + collaborative)

---

## 🙌 Acknowledgements

* Steam dataset / game metadata sources
* Scikit-learn documentation
* Streamlit for easy deployment

---

## 📬 Contact

**Mann Raval**
GitHub: https://github.com/your-username

---

## Kaggle : https://www.kaggle.com/code/mann14/game-recommender/

⭐ If you like this project, consider giving it a star!
