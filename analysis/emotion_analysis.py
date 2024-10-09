def basic_emotion_analysis(text):
    """Perform basic emotion analysis based on keyword matching."""
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
