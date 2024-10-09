import matplotlib.pyplot as plt
import streamlit as st

def plot_emotion_trends(participants):
    """Plot emotion trends over time for all participants."""
    emotions_over_time = {'happy': [], 'sad': [], 'angry': [], 'neutral': []}
    messages = []
    
    for speaker in participants:
        for i, message in enumerate(participants[speaker]['messages']):
            detected_emotions = participants[speaker]['emotion'][i]
            for emotion in emotions_over_time.keys():
                if emotion in detected_emotions:
                    emotions_over_time[emotion].append(1)
                else:
                    emotions_over_time[emotion].append(0)
            messages.append(f"{speaker}: {message}")
    
    # Plot the trends
    fig, ax = plt.subplots(figsize=(10, 6))
    for emotion, counts in emotions_over_time.items():
        ax.plot(range(len(messages)), counts, label=emotion)
    plt.xticks(range(len(messages)), messages, rotation=90)
    plt.legend()
    plt.title('Emotion Trends Over Time')
    plt.xlabel('Message Index')
    plt.ylabel('Emotion Presence (0 or 1)')
    st.pyplot(fig)
