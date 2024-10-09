import streamlit as st
import spacy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Load spacy model for NER and tokenization
nlp = spacy.load("en_core_web_sm")
# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text.lower())
    clean_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return clean_tokens

# Function for sentiment analysis using VADER
def vader_sentiment_analysis(text):
    scores = vader_analyzer.polarity_scores(text)
    return scores['compound'], scores

# Function for TextBlob sentiment analysis
def textblob_sentiment_analysis(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Simplified emotion analysis based on keyword matching
def basic_emotion_analysis(text):
    emotions = {
        'happy': ['happy', 'joy', 'excited', 'pleased', 'delighted'],
        'sad': ['sad', 'down', 'unhappy', 'depressed', 'melancholy'],
        'angry': ['angry', 'mad', 'furious', 'irritated', 'annoyed'],
        'fear': ['fear', 'afraid', 'scared', 'frightened', 'terrified']
    }
    detected_emotions = []
    for emotion, keywords in emotions.items():
        if any(word in text.lower() for word in keywords):
            detected_emotions.append(emotion)
    
    return detected_emotions if detected_emotions else ['neutral']

# Function to analyze conversation by splitting based on speakers
def analyze_conversation(conversation):
    participants = {}
    for line in conversation.split('\n'):
        if ':' in line:
            speaker, message = line.split(':', 1)
            polarity, sentiment_scores = vader_sentiment_analysis(message)
            if speaker not in participants:
                participants[speaker] = {'messages': [], 'sentiment': [], 'emotion': []}
            participants[speaker]['messages'].append(message)
            participants[speaker]['sentiment'].append((polarity, sentiment_scores))
            participants[speaker]['emotion'].append(basic_emotion_analysis(message))
    return participants

# Function to analyze dominance in the conversation
def analyze_dynamics(conversation):
    lines = conversation.split('\n')
    speaker_counts = {}
    for line in lines:
        if ':' in line:
            speaker, message = line.split(':', 1)
            word_count = len(message.split())
            speaker_counts[speaker] = speaker_counts.get(speaker, 0) + word_count
    
    total_words = sum(speaker_counts.values())
    dominance = {speaker: (count / total_words) * 100 for speaker, count in speaker_counts.items()}
    return dominance

# Named Entity Recognition function
def named_entity_recognition(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to plot conversation dynamics
def plot_dynamics(dynamics):
    labels = list(dynamics.keys())
    sizes = list(dynamics.values())
    
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Streamlit App
def main():
    st.title("Human Relationship Analyzer")

    st.write("This app uses NLP techniques to analyze conversations and provide insights on relationship dynamics, sentiment, emotion, and more.")

    conversation = st.text_area("Enter the conversation (e.g. 'Alice: Hi Bob! ...'):")

    if st.button("Analyze"):
        if conversation:
            st.subheader("Sentiment Analysis per Speaker")
            participants_sentiment = analyze_conversation(conversation)
            for speaker in participants_sentiment:
                st.write(f"**{speaker}**")
                for i, message in enumerate(participants_sentiment[speaker]['messages']):
                    polarity, sentiment_scores = participants_sentiment[speaker]['sentiment'][i]
                    st.write(f"Message: {message}")
                    st.write(f"Sentiment (VADER): Polarity={polarity}, Detailed Scores={sentiment_scores}")
                    emotion = participants_sentiment[speaker]['emotion'][i]
                    st.write(f"Emotion: {emotion}")

            st.subheader("Conversation Dynamics (Dominance)")
            dynamics = analyze_dynamics(conversation)
            st.write(dynamics)
            plot_dynamics(dynamics)

            st.subheader("Named Entities")
            entities = named_entity_recognition(conversation)
            st.write(entities)

if __name__ == "__main__":
    main()
