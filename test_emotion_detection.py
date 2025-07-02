
import unittest
from EmotionDetection import emotion_detection as ED

test_data = {    
    "I am glad this happened" :	"joy",
    "I am really mad about this" : "anger",
    "I feel disgusted just hearing about this" : "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

class TestApp(unittest.TestCase):
    def test_emotion_detection(self):
        for inst in test_data:
            self.assertEqual(
                ED.emotion_detector(inst)['dominant_emotion'], test_data[inst])


if __name__ == '__main__':
    unittest.main()
