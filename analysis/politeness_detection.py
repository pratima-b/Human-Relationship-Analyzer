def detect_politeness(text):
    """Detect politeness and impoliteness in the conversation."""
    polite_words = ['please', 'thank you', 'sorry', 'excuse me']
    impolite_words = ['now', 'do it', 'shut up']

    politeness_score = sum([1 for word in polite_words if word in text.lower()])
    impoliteness_score = sum([1 for word in impolite_words if word in text.lower()])

    return politeness_score - impoliteness_score

def analyze_politeness(participants):
    """Analyze politeness levels for each participant."""
    politeness_scores = {}
    for speaker in participants:
        politeness = 0
        for message in participants[speaker]['messages']:
            politeness += detect_politeness(message)
        politeness_scores[speaker] = politeness
    return politeness_scores
