def relationship_strength_analysis(participants, dynamics):
    """Analyze relationship strength based on sentiment and conversation balance."""
    total_polarity = 0
    total_messages = 0
    balance = min(dynamics.values()) / max(dynamics.values()) if len(dynamics) > 1 else 1

    for speaker in participants:
        for polarity, _ in participants[speaker]['sentiment']:
            total_polarity += polarity
            total_messages += 1

    avg_polarity = total_polarity / total_messages if total_messages else 0
    strength_score = (avg_polarity + balance) / 2  # A basic score combining sentiment and balance

    return strength_score
