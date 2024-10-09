import spacy
nlp = spacy.load("en_core_web_sm")

def detect_topics(conversation):
    """Detect topics from a conversation using spaCy."""
    doc = nlp(conversation)
    topics = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) > 1]
    topic_freq = {topic: topics.count(topic) for topic in set(topics)}
    sorted_topics = sorted(topic_freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_topics
