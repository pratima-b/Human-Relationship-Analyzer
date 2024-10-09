import matplotlib.pyplot as plt
import streamlit as st

def plot_sentiment_heatmap(participants):
    """Plot sentiment heatmap to visualize conversation polarity."""
    sentiments = []
    messages = []

    for speaker in participants:
        for i, message in enumerate(participants[speaker]['messages']):
            polarity = participants[speaker]['sentiment'][i][0]  # VADER polarity score
            sentiments.append(polarity)
            messages.append(f"{speaker}: {message}")

    fig, ax = plt.subplots(figsize=(10, 6))
    heatmap = ax.imshow([sentiments], cmap="RdYlGn", aspect='auto', vmin=-1, vmax=1)

    plt.xticks(range(len(messages)), messages, rotation=90)
    plt.yticks([])
    plt.colorbar(heatmap)
    plt.title("Sentiment Heatmap (Green = Positive, Red = Negative)")
    st.pyplot(fig)
