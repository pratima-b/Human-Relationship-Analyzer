def detect_toxic_behavior(text):
    """Detect toxic behavior based on specific keywords."""
    toxic_keywords = ['stupid', 'hate', 'idiot', 'dumb', 'worthless']
    for word in toxic_keywords:
        if word in text.lower():
            return True
    return False

def analyze_toxicity(participants):
    """Analyze participants' messages for toxic behavior."""
    toxic_messages = []
    for speaker in participants:
        for message in participants[speaker]['messages']:
            if detect_toxic_behavior(message):
                toxic_messages.append(f"{speaker}: {message}")
    return toxic_messages
