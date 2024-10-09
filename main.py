import streamlit as st
from analysis.sentiment_analysis import vader_sentiment_analysis
from analysis.emotion_analysis import basic_emotion_analysis
from analysis.topic_detection import detect_topics
from analysis.toxic_behavior import analyze_toxicity
from analysis.politeness_detection import analyze_politeness
from analysis.relationship_strength import relationship_strength_analysis
from visualization.plot_dynamics import plot_dynamics
from visualization.plot_emotions import plot_emotion_trends
from visualization.plot_sentiment_heatmap import plot_sentiment_heatmap
from analysis.relationship_suggestions import generate_suggestions

def analyze_conversation(conversation):
    """Process the conversation and extract participants and their emotions/sentiment."""
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

def analyze_dynamics(conversation):
    """Analyze conversation dynamics and calculate word counts for dominance analysis."""
    lines = conversation.split('\n')
    speaker_dynamics = {}
    for line in lines:
        if ':' in line:
            speaker = line.split(':')[0]
            speaker_dynamics[speaker] = speaker_dynamics.get(speaker, 0) + 1
    return speaker_dynamics

# Main Streamlit app
st.title("Human Relationship Analyzer")

conversation_input = st.text_area("Enter conversation (Speaker: Message format):")

if st.button("Analyze"):
    if conversation_input:
        participants = analyze_conversation(conversation_input)
        dynamics = analyze_dynamics(conversation_input)
        
        # Toxicity Analysis
        st.subheader("Toxic Behavior Detection")
        toxic_messages = analyze_toxicity(participants)
        st.write("Toxic messages:", toxic_messages)

        # Politeness Analysis
        st.subheader("Politeness Detection")
        politeness_scores = analyze_politeness(participants)
        st.write("Politeness scores:", politeness_scores)

        # Relationship Strength Analysis
        st.subheader("Relationship Strength Analysis")
        strength_score = relationship_strength_analysis(participants, dynamics)
        st.write(f"Relationship Strength Score: {strength_score:.2f}")

        # Visualization
        st.subheader("Conversation Dynamics")
        plot_dynamics(dynamics)

        st.subheader("Emotion Trends")
        plot_emotion_trends(participants)

        st.subheader("Sentiment Heatmap")
        plot_sentiment_heatmap(participants)

        st.subheader("Relationship Improvement Suggestions")
        suggestions = generate_suggestions(participants, dynamics, politeness_scores)
        if suggestions:
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.write("No significant suggestions at the moment.")
