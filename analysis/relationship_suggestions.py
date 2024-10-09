# utils/relationship_suggestions.py

def generate_suggestions(participants, dynamics, politeness_scores):
    suggestions = []

    # Balance in conversation dynamics
    max_speaker, max_percent = max(dynamics.items(), key=lambda item: item[1])
    if max_percent > 70:
        suggestions.append(f"Try to balance the conversation. {max_speaker} is speaking much more than others, encourage more participation from other participants.")

    # Politeness suggestions
    for speaker, politeness in politeness_scores.items():
        if politeness < 0:
            suggestions.append(f"{speaker} could use more polite phrases like 'please' or 'thank you' to improve the tone of the conversation.")
        elif politeness == 0:
            suggestions.append(f"{speaker} seems neutral. Adding more polite expressions might enhance the conversation.")

    # Negative sentiment suggestions
    for speaker in participants:
        negative_messages = [msg for i, msg in enumerate(participants[speaker]['messages']) if participants[speaker]['sentiment'][i][0] < -0.5]
        if negative_messages:
            suggestions.append(f"{speaker} has some negative messages. It's important to express concerns without too much criticism.")

    return suggestions
