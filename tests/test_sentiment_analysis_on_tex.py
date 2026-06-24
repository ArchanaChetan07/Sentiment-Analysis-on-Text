import pytest
import re


class TestTextPreprocessing:

    def test_lowercase_conversion(self):
        text = "Hello World THIS IS A TEST"
        assert text.lower() == "hello world this is a test"

    def test_punctuation_removal(self):
        text = "Hello, world! How are you?"
        clean = re.sub(r'[^\w\s]', '', text)
        assert ',' not in clean and '!' not in clean

    def test_empty_string_handling(self):
        text = ""
        tokens = text.split()
        assert tokens == []

    def test_stopword_removal(self):
        stopwords = {"the", "is", "a", "an", "in", "on", "at"}
        tokens = ["the", "cat", "is", "on", "a", "mat"]
        filtered = [t for t in tokens if t not in stopwords]
        assert filtered == ["cat", "mat"]

    def test_tokenization(self):
        text = "I love natural language processing"
        tokens = text.split()
        assert len(tokens) == 5
        assert tokens[0] == "I"


class TestSentimentScoring:

    def test_positive_words_detected(self):
        positive_words = {"good", "great", "excellent", "love", "happy"}
        text = "I love this great product"
        tokens = text.lower().split()
        score = sum(1 for t in tokens if t in positive_words)
        assert score > 0

    def test_negative_words_detected(self):
        negative_words = {"bad", "terrible", "hate", "awful", "poor"}
        text = "This is a terrible and awful experience"
        tokens = text.lower().split()
        score = sum(1 for t in tokens if t in negative_words)
        assert score >= 2

    def test_neutral_text_scores_near_zero(self):
        positive_words = {"good", "great", "love"}
        negative_words = {"bad", "hate", "terrible"}
        text = "The cat sat on the mat"
        tokens = text.lower().split()
        pos = sum(1 for t in tokens if t in positive_words)
        neg = sum(1 for t in tokens if t in negative_words)
        assert pos == 0 and neg == 0

    def test_sentiment_label_assignment(self):
        def label(score):
            if score > 0: return "positive"
            if score < 0: return "negative"
            return "neutral"
        assert label(3) == "positive"
        assert label(-2) == "negative"
        assert label(0) == "neutral"
