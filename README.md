# 🎵 Spotify Music Trends & AI-Based Song Mood Prediction

### 🎧 Explore Music. Discover Trends. Predict Moods with AI.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas&logoColor=white)

---

## 📌 Project Overview

🎵 **Spotify Music Trends & AI-Based Song Mood Prediction** is an end-to-end data analytics and machine learning project that combines **Python, Machine Learning, and Power BI** to analyze Spotify music data and uncover meaningful patterns in songs, genres, popularity, and audio characteristics.

🤖 A **Random Forest classification model** is used to predict song moods based on Spotify audio features such as **energy, valence, danceability, acousticness, instrumentalness, speechiness, liveness, and tempo**.

📊 The processed data is then integrated into an interactive **Power BI dashboard** that allows users to explore music trends, analyze AI-predicted moods, filter songs by genre, and drill through to individual song details.

---

## 🎯 Project Objectives

🔹 Analyze Spotify songs and identify **music trends and patterns**

🔹 Explore relationships between **popularity, energy, danceability, and valence**

🔹 Analyze music characteristics across different **genres**

🔹 Develop an **AI-based song mood prediction system**

🔹 Classify songs into **Happy, Energetic, Chill, and Sad** moods

🔹 Calculate **prediction confidence** for each song

🔹 Build an interactive **Power BI dashboard** for data exploration

🔹 Enable **filters and drill-through navigation** for song-level analysis

---

## 🛠️ Technologies & Tools

| 🧰 Technology | 💡 Purpose |
|---|---|
| 🐍 **Python** | Data preprocessing and analysis |
| 🐼 **Pandas** | Data cleaning and manipulation |
| 🤖 **Scikit-learn** | Machine Learning model development |
| 🌲 **Random Forest** | Song mood classification |
| 📊 **Power BI** | Interactive dashboard and visualization |
| 📈 **DAX** | Power BI calculations and analytics |
| 🗄️ **SQL** | Data querying and analytical concepts |
| 📗 **Excel** | Dataset preparation and initial exploration |
| 💻 **VS Code** | Python development environment |

---

## 📂 Dataset & Data Processing

🎵 The project uses a Spotify tracks dataset containing information about songs, artists, genres, popularity, and audio features.

### 📊 Dataset Statistics

| 📌 Metric | 🔢 Value |
|---|---:|
| 🎵 Total Songs | **113,550** |
| 🎼 Features | **20+** |
| 🎧 Audio Features | **8+** |
| 🎭 Predicted Mood Categories | **4** |

### 🧹 Data Processing Workflow

The dataset was processed using Python before being imported into Power BI.

📥 **Raw Spotify Dataset**

⬇️

🧹 **Data Cleaning**

⬇️

🔍 **Missing Value Handling**

⬇️

♻️ **Duplicate Removal**

⬇️

📊 **Exploratory Data Analysis**

⬇️

🎭 **Rule-Based Mood Labelling**

⬇️

🤖 **Random Forest Model**

⬇️

🔮 **Mood Prediction**

⬇️

📈 **Prediction Confidence**

⬇️

📁 **Processed Dataset**

⬇️

📊 **Power BI Dashboard**

---

## 🤖 AI-Based Song Mood Prediction

The project uses a **Random Forest Classifier** to classify songs into four mood categories based on their Spotify audio characteristics.

### 🎭 Mood Classification

| 🎭 Mood | 🎵 Definition |
|---|---|
| 🎉 **Happy** | High valence + High energy |
| ⚡ **Energetic** | Low valence + High energy |
| 😌 **Chill** | High valence + Low energy |
| 😢 **Sad** | Low valence + Low energy |

### 🧠 Machine Learning Workflow


🎵 Spotify Audio Features
          ↓
📊 Feature Selection
          ↓
✂️ Train / Test Split
          ↓
🌲 Random Forest Classifier
          ↓
🔮 Mood Prediction
          ↓
📈 Prediction Probability
          ↓
🎯 Prediction Confidence

---

## 📊 Power BI Dashboard

The processed Spotify dataset was transformed into an interactive **Power BI dashboard** designed to provide both high-level music insights and detailed song-level exploration.

### 🏠 1. Spotify Music Intelligence

🎵 Provides an overall view of the Spotify dataset.

**Key elements:**

- 📌 Total Songs
- ⭐ Average Popularity
- ⚡ Average Energy
- 💃 Average Danceability
- 🎭 AI Predicted Mood Distribution
- 🎼 Top Genres by Popularity
- 📈 Energy vs Valence Mood Landscape

---

### 📈 2. Music Trends

Explores relationships between Spotify audio features and music popularity.

**Key analysis:**

- 🎼 Genre-level Energy vs Popularity
- ⚡ Average Popularity by Energy Level
- 🎭 Average Energy by AI Predicted Mood
- 💃 Average Danceability by AI Predicted Mood
- 🔎 Genre and Mood Filters

---

### 🤖 3. AI Mood Intelligence

Provides a deeper analysis of the AI-generated mood classifications.

**Key elements:**

- 🎯 Average AI Prediction Confidence
- 🎭 Song Count by Predicted Mood
- 🎧 AI Mood Audio Profile
- ⚡ Energy Analysis
- 💃 Danceability Analysis
- 😊 Valence Analysis
- 🎸 Acousticness Analysis

---

### 🔎 4. Song Explorer

Allows users to explore individual songs interactively.

**Features:**

- 🎵 Song Name
- 👤 Artist
- 🎼 Genre
- ⭐ Popularity
- 🎭 AI Predicted Mood
- 🎯 Prediction Confidence
- 🔽 Mood Filter
- 🔽 Genre Filter

---

### 🎵 5. Song Details

A dedicated **drill-through page** provides detailed information about an individual song.

**Song-level metrics include:**

- 🎵 Song Name
- 👤 Artist
- 💿 Album
- 🎼 Genre
- ⭐ Popularity
- ⚡ Energy
- 💃 Danceability
- 😊 Valence
- 🎯 AI Prediction Confidence

🔗 Users can select a song from **Song Explorer** and drill through to its detailed analysis.
