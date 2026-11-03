import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Smoke tests for the Watson emotion detector."""

    def test_emotion_detector(self):
        result = emotion_detector("I am really mad about this")
        self.assertIn("emotionPredictions", result)
        self.assertIn("anger", result)


if __name__ == "__main__":
    unittest.main()
