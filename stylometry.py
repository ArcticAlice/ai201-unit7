"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, measured as the coefficient of variation
    (standard deviation divided by mean sentence length in words).

    Returns:
        A float (typically 0.0 to 1.0+). Higher means more variation (more human-like).
        Fewer than 2 sentences returns 0.0.
    """
    sents = sentences(text)
    if len(sents) < 2:
        return 0.0
    lengths = [len(words(s)) for s in sents]
    mean_len = statistics.mean(lengths)
    if mean_len == 0:
        return 0.0
    stdev = statistics.stdev(lengths)
    return round(stdev / mean_len, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words (Type-Token Ratio).

    Returns:
        A float between 0.0 and 1.0. Higher means more varied vocabulary.
    """
    all_words = words(text)
    if not all_words:
        return 0.0
    return round(len(set(all_words)) / len(all_words), 4)


def punctuation_density(text: str) -> float:
    """
    Punctuation marks per word (looking particularly at commas, semicolons,
    colons, dashes, and parentheses).

    Returns:
        A float. Higher means denser punctuation.
    """
    all_words = words(text)
    if not all_words:
        return 0.0
    punct_count = len(re.findall(r"[,;:\-—()\"']", text))
    return round(punct_count / len(all_words), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combines sentence length spread, type-token ratio, and punctuation density.
    Human writing tends to have high sentence length variance, rich vocabulary,
    and distinct punctuation patterns. AI tends toward uniform sentence
    cadence and repetitive structure.
    """
    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punct = punctuation_density(text)

    # If text is too short to measure style reliably, return neutral 0.5
    all_words = words(text)
    if len(all_words) < 8:
        return 0.5

    # 1. Sentence length variation: spread > 0.6 is very human (score near 0.1),
    # spread < 0.2 is very uniform / AI-like (score near 0.8).
    # Invert so higher = more AI.
    spread_ai = max(0.0, min(1.0, 1.0 - (spread / 0.70)))

    # 2. Type-token ratio: ttr > 0.80 is very diverse (human), ttr < 0.55 is repetitive (AI).
    # Invert so higher = more AI.
    ttr_ai = max(0.0, min(1.0, (0.80 - ttr) / 0.35))

    # 3. Punctuation density: very low punctuation (< 0.04) or extremely flat punctuation
    # tends to correlate with simpler machine generation.
    punct_ai = max(0.0, min(1.0, 1.0 - (punct / 0.15)))

    # Weighted combination of style features:
    # 50% sentence spread (strongest indicator of AI cadence),
    # 30% vocabulary diversity (TTR),
    # 20% punctuation density.
    score = 0.50 * spread_ai + 0.30 * ttr_ai + 0.20 * punct_ai
    return round(max(0.0, min(1.0, score)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
