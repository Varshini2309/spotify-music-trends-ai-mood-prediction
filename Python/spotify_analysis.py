import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_excel("spotify_tracks_dataset.xlsx")

df = df.drop(columns=['Unnamed: 0'])

print(df.head())

print(df.columns.tolist())

print(df.isnull().sum())

df['artists'] = df['artists'].fillna('Unknown Artist')
df['album_name'] = df['album_name'].fillna('Unknown Album')
df['track_name'] = df['track_name'].fillna('Unknown Track')

print(df.isnull().sum().sum())

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Dataset shape after removing duplicates:", df.shape)

print(df[['popularity', 'danceability', 'energy', 'acousticness', 'instrumentalness', 'valence', 'tempo']].describe())

def assign_mood(row):
    if row['valence'] >= 0.5 and row['energy'] >= 0.5:
        return 'Happy'

    elif row['valence'] < 0.5 and row['energy'] >= 0.5:
        return 'Energetic'

    elif row['valence'] >= 0.5 and row['energy'] < 0.5:
        return 'Chill'

    else:
        return 'Sad'


df['mood'] = df.apply(assign_mood, axis=1)

print(df['mood'].value_counts())

import matplotlib.pyplot as plt

mood_counts = df['mood'].value_counts()

plt.figure(figsize=(8, 5))
mood_counts.plot(kind='bar')

plt.title('Distribution of Song Moods')
plt.xlabel('Mood')
plt.ylabel('Number of Songs')

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

features = [
    'danceability',
    'energy',
    'valence',
    'acousticness',
    'instrumentalness',
    'speechiness',
    'liveness',
    'tempo'
]

X = df[features]
y = df['mood']

print("Features used for AI:")
print(features)

print("X shape:", X.shape)
print("y shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Model training completed!")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

print(classification_report(y_test, y_pred))

df['predicted_mood'] = model.predict(df[features])

print(df[['track_name', 'artists', 'mood', 'predicted_mood']].head(10))

probabilities = model.predict_proba(df[features])

df['prediction_confidence'] = probabilities.max(axis=1)

print(df[['track_name', 'predicted_mood', 'prediction_confidence']].head(10))

df.to_csv("spotify_mood_prediction.csv", index=False)

print("Final dataset saved successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))